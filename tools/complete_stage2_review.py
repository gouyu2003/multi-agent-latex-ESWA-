"""Apply reviewed stage-two decisions; never infer scientific support from metadata."""
from __future__ import annotations
from project_paths import project_path
import csv
import copy
import hashlib
import json
import re
import sys
from collections import Counter
from dataclasses import asdict
from pathlib import Path

from bs4 import BeautifulSoup
from active_tex import scan_manuscript
from build_reference_inventory import balanced_entries, parse_fields, publication_venue

ROOT = Path(__file__).resolve().parents[1]
WORK = project_path('audit_work')
SPEC = json.loads((WORK / 'stage2_completion_review_spec.json').read_text(encoding='utf-8'))
BASE = json.loads((WORK / 'stage2_completion_baseline.json').read_text(encoding='utf-8'))
FIELDS = ('author', 'title', 'year', 'venue', 'volume', 'number', 'pages', 'doi', 'url', 'type')

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def dump(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def set_field(raw, name, value):
    body_start = raw.find(',') + 1
    body = raw[body_start:raw.rfind('}')]
    matches = list(re.finditer(r'(?ms)^\s*([A-Za-z][\w-]*)\s*=\s*', body))
    for i, m in enumerate(matches):
        if m.group(1).lower() != name:
            continue
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        old = body[m.end():end]
        padding = old[len(old.rstrip()):]
        comma = ',' if old.rstrip().endswith(',') else ''
        new = '{' + value + '}' + comma + padding
        return raw[:body_start + m.end()] + new + raw[body_start + end:]
    pos = raw.rfind('}')
    prefix = raw[:pos].rstrip()
    if not prefix.endswith(','):
        prefix += ','
    return prefix + '\n  ' + name + ' = {' + value + '},\n' + raw[pos:]

def canonical(value):
    return re.sub(r'[^\w]+', '', str(value).lower())

def apply_changes():
    for name in ('manuscript.tex', 'references.bib', 'literature_audit.csv'):
        if sha(project_path(name)) != BASE['files'][name]:
            raise ValueError('Apply requires the reviewed original snapshot: ' + name)
    old_scan = scan_manuscript(ROOT)
    text_bytes = (project_path('manuscript.tex')).read_bytes()
    newline = '\r\n' if text_bytes.count(b'\r\n') == text_bytes.count(b'\n') else '\n'
    if b'\r\n' in text_bytes and newline == '\n':
        raise ValueError('Mixed newline source requires explicit byte-level handling')
    text = text_bytes.decode('utf-8').replace('\r\n', '\n')
    hidden_before = re.findall(r'\\iffalse\b.*?\\fi\b', text, re.S)
    log = []
    for item in SPEC['manuscript_edits']:
        old = item['before']
        if text.count(old) != 1:
            raise ValueError('Nonunique/unmatched prose replacement: ' + old[:130])
        if any(old in block for block in hidden_before):
            raise ValueError('Attempt to alter protected hidden text')
        line = text[:text.index(old)].count('\n') + 1
        text = text.replace(old, item['after'], 1)
        log.append(dict(item, applied_line_before_this_edit=line, audit_date=SPEC['audit_date']))
    if re.findall(r'\\iffalse\b.*?\\fi\b', text, re.S) != hidden_before:
        raise ValueError('Hidden block changed')
    (project_path('manuscript.tex')).write_bytes(text.replace('\n', newline).encode('utf-8'))
    new_scan = scan_manuscript(ROOT)
    if [c.keys for c in new_scan.citations] != [c.keys for c in old_scan.citations]:
        (project_path('manuscript.tex')).write_bytes(text_bytes)
        raise ValueError('Citation ordering/coverage changed unexpectedly; restored manuscript')
    dump(WORK / 'stage2_manuscript_correction_log.json', log)
    old_bib = (project_path('references.bib')).read_text(encoding='utf-8')
    entries = balanced_entries(old_bib)
    by_key = {key: (kind, raw) for kind, key, raw in entries}
    bibliography_log = []
    for item in SPEC['bibliography_edits'] + SPEC.get('additional_bibliography_edits', []):
        key, name = item['key'], item['field']
        kind, raw = by_key[key]
        fields = parse_fields(raw)
        if fields.get(name, '') != item['before']:
            raise ValueError(f'Stale bibliographic edit {key}:{name}')
        by_key[key] = (kind, set_field(raw, name, item['after']))
        bibliography_log.append(dict(item, audit_date=SPEC['audit_date']))
    # Publisher-deposited records have already been inspected against paper identity.
    # Fill only missing page/issue values; contradictory values require the explicit decisions above.
    for path in sorted((project_path('audits/references/stage2_sources')).glob('*__crossref.json')):
        key = path.stem.removesuffix('__crossref')
        if key not in by_key:
            continue
        message = json.loads(path.read_text(encoding='utf-8'))['message']
        kind, raw = by_key[key]
        fields = parse_fields(raw)
        if fields.get('doi', '').lower() != message['DOI'].lower():
            raise ValueError('DOI identity differs: ' + key)
        for field, attribute in (('pages', 'page'), ('number', 'issue')):
            value = message.get(attribute, '')
            if not value or fields.get(field):
                continue
            after = re.sub(r'(?<=\d)-(?=\d)', '--', str(value)) if field == 'pages' else str(value)
            raw = set_field(raw, field, after)
            fields[field] = after
            bibliography_log.append({'key': key, 'field': field, 'before': '', 'after': after,
                'evidence_url': 'https://api.crossref.org/works/' + message['DOI'],
                'locator': 'Publisher-deposited ' + attribute + ' field; evidence snapshot ' + path.relative_to(ROOT).as_posix(),
                'reason': '已检查作品身份；补入可核实的正式页码/期号，非根据PDF页数推算。', 'audit_date': SPEC['audit_date']})
        by_key[key] = (kind, raw)
    bibliography = old_bib
    for _, key, raw in entries:
        bibliography = bibliography.replace(raw, by_key[key][1], 1)
    with (project_path('references.bib')).open('w', encoding='utf-8', newline='') as handle:
        handle.write(bibliography.replace('\n', '\r\n'))
    dump(WORK / 'stage2_reference_correction_log.json', bibliography_log)
    refresh_evidence(new_scan, bibliography_log)

def refresh_evidence(scan, changes):
    entries = {key: (kind, parse_fields(raw)) for kind, key, raw in balanced_entries((project_path('references.bib')).read_text(encoding='utf-8'))}
    changed_fields = {(c['key'], c['field']): c for c in changes}
    primary = {}
    for path in (project_path('audits/references/stage2_sources')).glob('*__crossref.json'):
        key = path.stem.removesuffix('__crossref')
        primary[key] = (json.loads(path.read_text(encoding='utf-8'))['message'], path)
    cases = {c['citation_id']: c for c in SPEC['cases']}
    core = {r['key']: r for r in SPEC['core_eligibility']}
    current_citations = {c.command_id: c for c in scan.citations}
    hashes = {name: sha(project_path(name)) for name in ('manuscript.tex', 'references.bib')}
    extra_sources = {
        'wu2024autogen': ('D:/multi-agent review_joural/10.10ziliao/1328_AutoGen_Enabling_Next_Gen.pdf', 'COLM2024 formal PDF p1; §§2.1–2.2 pp3–6; §3 A5 p9', 'Conversable agents use developer-defined conversation control; GroupChatManager selects speakers and broadcasts responses.'),
        'khattab2024dspy': ('https://proceedings.iclr.cc/paper_files/paper/2024/file/f1cf02ce09757f57c3b93c0db83181e0-Paper-Conference.pdf', 'Formal ICLR2024 PDF p1; §§3–4', 'Declarative modules and metric-driven compilation optimize language-model pipelines.'),
        'asai2024selfrag': ('https://proceedings.iclr.cc/paper_files/paper/2024/file/25f7be9694d7b32d5cc670927b8091e1-Paper-Conference.pdf', 'Formal ICLR2024 PDF p1; §3/Algorithm1 pp3–5', 'Reflection tokens guide on-demand retrieval and critique in one trained language model.'),
        'mialon2024gaia': ('https://proceedings.iclr.cc/paper_files/paper/2024/file/25ae35b5b1738d80f1f03a8713e405ec-Paper-Conference.pdf', 'Formal ICLR2024 PDF p1; §§3.1–3.2 pp4–6', 'Six authors including Craig Swift; assistant tasks require reasoning, information access and tools.'),
        'anthropic2024mcp': ('https://www.anthropic.com/news/model-context-protocol', 'Dated announcement25November2024, Model Context Protocol section; versioned2024-11-05 spec as supplementary evidence', 'MCP defines connections between applications and tools/data; orchestration policy remains application design.'),
        'google2025a2a': ('https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/', 'Dated announcement9April2025, byline; design principles; How A2A works', 'Four named authors describe capability discovery, task lifecycle and cross-framework agent messages.'),
        'crewai2023': ('https://pypi.org/project/crewai/0.1.0/', 'Version0.1.0 release14November2023, Credits; Agent/Task/Crew/Process.sequential', 'The pinned release provides roles, tasks and sequential processes; later capabilities are not assumed.'),
        'dify2024': ('https://raw.githubusercontent.com/langgenius/dify/0.6.0/README.md', 'Tagged0.6.0 README introduction/features; LICENSE; official release8April2024', 'The pinned release supplies RAG, agent capabilities and workflow orchestration, not automatic architecture selection.'),
        'ragflow2024': ('https://raw.githubusercontent.com/infiniflow/ragflow/v0.6.0/README.md', 'Tagged0.6.0 README What is RAGFlow/Key Features; official release21May2024', 'The pinned release supports deep document parsing, retrieval, grounded citations and configurable RAG components.'),
        'packer2023memgpt': ('https://arxiv.org/pdf/2310.08560v1', 'v1 §§2.1–2.2 pp3–4', 'Function calls manage main context and external memory; this is not attention-weight eviction.'),
        'cui2023chatlaw': ('https://arxiv.org/pdf/2306.16092v1', 'v1 p1 and §2', 'The2023 legal model integrates external knowledge; it does not validate proposed oversight policies.'),
        'huang2023agentcoder': ('https://arxiv.org/pdf/2312.13010v1', 'v1 p1 and §§3.1–3.4 pp3–4', 'Five authors; two LLM roles generate code/tests, and a scripted executor supplies acceptance and feedback.')}
    all_refs = []
    for evidence_path in sorted(WORK.glob('ledger_evidence_*.json')):
        data = json.loads(evidence_path.read_text(encoding='utf-8'))
        data['stage2_completion_review'] = {'audit_date': SPEC['audit_date'], 'review_spec': 'audit_work/stage2_completion_review_spec.json', 'previous_source_hashes': data.get('source_hashes'), 'context_review': SPEC['previous_audit_reuse']}
        for row in data['references']:
            key = row['key']; kind, fields = entries[key]
            current = {n: kind if n == 'type' else publication_venue(fields) if n == 'venue' else fields.get(n, '') for n in FIELDS}
            row['stage2_prior_fields'] = {n: dict(check) for n, check in row['field_checks'].items()}
            for n in FIELDS:
                check = row['field_checks'][n]
                check['current'] = current[n]
                change = changed_fields.get((key, n))
                if n == 'venue':
                    change = next((changed_fields[(key, x)] for x in ('journal', 'booktitle', 'howpublished', 'publisher') if (key, x) in changed_fields and fields.get(x) == current[n]), None)
                if change:
                    check.update(status='verified', expected=current[n], evidence_url=change['evidence_url'], notes=change['reason'] + '；定位：' + change['locator'])
                elif check['status'] in ('normalization_suggested', 'recommended_normalization', 'minor_name_difference', 'minor_variant', 'source_name_variant'):
                    check.update(status='verified', expected=current[n], notes='正式姓名/题名字形的可接受书目表示；作者人数及顺序保持，省略中间名或装饰音符不改变作品身份。')
                if not current[n] and n in ('volume', 'number', 'pages'):
                    exempt = kind in ('misc', 'book') or 'arXiv preprint' in current['venue'] or (n in ('volume', 'number') and kind == 'inproceedings')
                    if exempt:
                        check.update(status='not_applicable', expected='', evidence_url=row['official_sources'][0]['url'], notes='所选来源/整本书引用类型允许省略此字段；非证明该作品在所有其他版本都没有该字段。会议卷信息已在venue/series中表示时不重复推填。')
                if key in primary:
                    message, path = primary[key]; url = 'https://api.crossref.org/works/' + message['DOI']
                    value = message.get({'pages':'page','number':'issue','volume':'volume','doi':'DOI'}.get(n, ''), '')
                    if value and canonical(current[n]) == canonical(value):
                        check.update(status='verified', expected=current[n], evidence_url=url, notes='与已核作品的出版商登记字段一致；快照：' + path.relative_to(ROOT).as_posix())
                    if n == 'url' and current[n].startswith('https://doi.org/') and current[n].split('doi.org/', 1)[1].lower() == message['DOI'].lower():
                        check.update(status='verified', expected=current[n], evidence_url=url, notes='出版商登记DOI对应的规范标识符URL已核；不据此声称出版社网页不存在访问限制。')
                if n == 'type' and 'arXiv preprint' in current['venue']:
                    check.update(status='verified', expected=kind, evidence_url=current['url'], notes='article为标明arXiv预印本的BibTeX约定，非声称它是正式期刊论文。')
            if key in extra_sources:
                url, locator, evidence = extra_sources[key]
                row['official_sources'].append({'url':url, 'locator':locator, 'evidence':evidence, 'access_level':'formal_full_text_user_provided_pdf' if key == 'wu2024autogen' else 'official_versioned_or_dated_primary_source', 'checked_date':SPEC['audit_date'], 'provenance':'Current authorized stage-two review; source snapshot/identifier retained.'})
            if key == 'wu2024autogen':
                for n in ('author','title','year','venue','type'):
                    row['field_checks'][n].update(status='verified', expected=current[n], evidence_url=extra_sources[key][0], notes='COLM2024正式PDF首页直接核实；14位作者按原顺序。PDF有46页，不把此篇幅编造为正式书目页码。')
                row['existence_status'] = 'verified_formal_colm2024_pdf'
            if key in ('anthropic2024mcp','google2025a2a','dify2024','ragflow2024','crewai2023'):
                for n in ('author','title','year','venue','url','type'):
                    row['field_checks'][n].update(status='verified', expected=current[n], evidence_url=extra_sources[key][0], notes='采用已核查的具日期公告或指定历史发行版本；定位：' + extra_sources[key][1])
                row['existence_status'] = 'verified_selected_dated_or_versioned_technical_source'
            if key in ('khattab2024dspy','asai2024selfrag','mialon2024gaia','guha2023legalbench'):
                source = extra_sources.get(key, (row['official_sources'][-1]['url'], 'FormalPDFp1', ''))
                row['field_checks']['author'].update(status='verified', expected=current['author'], evidence_url=source[0], notes='人数及顺序按正式PDF核对；保留网页/全文差异历史。Self-RAG使用官方元数据Zeqiu以及全文Avirup全名，非声称所有来源显示完全相同。')
            prior_extra_checks = copy.deepcopy(row.get('additional_field_checks', {}))
            row['additional_field_checks'] = {n:(prior_extra_checks[n] if n in prior_extra_checks and prior_extra_checks[n].get('current') == value else {'current':value,'status':'not_verified','expected':'','evidence_url':'','notes':'本次未取得字段级证明的非必填附加字段，明确保留未核实。'}) for n,value in fields.items() if n not in FIELDS and n not in ('journal','booktitle','howpublished') and not (n == 'publisher' and kind == 'book')}
            for n, check in row['additional_field_checks'].items():
                if (key,n) in changed_fields:
                    change = changed_fields[(key,n)];check.update(status='verified', expected=check['current'], evidence_url=change['evidence_url'], notes=change['reason'])
                elif key in primary and n == 'publisher':
                    message, path = primary[key]
                    if canonical(check['current']) in canonical(message.get('publisher','')):
                        check.update(status='verified', expected=check['current'], evidence_url='https://api.crossref.org/works/'+message['DOI'], notes='出版商登记机构名称的可接受全称或缩写。')
                elif key == 'tang2025llmmedqa' and n == 'organization':
                    check.update(status='verified', expected='IEEE', evidence_url='https://api.crossref.org/works/10.1109%2FIJCNN64981.2025.11228647', notes='正式PDF会议版权及出版商登记确认IEEE。')
            if key in core:
                row['eligibility_review'] = core[key]
            row['current'] = {'type':kind, **fields}
            row['metadata_status'] = 'current_stage2_field_review_complete_with_explicit_optional_limits'
            row['recommendation'] = '当前字段和版本已逐项处理；余下未核实字段以当前field_checks为准，不为补齐而编造。历史issues保存在审计历史。'
            row['stage2_prior_issue_states'] = row.get('issue_states', [])
            row['issue_states'] = [{'field':n, 'state':'pending_optional_field', 'resolution':check.get('notes','')} for n,check in {**row['field_checks'], **row['additional_field_checks']}.items() if check['status'] not in ('verified','not_applicable')]
            row['stage2_prior_issues'] = row.get('issues', [])
            row['issues'] = [f"[current optional limitation] {n}: {check.get('notes','')}" for n,check in {**row['field_checks'], **row['additional_field_checks']}.items() if check['status'] not in ('verified','not_applicable')]
            all_refs.append(row)
        for row in data['citations']:
            cid = row['command_id']; citation = current_citations[cid]
            row['stage2_prior_context'] = {'original_sentence':row.get('original_sentence'), 'context':row.get('context'), 'line':row.get('line'), 'assessments':copy.deepcopy(row['by_key_assessments'])}
            row.update(asdict(citation))
            for a in row['by_key_assessments']:
                key = a['key']
                if key in extra_sources:
                    url, locator, evidence = extra_sources[key]
                    a.update(evidence_url=url, source_urls=[url], locator=locator, source_evidence=evidence, evidence_access_level='formal_full_text_user_provided_pdf' if key=='wu2024autogen' else 'official_versioned_or_dated_primary_source')
                if cid in cases:
                    case = cases[cid]
                    a.update(support_degree='author_inference', evidence_url=case['evidence_url'], source_urls=[case['evidence_url']], locator=case['locator'], source_evidence=case['source_evidence'], recommendation='统一控制权编码已实施；源流程获支持，架构标签和匹配为本文回顾性判断。见case_classification_audit.json；不是来源自报标签或性能/安全保证。')
                elif cid in ('C009','C010','C011'):
                    a.update(support_degree='direct', recommendation='仅引用作品身份和发表日期；历史增补以working records注明，未把论文存在当作原始检索操作证明。')
                elif cid == 'C031':
                    a.update(support_degree='direct', recommendation='当前只说跨reasoner答案对比；已撤去全部来源均证明普遍优于自我修正的含义。')
                elif cid in ('C050','C054','C055','C056','C073','C104','C108','C109','C110'):
                    a.update(support_degree='author_inference', recommendation='具体机制/资源能力获来源支持；控制权类别、适用情境及局限属于明确标注的作者分析。无条件flat/hybrid标签已移除。')
                elif cid in ('C112','C115','C124','C125'):
                    a.update(support_degree='direct', recommendation='当前具体机制按所选正式全文或历史版本复核；条件性设计分析不作为来源已验证效果。')
                if key in core and cid not in cases:
                    a.update(locator=core[key]['locator'], source_evidence=core[key]['method_evidence'], evidence_url=next((u for u in core[key]['sources'] if u.endswith('.pdf') or '/pdf/' in u), a['evidence_url']))
                    if cid == 'C098':
                        a['support_degree'] = 'direct'
                if key == 'wu2024autogen':
                    a['recommendation'] = '按COLM2024正式§§2.1–2.2及§3A5复核；通用选择/部署建议保持作者分析，不归为该文实测效果。'
                if cid == 'C131':
                    a['support_degree'] = 'author_inference'
                    a['recommendation'] = '所选版本支持基本可复用组件；自动组装和部署前验证仍是本文提出的方案，不是原资源验证的选择策略。'
                if cid == 'C132' and key == 'kim2024mdagents':
                    a['recommendation'] = '复杂度驱动的solo/MDT/ICT路由已在正式§3核实；不扩展为动态控制权切换或临床部署安全证据。'
                a['resolution_state'] = 'reviewed_current_context_with_explicit_scope'
                a['checked_date'] = SPEC['audit_date']
                a['assessment_scope'] = '当前来源对应的机制/数据/流程事实；类别、治理和未来建议不自动升级为原文实证。'
            row['source_evidence'] = row['by_key_assessments']
            row['key_assessments'] = row['by_key_assessments']
            row['claim_context'] = citation.context
        for row in data['references']:
            relevant = [c for c in scan.citations if row['key'] in c.keys]
            row['active_citation_ids'] = [c.command_id for c in relevant]
            row['active_citation_command_ids'] = row['active_citation_ids']
            row['active_citation_lines'] = [c.line for c in relevant]
            row['active_citation_count'] = len(relevant)
        data['source_hashes'] = hashes
        data['basis'] = {'manuscript_tex_sha256':hashes['manuscript.tex'],'references_bib_sha256':hashes['references.bib']}
        data['audit_date'] = SPEC['audit_date']
        data['current_pending_summary'] = 'Only explicitly listed optional field/access limits remain; version and ten-case decisions implemented.'
        data['limitations'] = SPEC['nonblocking_limits']
        dump(evidence_path, data)
    with (project_path('literature_audit.csv')).open(encoding='utf-8-sig', newline='') as handle:
        rows = list(csv.DictReader(handle)); columns = list(rows[0])
    counts = Counter(k for c in scan.citations for k in c.keys)
    for row in rows:
        if row['key'] in entries:
            kind, fields = entries[row['key']]
            row.update(current_audit_date=SPEC['audit_date'], current_field_audit='audit_work/reference_field_audit.json#'+row['key'], cited_in_manuscript='yes' if counts[row['key']] else 'no', citation_count=str(counts[row['key']]))
            # The historical local/matched metadata columns stay historical; current values live in the field ledger.
    with (project_path('literature_audit.csv')).open('w',encoding='utf-8-sig',newline='') as handle:
        writer=csv.DictWriter(handle,fieldnames=columns);writer.writeheader();writer.writerows(rows)
    dump(WORK / 'case_classification_audit.json', {'audit_date':SPEC['audit_date'], 'rule':'Stable controller/final-decision authority => hierarchical; peer update without persistent top-down controller => flat; changing decision authority must be demonstrated for hybrid. Feedback, graph structure and voting alone are insufficient.', 'prior_proposed_labels_retained':True, 'not_blind_or_preregistered':True, 'cases':SPEC['cases'], 'agreement_count':6, 'disagreement_count':4, 'source_based_counts':dict(Counter(c['source_based_label'] for c in SPEC['cases'])), 'limits':'Purposive descriptive comparison; no source-coded hybrid case, selection accuracy or safety guarantee.'})
    dump(WORK / 'core_eligibility_audit.json', {'audit_date':SPEC['audit_date'],'criteria':'Manuscript five criteria; QA must be a substantive primary evaluation track, not necessarily the sole task.','core_count':len(core),'records':SPEC['core_eligibility'],'triad':'S by explicit author decision; single-agent/multi-role workflow; retained supporting example.'})
    actual_pdfs = json.loads((WORK / 'reference_followup_20261010.json').read_text(encoding='utf-8'))['source_pdfs']
    new_pdfs = list(actual_pdfs.values()) + SPEC['source_pdfs']
    review = {k:v for k,v in SPEC.items() if k not in ('bibliography_edits','additional_bibliography_edits','manuscript_edits')}
    review.update(stage_two_complete=False, pending_implementation=['Fresh compile, rendered spot checks and final ledger/static checks'], source_pdfs=new_pdfs, current_input_sha256=hashes, reference_field_changes=len(changes), manuscript_change_blocks=len(SPEC['manuscript_edits']), core_count=len(core), case_agreements=6, case_disagreements=4, essential_metadata_blockers=[], factual_claim_blockers=[])
    dump(WORK / 'stage2_completion_review.json', review)
    print(json.dumps({'bibliography_field_changes':len(changes),'manuscript_change_blocks':len(SPEC['manuscript_edits']),'reference_records':len(all_refs),'citation_commands':len(scan.citations),'citation_key_occurrences':sum(len(c.keys) for c in scan.citations),'core':len(core),'case_agreements':6,'pending':'compile and acceptance'},ensure_ascii=False))

if __name__ == '__main__':
    if sys.argv[1:] != ['--apply-reviewed-decisions']:
        raise SystemExit('Requires explicit --apply-reviewed-decisions; evidence generator does not approve facts.')
    apply_changes()
