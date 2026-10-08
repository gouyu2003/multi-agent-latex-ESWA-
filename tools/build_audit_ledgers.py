"""Join manually reviewed source evidence to the current active manuscript.

This writes audit files only. Evidence JSON is human/agent-reviewed input, never
a title-similarity cache. Missing evidence aborts rather than creating a false
verified row. No search is performed by this generator.
"""
from __future__ import annotations
import csv
import hashlib
import json
import zipfile
from collections import Counter
from dataclasses import asdict
from pathlib import Path

from active_tex import scan_manuscript
from build_reference_inventory import balanced_entries, parse_fields, publication_venue

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "audit_work"
FIELDS = ("author", "title", "year", "venue", "volume", "number", "pages", "doi", "url", "type")
DEGREE_ZH = {"direct": "直接支持", "partial": "部分支持/表述需收窄", "unsupported": "未支持该具体归因",
    "contradicted": "与来源相矛盾", "author_inference": "作者推论，须标明边界", "proposal": "前瞻建议，非原论文验证",
    "not_verified": "证据不足，未核实", "mixed": "多来源支持程度不同"}
FIELD_ZH = {"verified": "已核实", "confirmed_error": "已确认差异", "version_conflict": "版本/来源冲突",
    "incomplete": "字段不完整", "normalization_suggested": "建议规范化", "not_verified": "未核实",
    "not_applicable": "不适用"}
STATUS_MAP = {
    "verified_correspondence": "verified", "acceptable_representation": "verified",
    "appropriate_convention": "verified", "verified_abbreviation": "verified",
    "missing_verified_identifier": "incomplete", "missing_or_incomplete_verified_metadata": "incomplete",
    "missing_optional": "incomplete", "source_conflict": "version_conflict",
    "version_mismatch": "version_conflict", "version_confirmation_required": "version_conflict",
    "source_conflict_requires_pdf_confirmation": "version_conflict",
    "recommended_normalization": "normalization_suggested", "minor_name_difference": "normalization_suggested",
    "source_name_variant": "normalization_suggested", "minor_variant": "normalization_suggested",
    "recommended_primary_source": "normalization_suggested", "recommended_version_of_record": "normalization_suggested",
    "check_suggested": "not_verified", "partially_verified": "not_verified",
    "access_date_provenance_unverified": "not_verified",
    "needs_fix": "confirmed_error", "verified_v1_with_display_error": "confirmed_error",
}


def dump(path: Path, value) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def cell(value) -> str:
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=False)
    return str(value or "—").replace("|", "\\|").replace("\n", "<br>")


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    corrections = json.loads((WORK / "reference_correction_log.json").read_text(encoding="utf-8"))
    text_corrections = json.loads((WORK / "manuscript_correction_log.json").read_text(encoding="utf-8"))
    with zipfile.ZipFile(WORK / "before_reference_corrections_20261008.zip") as baseline:
        previous_claims = {c["command_id"]: c for c in json.loads(baseline.read("audit_work/citation_claim_audit.json"))}
    evidence_paths = sorted(WORK.glob("ledger_evidence_*.json"))
    if len(evidence_paths) != 3:
        raise ValueError("Expected three reviewed evidence batches, not automatic verification caches")
    reviewed_refs = {}
    assessments = {}
    for path in evidence_paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        bound_hashes = data.get("source_hashes", {}) or {
            "manuscript.tex": data.get("basis", {}).get("manuscript_tex_sha256"),
            "references.bib": data.get("basis", {}).get("references_bib_sha256")}
        for filename in ("manuscript.tex", "references.bib"):
            if bound_hashes.get(filename) != hashlib.sha256((ROOT / filename).read_bytes()).hexdigest():
                raise ValueError(f"Evidence batch {path.name} is not bound to the current {filename}; re-review first")
        for row in data["references"]:
            if row["key"] in reviewed_refs:
                raise ValueError(f"Duplicate reference evidence: {row['key']}")
            reviewed_refs[row["key"]] = row
        for row in data["citations"]:
            for item in row["by_key_assessments"]:
                identity = (row["command_id"], item["key"])
                if identity in assessments:
                    raise ValueError(f"Duplicate citation evidence: {identity}")
                assessments[identity] = item
    scan = scan_manuscript(ROOT)
    counts = Counter(k for c in scan.citations for k in c.keys)
    with (ROOT / "literature_audit.csv").open(encoding="utf-8-sig", newline="") as handle:
        historical = {r["key"]: r for r in csv.DictReader(handle)}
    entries = balanced_entries((ROOT / "references.bib").read_text(encoding="utf-8"))
    if set(reviewed_refs) != {key for _, key, _ in entries}:
        raise ValueError("Reviewed reference pool differs from current BibTeX pool")
    refs = []
    reference_csv = []
    for sequence, (entry_type, key, raw) in enumerate(entries, 1):
        fields = parse_fields(raw)
        current = {name: (entry_type if name == "type" else
            publication_venue(fields) if name == "venue" else fields.get(name, "")) for name in FIELDS}
        evidence = reviewed_refs[key]
        if not evidence.get("official_sources"):
            raise ValueError(f"Missing official source for {key}")
        for name in FIELDS:
            check = evidence["field_checks"][name]
            check["current"] = check.get("current") or ""
            check["original_status"] = check["status"]
            check["status"] = STATUS_MAP.get(check["status"], check["status"])
            if check["status"] not in FIELD_ZH:
                raise ValueError(f"Unknown field status for {key}:{name}: {check['status']}")
            # A checked source value must be bound to the exact current input.
            if check.get("current", "") != current[name]:
                raise ValueError(f"Stale evidence current value for {key}:{name}: {check.get('current')} != {current[name]}")
            if check["status"] == "verified" and not check.get("evidence_url"):
                raise ValueError(f"Verified field without source: {key}:{name}")
        record = dict(evidence, sequence=sequence,
            bib_line=(ROOT / "references.bib").read_text(encoding="utf-8").split(raw, 1)[0].count("\n") + 1,
            current_fields=current,
            current_record={"type": entry_type, **fields},
            active_cited=bool(counts[key]), citation_command_count=counts[key],
            evidence_role=historical.get(key, {}).get("evidence_role", "unclassified"),
            role_status="inherited author coding; not re-adjudicated; Triad eligibility pending")
        record["applied_corrections"] = [c for c in corrections if c["key"] == key]
        # Preserve every local field, including notes/publisher/version data that
        # are outside the ten-field comparison matrix. Do not hide unchecked data.
        record["additional_field_checks"] = {name: {"current": value, "status": "not_verified",
            "expected": "", "evidence_url": "", "notes": "保留完整本地字段；未在10项核心字段矩阵中逐项核实。"}
            for name, value in fields.items() if name not in FIELDS and name not in {"journal", "booktitle", "howpublished"}
            and not (name == "publisher" and entry_type == "book")}
        for name, extra in evidence.get("additional_field_checks", {}).items():
            if name not in record["additional_field_checks"]:
                continue
            extra = dict(extra)
            extra["status"] = STATUS_MAP.get(extra["status"], extra["status"])
            if extra.get("current", "") != fields[name] or extra["status"] not in FIELD_ZH:
                raise ValueError(f"Stale or unknown additional-field evidence for {key}:{name}")
            if extra["status"] == "verified" and not extra.get("evidence_url"):
                raise ValueError(f"Verified additional field without source: {key}:{name}")
            record["additional_field_checks"][name] = extra
        # Explicitly applied, source-grounded extra fields retain the same
        # before/after trail as the ten core fields. Unchecked extras stay so.
        for correction in record["applied_corrections"]:
            name = correction["field"]
            if name in record["additional_field_checks"] and correction.get("evidence_url") and correction["after"] == fields.get(name):
                record["additional_field_checks"][name].update(status="verified",
                    expected=correction["after"], evidence_url=correction["evidence_url"],
                    notes="已按所列正式来源修正；修正前值保存在 applied_corrections。")
        refs.append(record)
        row = {"sequence": sequence, "key": key, "active_cited": "yes" if counts[key] else "no",
            "bib_line": record["bib_line"], "citation_command_count": counts[key], "evidence_role_author_coded": record["evidence_role"],
            "existence_status": record["existence_status"],
            "official_sources": "\n".join(s["url"] for s in record["official_sources"])}
        for name in FIELDS:
            check = record["field_checks"][name]
            for attribute in ("current", "status", "original_status", "expected", "evidence_url", "notes"):
                row[name + "_" + attribute] = check.get(attribute, "")
        row["issues"] = json.dumps(record.get("issues", []), ensure_ascii=False)
        row["additional_field_checks"] = json.dumps(record["additional_field_checks"], ensure_ascii=False)
        row["recommendation"] = record.get("recommendation", "")
        row["applied_corrections"] = json.dumps(record["applied_corrections"], ensure_ascii=False)
        row["issue_states"] = json.dumps(record.get("issue_states", []), ensure_ascii=False)
        row["resolved_issues"] = json.dumps(record.get("resolved_issues", []), ensure_ascii=False)
        reference_csv.append(row)
    claims = []
    used_assessments = set()
    for citation in scan.citations:
        by_key = []
        for key in citation.keys:
            identity = (citation.command_id, key)
            if identity not in assessments:
                raise ValueError(f"Missing citation assessment: {identity}")
            item = assessments[identity]
            for name in ("source_evidence", "evidence_url", "locator", "support_degree", "recommendation"):
                if not item.get(name):
                    raise ValueError(f"Missing {name} for {identity}")
            if item["support_degree"] not in DEGREE_ZH:
                raise ValueError(f"Unknown support degree for {identity}")
            by_key.append(item)
            used_assessments.add(identity)
        degrees = {a["support_degree"] for a in by_key}
        record = asdict(citation)
        previous = previous_claims.get(citation.command_id, {})
        changed = previous.get("context") != citation.context or previous.get("keys") != citation.keys
        record.update(by_key_assessments=by_key,
            support_degree=next(iter(degrees)) if len(degrees) == 1 else "mixed",
            recommendation="\n".join(dict.fromkeys(a["recommendation"] for a in by_key)),
            applied=changed,
            previous_sentence=previous.get("original_sentence", ""),
            previous_keys=previous.get("keys", []),
            previous_assessments=previous.get("by_key_assessments", []),
            implementation_status="已修正相关表述，按当前句重新判断" if changed else "原表述保留，按当前证据复核")
        claims.append(record)
    if used_assessments != set(assessments):
        raise ValueError(f"Evidence contains inactive/stale citations: {set(assessments) - used_assessments}")
    dump(WORK / "reference_field_audit.json", refs)
    dump(WORK / "citation_claim_audit.json", claims)
    write_csv(WORK / "reference_field_audit.csv", reference_csv)
    write_csv(WORK / "citation_claim_audit.csv", [{
        "command_id": c["command_id"], "file": c["file"], "line": c["line"], "end_line": c["end_line"],
        "keys": ",".join(c["keys"]), "section": c["section"], "kind": c["kind"],
        "original_sentence": c["original_sentence"], "full_context": c["context"], "raw_command": c["raw_command"],
        "support_degree": c["support_degree"], "support_degree_zh": DEGREE_ZH[c["support_degree"]],
        "source_evidence": "\n".join(a["key"] + ": " + a["source_evidence"] for a in c["by_key_assessments"]),
        "evidence_location": "\n".join(a["key"] + ": " + a["locator"] for a in c["by_key_assessments"]),
        "evidence_urls": "\n".join(a["key"] + ": " + a["evidence_url"] for a in c["by_key_assessments"]),
        "per_key_support": "\n".join(a["key"] + ": " + a["support_degree"] for a in c["by_key_assessments"]),
        "recommended_change": c["recommendation"], "applied": "yes" if c["applied"] else "no",
        "implementation_status": c["implementation_status"], "previous_sentence": c["previous_sentence"],
        "previous_keys": ",".join(c["previous_keys"])} for c in claims])
    ref_md = ["# 书目字段核查台账", "", "核查日期：2026-10-08。范围：当前 references.bib 全部记录；正文未引用条目保留。",
        "", "这是修正后的当前台账；已实施修改另有 before/after 记录。存在性核实不等于所有字段均核实；每个字段单独标记。",
        "优先使用出版商、正式会议录、arXiv 对应版本和官方项目文档。网页与 PDF 不一致、版本漂移、访问限制均保留。",
        "DOI API 连接失败不作为 DOI 错误；未独立核实的 DOI 标明未核实。内部证据角色沿用作者编码，Triad 的核心纳入边界待确认。", "",
        "| 序号 | key | 正文引用次数 | 存在性 | 字段需关注 |", "|---|---|---:|---|---|"]
    for r in refs:
        checks = {**r["field_checks"], **r["additional_field_checks"]}
        attention = ", ".join(n + ":" + FIELD_ZH[f["status"]] for n, f in checks.items() if f["status"] not in {"verified", "not_applicable"})
        ref_md.append(f"| {r['sequence']} | [{r['key']}](#r{r['sequence']:03d}) | {r['citation_command_count']} | {cell(r['existence_status'])} | {cell(attention or '无')} |")
    for r in refs:
        ref_md += ["", f"<a id=\"r{r['sequence']:03d}\"></a>", f"## {r['sequence']}. {r['key']}", "",
            f"正文引用：{'有效引用' if r['active_cited'] else '未引用，保留书目池'}；引用命令数：{r['citation_command_count']}；作者编码角色：{r['evidence_role']}。", "",
            "| 字段 | 当前值 | 状态 | 来源值/建议值 | 证据与说明 |", "|---|---|---|---|---|"]
        for name in FIELDS:
            f = r["field_checks"][name]
            url = f.get("evidence_url", "")
            source = f"[来源]({url}) " if url else ""
            ref_md.append(f"| {name} | {cell(f.get('current'))} | {FIELD_ZH[f['status']]} | {cell(f.get('expected'))} | {source}{cell(f.get('notes'))} |")
        for name, f in r["additional_field_checks"].items():
            url = f.get("evidence_url", "")
            source = f"[来源]({url}) " if url else ""
            ref_md.append(f"| {name}（附加字段） | {cell(f.get('current'))} | {FIELD_ZH[f['status']]} | {cell(f.get('expected'))} | {source}{cell(f.get('notes'))} |")
        ref_md += ["", "来源记录：", ""]
        for s in r["official_sources"]:
            ref_md.append(f"- [{cell(s.get('locator', '官方来源'))}]({s['url']})：{cell(s.get('evidence', ''))}；获取范围：{cell(s.get('access_level', '未记录'))}。")
        ref_md += ["", "处理建议：" + cell(r.get("recommendation", ""))]
        if r["applied_corrections"]:
            ref_md += ["", "本轮已实施：", ""]
            for correction in r["applied_corrections"]:
                ref_md.append(f"- {correction['field']}：{cell(correction['before'])} → {cell(correction['after'])}。")
        if r.get("issues"):
            ref_md += ["", "差异记录：" + cell(r["issues"])]
        if r.get("issue_states") or r.get("resolved_issues"):
            ref_md += ["", "已关闭/待处理状态：" + cell(r.get("issue_states", [])) + cell(r.get("resolved_issues", []))]
    (WORK / "reference_field_audit.md").write_text("\n".join(ref_md).rstrip() + "\n", encoding="utf-8")
    claim_md = ["# 正文引用—来源证据台账", "", "核查日期：2026-10-08。每条记录对应一处实际有效引用命令；多键命令内部逐来源判断。",
        "排除注释、禁用条件块和未被主稿包含的历史章节。原句保留 TeX 标记；表格按完整行记录。",
        "完整段落/表格上下文在 JSON 和 CSV 的 context/full_context 中，避免只检查含引用的短句而遗漏相邻归因。",
        "多来源支持程度不同标为 mixed，不等于整句均无支持。direct 只表示所述具体内容获支持，不代表来源的所有结论均成立。",
        "获取范围以证据批次及书目台账记录为准；摘要/方法概要不能替代未读取的实验细节。已修正句按当前证据重新判断；原判断与原句另存。", "",
        "| ID | 位置 | 文献键 | 支持程度 |", "|---|---|---|---|"]
    for c in claims:
        claim_md.append(f"| [{c['command_id']}](#{c['command_id'].lower()}) | {c['file']}:{c['line']} | {cell(', '.join(c['keys']))} | {DEGREE_ZH[c['support_degree']]} |")
    for c in claims:
        claim_md += ["", f"<a id=\"{c['command_id'].lower()}\"></a>", f"## {c['command_id']} · {c['file']}:{c['line']}", "",
            "原句/表格行：", "", "> " + c["original_sentence"], "",
            "| 来源 | 证据位置 | 来源内容与支持范围 | 支持程度 |", "|---|---|---|---|"]
        for a in c["by_key_assessments"]:
            claim_md.append(f"| [{a['key']}]({a['evidence_url']}) | {cell(a['locator'])} | {cell(a['source_evidence'])} | {DEGREE_ZH[a['support_degree']]} |")
        claim_md += ["", "处理建议：", ""]
        for recommendation in dict.fromkeys(a["recommendation"] for a in c["by_key_assessments"]):
            claim_md.append("- " + recommendation)
        claim_md += ["", "实施状态：" + c["implementation_status"] + "。"]
        if c["applied"]:
            claim_md += ["", "修正前：", "", "> " + c["previous_sentence"]]
    (WORK / "citation_claim_audit.md").write_text("\n".join(claim_md).rstrip() + "\n", encoding="utf-8")
    input_paths = {f["file"] for f in scan.files} | {"references.bib", "literature_audit.csv", "search_log.csv", "audit_work/reference_correction_log.json", "audit_work/manuscript_correction_log.json", "audit_work/compile_verification.json", "audit_work/correction_baseline.json", "audit_work/correction_verification.json", "tools/active_tex.py", "tools/build_audit_ledgers.py", "tools/build_reference_inventory.py", "tools/static_reference_checks.py"} | {p.relative_to(ROOT).as_posix() for p in evidence_paths}
    protected = json.loads((WORK / "correction_baseline.json").read_text(encoding="utf-8"))
    input_paths.update(protected["figure_sha256"])
    if any(hashlib.sha256((ROOT / f).read_bytes()).hexdigest() != h for f, h in protected["figure_sha256"].items()):
        raise ValueError("An original figure changed during the reference-only correction phase")
    compilation = json.loads((WORK / "compile_verification.json").read_text(encoding="utf-8"))
    compilation_current = all(hashlib.sha256((ROOT / f).read_bytes()).hexdigest() == h for f, h in compilation["inputs_sha256"].items())
    compilation_passed = compilation_current and all(r["exit_code"] == 0 for r in compilation["runs"]) and not compilation["undefined_citation_or_reference"]
    manifest = {"audit_date": "2026-10-08", "evidence_provenance": "Prior read-only official-source audit plus explicitly recorded follow-up checks; not old title-search caches",
        "input_sha256": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in sorted(input_paths)},
        "ledger_output_sha256": {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for stem in ("reference_field_audit", "citation_claim_audit")
            for suffix in (".json", ".csv", ".md") for p in [WORK / (stem + suffix)]},
        "reference_records": len(refs), "active_cited_records": len(counts), "citation_commands": len(claims),
        "citation_key_assessments": len(used_assessments), "unused_pool_keys": [r["key"] for r in refs if not r["active_cited"]],
        "pool_roles_author_coded": dict(Counter(r["evidence_role"] for r in refs)),
        "active_roles_author_coded": dict(Counter(r["evidence_role"] for r in refs if r["active_cited"])),
        "per_key_support_degrees": dict(Counter(a["support_degree"] for c in claims for a in c["by_key_assessments"])),
        "command_support_degrees": dict(Counter(c["support_degree"] for c in claims)),
        "field_status_counts": dict(Counter(f["status"] for r in refs for f in r["field_checks"].values())),
        "additional_field_status_counts": dict(Counter(f["status"] for r in refs for f in r["additional_field_checks"].values())),
        "manuscript_modified": True, "bibliography_modified": True, "figures_modified": False, "corrections_applied": True,
        "applied_bib_field_changes": len(corrections), "applied_text_change_blocks": len(text_corrections),
        "citation_commands_with_updated_context": sum(c["applied"] for c in claims),
        "compilation_current": compilation_current, "compilation_passed": compilation_passed,
        "limits": ["Not a full TeX interpreter; unsupported conditionals/dynamic inputs fail closed",
            "Fresh pdflatex/BibTeX compilation compared to current active sources; layout warnings retained for formatting phase",
            "Source access and field-level uncertainty recorded; no blanket all-field verification claim",
            "Core study eligibility remains inherited author coding; Triad requires author decision",
            "Figure counts retain earlier 84-record snapshot; current pool85/active78/core coding14; update deferred to figure phase"]}
    write_pending(manifest, refs, claims)
    for suffix in (".json", ".csv", ".md"):
        path = WORK / ("pending_reference_decisions" + suffix)
        manifest["ledger_output_sha256"][path.relative_to(ROOT).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    dump(WORK / "ledger_manifest.json", manifest)
    dump(WORK / "final_audit_summary.json", {"supersedes": "historical 75-record summary", **manifest})
    write_report(manifest, refs, claims)
    print(json.dumps({k: manifest[k] for k in ("reference_records", "active_cited_records", "citation_commands", "citation_key_assessments", "command_support_degrees", "field_status_counts")}, ensure_ascii=False, indent=2))


def write_report(manifest: dict, refs: list[dict], claims: list[dict]) -> None:
    n = manifest["reference_records"]
    c = manifest["citation_commands"]
    lines = ["# 参考文献修正与验收报告", "", "日期：2026-10-08。已应用有来源依据的书目字段修正和正文最小修正，保留导师修改后的章节结构及原有 citation keys；图片留待下一阶段。", "",
        "## 当前统计", "", "| 口径 | 数量 |", "|---|---:|",
        f"| 书目池 | {n} |", f"| 有效正文不同文献 | {manifest['active_cited_records']} |",
        f"| 有效引用命令 | {c} |", f"| 展开多键后的出现次数 | {manifest['citation_key_assessments']} |",
        f"| 保留的未引用记录 | {len(manifest['unused_pool_keys'])} |", "",
        "原有84条全部保留。新增1条有日期的官方 LangGraph interrupt 技术文章，用于暂停、检查点和恢复机制；不是补足文献数量。",
        "书目池角色：" + json.dumps(manifest["pool_roles_author_coded"], ensure_ascii=False) + "；有效引用角色：" + json.dumps(manifest["active_roles_author_coded"], ensure_ascii=False) + "。",
        "14项I沿用作者编码；Triad的一个LLM承担三角色已在方法和表格中披露为纳入边界，是否转为S仍待作者裁定。", "",
        "## 已完成修改", "",
        "- 修正 Natural Questions 页码、ReAct及NeurIPS会议条目类型、GLM集体署名、MemGPT姓名显示、SWE-agent错误URL、CrewAI首次PyPI发布日期；补充已核实的会议DOI。",
        "- Guo综述使用IJCAI2024正式出处，GPTSwarm使用ICML/PMLR正式出处；Least-to-Most、Decomposed Prompting、Self-Consistency使用ICLR2023正式出处。仍存在来源冲突的作者字段没有自动覆盖。",
        "- 收窄综述新颖性定位；修正MemGPT、Self-RAG/FLARE、ToT/GoT、CoVe、AgentVerse/MetaGPT及GPTSwarm等机制归因。区分CoCoA-zero多代理推理与CoCoA单模型蒸馏。",
        "- 将架构适用性、成本收益准则、治理要求和部分评估建议标为作者综合或建议；修复两处失效交叉引用，保留AI使用披露。",
        "- 正文与literature_audit.csv同步当前统计，历史排除记录保留；搜索历史与本次字段核查分别记录。",
        f"书目修改日志含{manifest['applied_bib_field_changes']}项字段/新增记录操作；正文有{manifest['applied_text_change_blocks']}个差异块。日志包含修正前后内容，不能把一个差异块视为一个独立科学结论。", "",
        "完整记录：[书目before/after](audit_work/reference_correction_log.json)、[正文before/after](audit_work/manuscript_correction_log.json)、[修改前快照](audit_work/before_reference_corrections_20261008.zip)。", "",
        "## 当前证据台账", "",
        f"- [{n}条书目字段台账](audit_work/reference_field_audit.md)：[CSV](audit_work/reference_field_audit.csv)、[JSON](audit_work/reference_field_audit.json)。逐字段标明已核实、冲突、未核实等，原差异与已修正项保留历史。",
        f"- [{c}处正文引用证据台账](audit_work/citation_claim_audit.md)：[CSV](audit_work/citation_claim_audit.csv)、[JSON](audit_work/citation_claim_audit.json)。当前原句、证据位置、支持程度、实施状态及修改前句分别记录，多键命令逐来源判断。", "",
        "10项核心字段状态：", "", "| 状态 | 字段数 |", "|---|---:|"]
    lines += [f"| {FIELD_ZH.get(k,k)} | {v} |" for k,v in manifest["field_status_counts"].items()]
    lines += ["", "引用命令状态：", "", "| 支持程度 | 命令数 |", "|---|---:|"]
    lines += [f"| {DEGREE_ZH[k]} | {v} |" for k,v in manifest["command_support_degrees"].items()]
    lines += ["", "作者推论或前瞻建议不自动视为错误，也不升级为原论文已验证结论。存在性核实不等于所有字段核实；未获取正式全文的字段保持限制说明。", "",
        "## 编译及一致性验收", "",
        f"当前编译快照有效：{manifest['compilation_current']}；编译和引用解析通过：{manifest['compilation_passed']}。",
        "[编译记录](audit_work/compile_verification.json)保存命令、退出码、未定义引用检查、版面警告和输入/输出哈希。过长URL与原有版面警告留待格式阶段，不据此声称最终排版已验收。",
        "[当前清单](audit_work/inventory_summary.json)对照实际主稿、.aux及.bbl；[静态检查](audit_work/static_reference_checks.json)检查覆盖、定位和哈希，warnings为待确认项，不等同于结构检查失败。",
        "禁用条件块、未被主稿包含的历史章节和19个原图片文件保持不变；保护检查见[correction_verification.json](audit_work/correction_verification.json)。", "",
        "复现台账检查：", "", "```powershell", "python -m unittest discover -s tools -p test_active_tex.py -v", "python tools/build_reference_inventory.py", "python tools/build_audit_ledgers.py", "python tools/static_reference_checks.py", "```", "",
        "证据生成器不联网，也不自动证明来源；来源变化后需要重新审阅，禁止仅改哈希绕过。旧finalize工具入口已停用，防止过时缓存删掉未引记录。", "",
        "## 待确认及图片阶段", "",
        "[待确认清单](audit_work/pending_reference_decisions.md)汇总Triad、版本选择、官方网页/PDF冲突及未直接核实字段；[CSV](audit_work/pending_reference_decisions.csv)逐字段保留。",
        "图片仍有84 active或旧角色分配等口径。正文已注明旧快照；下一阶段需同步为书目池85、有效引用78、作者编码I14（Triad待裁定），并缩小图中文字。本轮未改图。",
        "以下7条保留，不为凑数补引：", ""]
    lines += ["- `"+k+"`" for k in manifest["unused_pool_keys"]]
    lines += ["", "[旧报告归档](audit_work/reference_audit_report_legacy_20260802.md)保留历史75条结论。literature_audit.csv的引用标志和次数已同步，旧元数据匹配列仍属历史证据，当前字段结论以两份台账为准。", ""]
    (ROOT / "reference_audit_report.md").write_text("\n".join(lines).rstrip()+"\n", encoding="utf-8")


def write_pending(manifest: dict, refs: list[dict], claims: list[dict]) -> None:
    rows = []
    for r in refs:
        for field, f in {**r["field_checks"], **r["additional_field_checks"]}.items():
            if f["status"] in {"verified", "not_applicable"}:
                continue
            rows.append({"key":r["key"],"field":field,"status":f["status"],"current":f.get("current", ""),
                "source_or_expected":f.get("expected", ""),"evidence_url":f.get("evidence_url", ""),
                "detail":f.get("notes", ""),"action":"确认具体版本/来源后再修改" if f["status"] == "version_conflict" else "获取字段级正式来源后确认；不凭题名相似度补全"})
    write_csv(WORK / "pending_reference_decisions.csv", rows)
    dump(WORK / "pending_reference_decisions.json", {"unresolved_metadata_fields":rows,
        "citation_rows_with_evidence_boundary":[{"command_id":c["command_id"], "support_degree":c["support_degree"], "recommendation":c["recommendation"]} for c in claims if c["support_degree"] != "direct"]})
    lines = ["# 参考文献与证据边界待确认清单", "", "日期：2026-10-08。确定错误已修正；以下不确定项保留，不自动替作者选择版本或调整纳入范围。", "",
        "| 项目 | 当前处理 | 后续具体步骤 |", "|---|---|---|",
        "| Triad纳入标准 | 保留I编码及十案例比较，正文披露一个LLM三角色 | 由作者裁定独立多代理标准。若严格要求≥2独立代理，改为S并重算I/S和图中数量；是否保留十案例诊断另行说明。 |",
        "| 书籍/预印本版本 | 保留当前Minsky版次、GPT-4/MemGPT/ChatLaw等版本冲突 | 固定实际使用的版次或arXiv vN；核对该版本作者、年份及链接后一致更新。citation key无需改名。 |",
        "| 网页与PDF作者冲突 | GAIA、DSPy、Self-RAG、LegalBench等不盲改姓名 | 取得正式PDF首页，与官方HTML/版本历史逐项核对，记录冲突与采用理由。 |",
        "| 未直接核实的出版字段 | LLM-MedQA、Financial Reflection QA、SWE-agent等部分页码或DOI保留未核实状态 | 以本条出版商元数据或论文PDF核实；另一论文的参考文献仅作间接线索。 |",
        "| 软件与协议版本 | Dify/RAGFlow/CrewAI、MCP/A2A等保留历史版本限制 | 若论述特定年份能力，固定release/tag/commit或当时文档；当前文档只支持当前能力。 |",
        "| 历史检索过程 | 108候选、四异常等写为历史日志记录 | 若需方法复现，补原始检索导出和筛选记录；本次核查不替代当年的实际检索凭证。 |",
        "| 图片同步 | 原图未修改，图注已标历史快照 | 统一pool85、active78及I14边界说明；核对所有图内84 active、旧角色数量和CoCoA等标签，再缩小字体导出。 |",
        "| AI绘图来源 | 保留AI使用披露，去掉不存在的图引用 | 图片阶段确认Nano Banana所对应的实际采用图及编辑来源，若未采用则准确说明。 |", "",
        f"逐字段未决记录共{len(rows)}项（含非必填附加字段，不等于{len(rows)}篇文献有错误）；完整值、状态与证据见[CSV](pending_reference_decisions.csv)。", "",
        "## 版本/来源冲突的具体字段", "", "| key | 字段 | 当前值 | 来源值/冲突 |", "|---|---|---|---|"]
    lines += [f"| {cell(r['key'])} | {cell(r['field'])} | {cell(r['current'])} | {cell(r['source_or_expected'])} |" for r in rows if r["status"] == "version_conflict"]
    lines += ["", "## 未核实字段按记录列出", "", "| key | 未决字段及状态 |", "|---|---|"]
    for r in refs:
        fields = [f["field"]+":"+FIELD_ZH[f["status"]] for f in rows if f["key"] == r["key"]]
        if fields:
            lines.append(f"| {r['key']} | {cell(', '.join(fields))} |")
    lines += ["", "## 正文证据边界", "", "当前台账对作者综合、前瞻建议和来源获取限制继续单独标记。对于未修正且证据仍不足的具体断言，须取得原文证据或进一步收窄；不得因结构检查通过而标成已验证。", "",
        "| 引用ID | 当前支持程度 | 后续/保留理由 |", "|---|---|---|"]
    lines += [f"| {c['command_id']} | {DEGREE_ZH[c['support_degree']]} | {cell(c['recommendation'])} |" for c in claims if c["support_degree"] != "direct"]
    (WORK / "pending_reference_decisions.md").write_text("\n".join(lines).rstrip()+"\n", encoding="utf-8")


if __name__ == "__main__":
    main()
