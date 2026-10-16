"""Compile and check the authorized reference revision against its saved baseline.

Scientific decisions are manually reviewed inputs; these checks do not approve facts.
"""
from __future__ import annotations
from project_paths import project_path
import copy
import csv
import hashlib
import io
import json
import re
import subprocess
import sys
import time
import zipfile
from collections import Counter
from pathlib import Path
from dataclasses import asdict
from active_tex import scan_manuscript
from build_reference_inventory import balanced_entries, parse_fields

ROOT = Path(__file__).resolve().parents[1]
WORK = project_path('audit_work')
BASE = json.loads((WORK / 'stage2_completion_baseline.json').read_text(encoding='utf-8'))

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def dump(p, value):
    Path(p).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def repair_review_history():
    """Restore exact previous assessments and unchanged verified extras from backup."""
    with zipfile.ZipFile(project_path('audits/revisions/backups/before_stage2_completion_20261010.zip')) as z:
        for p in sorted(WORK.glob('ledger_evidence_*.json')):
            old = json.loads(z.read(p.relative_to(ROOT).as_posix()))
            data = json.loads(p.read_text(encoding='utf-8'))
            previous = {r['key']: r for r in old['references']}
            for row in data['references']:
                for name, check in row.get('additional_field_checks', {}).items():
                    prior = previous[row['key']].get('additional_field_checks', {}).get(name, {})
                    if check['status']=='not_verified' and prior.get('current')==check['current'] and prior.get('status') in ('verified','verified_correspondence','acceptable_representation','appropriate_convention','verified_abbreviation'):
                        row['additional_field_checks'][name] = copy.deepcopy(prior)
                if row['key'] in ('langgraph2024','xagent2023'):
                    url = 'https://www.langchain.com/blog/langgraph-multi-agent-workflows' if row['key']=='langgraph2024' else 'https://github.com/OpenBMB/XAgent'
                    check = row['field_checks']['venue']
                    check.update(status='verified',expected=check['current'],evidence_url=url,
                        notes='官方博客/仓库身份和归属已核；howpublished是该技术资源的可接受载体表示，非正式学术会议。')
                row['issue_states'] = [{'field':n,'state':'pending_optional_field','resolution':c.get('notes','')} for n,c in {**row['field_checks'],**row.get('additional_field_checks',{})}.items() if c['status'] not in ('verified','not_applicable','appropriate_convention','acceptable_representation','verified_correspondence','verified_abbreviation')]
            prior_citations = {r['command_id']:r for r in old['citations']}
            for row in data['citations']:
                prior = prior_citations[row['command_id']]
                row['stage2_prior_context']={'original_sentence':prior.get('original_sentence'),'context':prior.get('context'),'line':prior.get('line'),'assessments':copy.deepcopy(prior['by_key_assessments'])}
            dump(p,data)

def compile_current():
    latex = r'D:\texlive\2026\bin\windows\pdflatex.exe'
    bibtex = r'D:\texlive\2026\bin\windows\bibtex.exe'
    common = [latex,'-interaction=nonstopmode','-halt-on-error','-no-shell-escape','-synctex=1','manuscript.tex']
    runs=[]
    for step,command in [('latex_first',common),('bibtex',[bibtex,'manuscript']),('latex_second',common),('latex_final',common)]:
        start=time.monotonic()
        result=subprocess.run(command,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        out=WORK / ('compile_stage2_20261010_'+step+'.txt')
        out.write_bytes(result.stdout)
        runs.append({'step':step,'command':command,'exit_code':result.returncode,'output_file':out.relative_to(ROOT).as_posix(),'elapsed_seconds':round(time.monotonic()-start,2)})
        print(step,result.returncode,flush=True)
        if result.returncode:
            print(result.stdout.decode('utf-8',errors='replace')[-10000:])
            raise SystemExit(result.returncode)
    log=(project_path('manuscript.log')).read_text(encoding='utf-8',errors='replace')
    bib=(project_path('manuscript.blg')).read_text(encoding='utf-8',errors='replace')
    report={'audit_date':'2026-10-10','revision':'Stage-two completion; authorized bibliography and necessary prose edits',
        'runs':runs,'undefined_citation_or_reference':[l for l in log.splitlines() if re.search(r'(Citation|Reference).*undefined|There were undefined',l)],
        'overfull_boxes':[l for l in log.splitlines() if l.startswith('Overfull')],
        'underfull_box_count':len(re.findall('Underfull',log)),
        'bibtex_warnings':[l for l in bib.splitlines() if l.startswith('Warning--')],
        'output':[l for l in log.splitlines() if l.startswith('Output written')],
        'inputs_sha256':{n:sha(project_path(n)) for n in ['manuscript.tex','references.bib','manuscript.aux','manuscript.bbl','manuscript.pdf','manuscript.synctex.gz']},
        'visual_review':{'status':'pending','scope':'Updated content/table/bibliography spots; complete formatting belongs to later stage.'}}
    dump(WORK/'compile_verification.json',report)
    print(json.dumps({k:report[k] for k in ['output','undefined_citation_or_reference','bibtex_warnings','overfull_boxes']},ensure_ascii=False))

def check_protection():
    with zipfile.ZipFile(project_path('audits/revisions/backups/before_stage2_completion_20261010.zip')) as z:
        old_text=z.read('manuscript.tex'); current=(project_path('manuscript.tex')).read_bytes()
        old_bib={k for _,k,_ in balanced_entries(z.read('references.bib').decode('utf-8'))}
        old_csv=list(csv.DictReader(io.StringIO(z.read('literature_audit.csv').decode('utf-8-sig'))))
    with (project_path('literature_audit.csv')).open(encoding='utf-8-sig',newline='') as h:
        current_csv={r['key']:r for r in csv.DictReader(h)}
    figures=json.loads((WORK/'correction_baseline.json').read_text(encoding='utf-8'))['figure_sha256']
    historical={n:h for n,h in BASE['files'].items() if re.fullmatch(r'ch\d+_en\.tex',n)}
    keys={k for _,k,_ in balanced_entries((project_path('references.bib')).read_text(encoding='utf-8'))}
    scan=scan_manuscript(ROOT)
    roles={r['key']:r['evidence_role'] for r in current_csv.values()}
    cited={k for c in scan.citations for k in c.keys}
    checks={'bibliography_pool_keys_preserved':keys==old_bib,
        'inactive_block_byte_identical':re.findall(rb'\\iffalse\b.*?\\fi\b',old_text,re.S)==re.findall(rb'\\iffalse\b.*?\\fi\b',current,re.S),
        'section_headings_unchanged':re.findall(rb'\\section\{[^}]+\}',old_text)==re.findall(rb'\\section\{[^}]+\}',current),
        'historically_excluded_csv_rows_preserved':all(current_csv.get(r['key'])==r for r in old_csv if r['evidence_role']=='X'),
        'figure_source_data_byte_identical':sha(project_path('figure_source_data.csv'))==BASE['files']['figure_source_data.csv'],
        'historical_tex_files_unchanged':all(sha(project_path(n))==h for n,h in historical.items()),
        'source_pdfs_sha256_unchanged':all(sha(Path(n))==h for n,h in BASE['source_pdf_sha256'].items()),
        'original_figures_unchanged':all(sha(project_path(n))==h for n,h in figures.items()),
        'active_citation_count_preserved':len(scan.citations)==136 and len(cited)==78 and sum(len(c.keys) for c in scan.citations)==180,
        'triad_is_supporting':roles['hu2024triad']=='S'}
    report={'audit_date':'2026-10-10','stage2_baseline':'audit_work/stage2_completion_baseline.json','checks':checks,**checks,
        'figure_files_checked':len(figures),'historical_tex_files_checked':len(historical),'source_pdfs_checked':len(BASE['source_pdf_sha256']),
        'bibliography_modified_as_authorized':sha(project_path('references.bib'))!=BASE['files']['references.bib'],
        'bibliography_byte_identical_to_followup_baseline':False,
        'bibliography_pool_roles':dict(Counter(roles[k] for k in keys)),'active_citation_roles':dict(Counter(roles[k] for k in cited)),
        'checks_passed':all(checks.values())}
    dump(WORK/'correction_verification.json',report)
    print(json.dumps(report,ensure_ascii=False,indent=2))
    if not report['checks_passed']: raise SystemExit(1)

def mark_complete():
    report=json.loads((WORK/'compile_verification.json').read_text(encoding='utf-8'))
    protection=json.loads((WORK/'correction_verification.json').read_text(encoding='utf-8'))
    static=json.loads((WORK/'static_reference_checks.json').read_text(encoding='utf-8'))
    review=json.loads((WORK/'stage2_completion_review.json').read_text(encoding='utf-8'))
    if not (protection['checks_passed'] and static['checks_passed'] and all(r['exit_code']==0 for r in report['runs']) and not report['undefined_citation_or_reference'] and report['visual_review']['status']=='reviewed'):
        raise ValueError('Compile, visual, protection and static checks must pass first')
    if any(sha(project_path(p))!=h for p,h in report['inputs_sha256'].items()):raise ValueError('Stale compile')
    refs=json.loads((WORK/'reference_field_audit.json').read_text(encoding='utf-8'))
    claims=json.loads((WORK/'citation_claim_audit.json').read_text(encoding='utf-8'))
    essential=[(r['key'],n) for r in refs for n in ['author','title','year','venue','type'] if r['field_checks'][n]['status'] not in ['verified','not_applicable']]
    factual=[(c['command_id'],a['key'],a['support_degree']) for c in claims for a in c['by_key_assessments'] if a['support_degree'] in ['partial','unsupported','contradicted','not_verified']]
    if essential or factual:raise ValueError(f'Review blockers: {essential}; {factual}')
    cases=json.loads((WORK/'case_classification_audit.json').read_text(encoding='utf-8'))
    core=json.loads((WORK/'core_eligibility_audit.json').read_text(encoding='utf-8'))
    if sum(c['match']=='agreement' for c in cases['cases'])!=6 or sum(c['match']=='disagreement' for c in cases['cases'])!=4:raise ValueError('Case count mismatch')
    if len(core['records'])!=13 or any(not all(r['criteria'].values()) for r in core['records']):raise ValueError('Core review incomplete')
    review.update(stage_two_complete=True,pending_implementation=[],essential_metadata_blockers=[],factual_claim_blockers=[],
        final_acceptance={'compile_passed':True,'protected_material_unchanged':True,'rendered_content_spots_reviewed':True,'static_structure_passed':True,
            'field_limits_preserved':True,'not_blanket_verification':True,'later_stages':['Formatting','Original figure statistics/labels/font reduction']})
    dump(WORK/'stage2_completion_review.json',review)
    print('Stage-two review complete. Regenerate ledger snapshot and run static checks to bind the final decision.')

if __name__=='__main__':
    operations={'--repair-history':repair_review_history,'--compile':compile_current,'--protect':check_protection,'--mark-complete':mark_complete}
    if len(sys.argv)!=2 or sys.argv[1] not in operations:raise SystemExit('Select one explicit stage verification operation')
    operations[sys.argv[1]]()
