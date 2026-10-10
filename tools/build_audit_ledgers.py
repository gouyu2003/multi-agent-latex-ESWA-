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
FOLLOWUP_PATH = WORK / "reference_followup_20261010.json"
FOLLOWUP = json.loads(FOLLOWUP_PATH.read_text(encoding="utf-8"))
REVIEW_PATH = WORK / "stage2_completion_review.json"
REVIEW = json.loads(REVIEW_PATH.read_text(encoding="utf-8"))
CORE = json.loads((WORK / "core_eligibility_audit.json").read_text(encoding="utf-8"))
CASES = json.loads((WORK / "case_classification_audit.json").read_text(encoding="utf-8"))
AUDIT_DATE = REVIEW["audit_date"]
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
    corrections = json.loads((WORK / "reference_correction_log.json").read_text(encoding="utf-8")) + json.loads((WORK / "stage2_reference_correction_log.json").read_text(encoding="utf-8"))
    text_corrections = json.loads((WORK / "manuscript_correction_log.json").read_text(encoding="utf-8")) + json.loads((WORK / "stage2_manuscript_correction_log.json").read_text(encoding="utf-8"))
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
    if FOLLOWUP:
        decision = FOLLOWUP["triad_decision"]
        if historical[decision["key"]]["evidence_role"] != decision["current_role"]:
            raise ValueError("Triad role differs from the recorded author decision")
        for source in FOLLOWUP["source_pdfs"].values():
            if hashlib.sha256(Path(source["path"]).read_bytes()).hexdigest() != source["sha256"]:
                raise ValueError(f"Reviewed source PDF changed: {source['path']}")
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
            role_status=("Triad S confirmed by author on 2026-10-10; supporting boundary example" if key == "hu2024triad" else
                "Core I eligibility re-adjudicated against five criteria and full methods/evaluation; see core_eligibility_audit.json" if key in {r['key'] for r in CORE['records']} else
                "Supporting/background/technical role retained; not counted as core study"))
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
    ref_md = ["# 书目字段核查台账", "", f"截至：{AUDIT_DATE}。第二阶段当前修正版：此前核查加五篇用户提供的正式PDF、官方全文、版本记录及出版商登记信息。范围：当前 references.bib 全部记录；正文未引用条目保留。",
        "", "这是修正后的当前台账；已实施修改另有 before/after 记录。存在性核实不等于所有字段均核实；每个字段单独标记。",
        "优先使用出版商、正式会议录、arXiv 对应版本和官方项目文档。网页与 PDF 不一致、版本漂移、访问限制均保留。",
        "DOI API连接失败不作为DOI错误；未独立核实的字段标明未核实。Triad经作者确认改为S；13项核心研究已按五项标准重核，见core_eligibility_audit.md。", "",
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
    claim_md = ["# 正文引用—来源证据台账", "", f"截至：{AUDIT_DATE}。第二阶段当前修正版；五篇正式PDF及新增官方全文补证、版本固定、十案例统一编码和必要正文修正已纳入。每条记录对应一处实际有效引用命令；多键命令内部逐来源判断。",
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
    if FOLLOWUP:
        input_paths.add(FOLLOWUP_PATH.relative_to(ROOT).as_posix())
        input_paths.add("Highlights.txt")
        input_paths.update(source["path"] for source in FOLLOWUP["source_pdfs"].values())
    input_paths.update({"audit_work/stage2_completion_review.json", "audit_work/stage2_completion_review_spec.json", "audit_work/stage2_completion_baseline.json", "audit_work/stage2_reference_correction_log.json", "audit_work/stage2_manuscript_correction_log.json", "audit_work/case_classification_audit.json", "audit_work/core_eligibility_audit.json", "tools/complete_stage2_review.py", "tools/verify_stage2_completion.py"})
    input_paths.update(p.relative_to(ROOT).as_posix() for p in (WORK / "stage2_sources").iterdir() if p.is_file())
    input_paths.update(p.relative_to(ROOT).as_posix() for p in WORK.glob("stage2*source*retrieval.json"))
    input_paths.update(source["path"] for source in REVIEW["source_pdfs"])
    protected = json.loads((WORK / "correction_baseline.json").read_text(encoding="utf-8"))
    input_paths.update(protected["figure_sha256"])
    if any(hashlib.sha256((ROOT / f).read_bytes()).hexdigest() != h for f, h in protected["figure_sha256"].items()):
        raise ValueError("An original figure changed during the reference-only correction phase")
    compilation = json.loads((WORK / "compile_verification.json").read_text(encoding="utf-8"))
    compilation_current = all(hashlib.sha256((ROOT / f).read_bytes()).hexdigest() == h for f, h in compilation["inputs_sha256"].items())
    compilation_passed = compilation_current and all(r["exit_code"] == 0 for r in compilation["runs"]) and not compilation["undefined_citation_or_reference"]
    manifest = {"audit_date": AUDIT_DATE, "evidence_provenance": "Prior official-source context review plus five formal source PDFs, official full texts, publisher records and dated/versioned resources; each field/context assessed separately",
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
        "stage2_bib_field_changes": REVIEW["reference_field_changes"], "stage2_text_change_blocks": REVIEW["manuscript_change_blocks"],
        "core_eligibility_review_count": CORE["core_count"], "case_agreements": CASES["agreement_count"], "case_disagreements": CASES["disagreement_count"],
        "stage_two_complete": bool(REVIEW["stage_two_complete"] and compilation_passed),
        "citation_commands_with_updated_context": sum(c["applied"] for c in claims),
        "compilation_current": compilation_current, "compilation_passed": compilation_passed,
        "limits": ["Not a full TeX interpreter; unsupported conditionals/dynamic inputs fail closed",
            "Fresh pdflatex/BibTeX compilation compared to current active sources; layout warnings retained for formatting phase",
            "Source access and field-level uncertainty recorded; no blanket all-field verification claim",
            "Triad is S by author decision; ten-case control-authority coding is retrospective, not blind or prospective validation",
            "Figure counts retain earlier 84-record snapshot; current pool85/active78/core coding13; update deferred to figure phase"],
        "followup": {"decision_record": "audit_work/reference_followup_20261010.json", "triad": FOLLOWUP.get("triad_decision"),
            "source_pdfs_reviewed": len(REVIEW["source_pdfs"]), "bibliography_modified_in_followup": True,
            "stage_two_complete": bool(REVIEW["stage_two_complete"] and compilation_passed)}}
    write_pending(manifest, refs, claims)
    for suffix in (".json", ".csv", ".md"):
        path = WORK / ("pending_reference_decisions" + suffix)
        manifest["ledger_output_sha256"][path.relative_to(ROOT).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    dump(WORK / "ledger_manifest.json", manifest)
    dump(WORK / "final_audit_summary.json", {"supersedes": "historical 75-record summary", **manifest})
    write_report(manifest, refs, claims)
    print(json.dumps({k: manifest[k] for k in ("reference_records", "active_cited_records", "citation_commands", "citation_key_assessments", "command_support_degrees", "field_status_counts")}, ensure_ascii=False, indent=2))


def write_report(manifest: dict, refs: list[dict], claims: list[dict]) -> None:
    complete = manifest["stage_two_complete"]
    lines = ["# 第二阶段参考文献与正文证据审计报告", "", f"核查日期：{AUDIT_DATE}。唯一基线：ESWA_Submission_caomodify。",
        "", "## 当前结论", "",
        ("第二阶段已完成：书目版本及必要字段修正、有效正文引用相关性、13项核心纳入标准、十案例统一分类及匹配修正均已落实；新稿已编译并通过保护与结构验收。" if complete else "科学内容修正及台账更新已落实；编译、渲染或最终验收尚未全部完成，暂不标记第二阶段完成。"),
        "这里的完成不代表所有可选字段均得到证明：缺乏正式证据的DOI、页码、出版者等仍逐字段标为未核实；不据篇幅编造出版页码，不将作者分析改标为原文实证。", "",
        "## 核查覆盖", "",
        "| 项目 | 当前结果 |", "|---|---|",
        f"| 书目池 | {manifest['reference_records']}条；全部逐字段记录 |",
        f"| 有效引用 | {manifest['active_cited_records']}篇；{manifest['citation_commands']}处引用命令；{manifest['citation_key_assessments']}个逐来源判断 |",
        f"| 池内角色 | {cell(manifest['pool_roles_author_coded'])} |",
        f"| 有效引用角色 | {cell(manifest['active_roles_author_coded'])} |",
        f"| 核心纳入重核 | {manifest['core_eligibility_review_count']}项；五项标准均有方法/评估证据定位 |",
        f"| 本次实施 | {manifest['stage2_bib_field_changes']}项书目字段修改；{manifest['stage2_text_change_blocks']}处正文差异块 |",
        f"| 引用判断 | {cell(manifest['command_support_degrees'])} |",
        f"| 十案例 | {manifest['case_agreements']}例一致；{manifest['case_disagreements']}例不一致；来源流程编码为9层级、1扁平、0混合 |", "",
        "未引用的7条记录保留在书目池，未为凑数补引。I是核心研究、S是支持研究、B是背景、T是技术资源；Triad按作者明确决定为S。", "",
        "## 已落实的主要修改", "",
        "- AutoGen使用用户提供的COLM 2024正式全文，核对14位作者、正式题名及GroupChatManager等机制位置；没有把46页篇幅填成正式出版页码。",
        "- GPT-4、MemGPT、ChatLaw、AgentCoder固定实际使用的arXiv版本。AgentCoder按2023 v1的五位作者及顺序修正；该版本测试执行角色为脚本，正文不把它算作第三个LLM智能体。",
        "- DSPy题名/作者以正式全文为依据；GAIA补回Craig Swift；Self-RAG使用官方Zeqiu拼写及正式全文Avirup全名；LegalBench以正式全文作者列为依据，保留网页差异历史。",
        "- Natural Questions采用正式PDF和出版商登记一致的453–466；ACL网页452–466差异保留。LLM-MedQA的1–8获出版商登记支持；Memory survey按Article155写为155:1–155:47；EduPlanner题名按Multiagent规范。",
        "- 仅据正式来源补入可确认的ICLR/NeurIPS连续页码与DOI。未获证明的字段维持未核实；可访问的摘要不替代未读的实验内容。",
        "- CrewAI固定0.1.0、Dify固定0.6.0、RAGFlow固定v0.6.0；MCP采用2024-11-25公告、A2A采用2025-04-09公告；不以当前功能倒推早期版本。",
        "- 十案例保留既有建议架构，按统一控制权标准重新编码来源流程。MedAgents、LLM-MedQA、LegalGraphRAG、EduPlanner改判为层级，得到六例一致、四例不一致；不作为选择策略预测准确率。",
        "- CAMEL角色对、AutoGen可配置会话、GPTSwarm图结构、AgentVerse反馈、LangGraph状态图不再机械等同扁平或混合。区分控制权架构与可复用机制。",
        "- Financial QA收窄为critic feedback and answer revision；其多轮反复辩论是未来工作。撤去必须全局知识图谱、实时同步及保证避免重复检索等缺少依据的强断言。", "",
        "## 按有效章节定位", "",
        "| 章节 | 本次相关修正 |", "|---|---|",
        "| 第1章 Introduction及文献筛选说明 | 历史检索描述收窄为工作记录，85/78与核心13口径同步；绝对性领域知识/增长断言收窄 |",
        "| 第2章 Background | 跨reasoner答案比较与普遍优于自我修正分开；已核机制归因保持来源边界 |",
        "| 第3章 Architectures | 控制权分类、交叉机制表、十案例编码/勾叉、人工审批及混合判断规则修正 |",
        "| 第4章 Key technologies | 按选定版本核实MemGPT/Self-RAG/FLARE/ToT/GoT/CoVe；知识共享与自省效果不作无条件保证 |",
        "| 第5章 Development and evaluation resources | 框架表按实际机制命名，固定软件/协议版本，不扩展为自动架构选择或部署验证 |",
        "| 第6章 Challenges and Future Directions | Financial QA反馈修订机制收窄；建议和来源实测效果明确区分 |",
        "| 第7章 Conclusion及末尾声明 | 六/四回顾性比较、无来源编码混合样本、非独立验证局限及版本选择同步 |", "",
        "导师隐藏的旧应用章/旧完整选择章及独立历史章节文件继续保留，不参与此次有效正文核查。完整逐处before/after见[正文修改日志](audit_work/stage2_manuscript_correction_log.json)；逐字段见[书目修改日志](audit_work/stage2_reference_correction_log.json)。", "",
        "## 核心证据与限制", "",
        "[书目字段台账](audit_work/reference_field_audit.md)覆盖全部85条及附加字段；[正文证据台账](audit_work/citation_claim_audit.md)覆盖全部136处有效引用及180个逐来源语境。",
        "[核心纳入重核](audit_work/core_eligibility_audit.md)记录13项五标准证据；[十案例复核](audit_work/case_classification_audit.md)记录来源流程、编码和匹配。",
        "来源优先正式全文、出版社/会议官方页、出版商登记、选定arXiv版本及官方日期/发行记录；同一机构的HTML和PDF属于主来源的不同载体，不冒充独立双源。检索失败、页面访问限制和版本差异保留在快照/检索记录与字段台账中。",
        "[余下未核实字段](audit_work/pending_reference_decisions.md)逐项列出，均保留限制而非标记通过。历史检索原始导出、独立编码/前瞻验证未取得，已在正文收窄或声明限制；它们不被伪造为已完成的实证。", "",
        "## 验收与后续范围", "",
        f"当前输入绑定的新编译：{manifest['compilation_passed']}；[编译与渲染记录](audit_work/compile_verification.json)。pdfLaTeX → BibTeX → pdfLaTeX → pdfLaTeX，保持SyncTeX同步。",
        "[结构验收](audit_work/static_reference_checks.json)检查引用、aux/bbl、证据覆盖及输入输出哈希；结构通过不代表所有字段全部核实。",
        "[保护验收](audit_work/correction_verification.json)检查隐藏正文、19个原图、历史章节、历史排除记录和五篇用户PDF未变化。修正前文件保存在audit_work/before_stage2_completion_20261010.zip。",
        "全面格式调整与图中文字缩小仍是后续阶段。原图仍保留旧84条快照，需要随后同步为pool85（I13/S17/B46/T9）、active78（I13/S15/B42/T8），并核对分类标签。此次未改原图。",
        "长URL、原有版面警告及AI绘图采用来源说明留待相应阶段，不能据本次编译宣称整篇已达到最终投稿排版要求。", "",
        "复核命令：", "", "```powershell", "python -B tools/build_reference_inventory.py",
        "python -B tools/build_audit_ledgers.py", "python -B tools/static_reference_checks.py", "```", "",
        "生成器仅整理已审阅证据，不能靠改哈希、题名相似或自动匹配证明来源。历史literature_audit.csv的旧匹配列保留；当前结论以两份台账为准。", ""]
    (ROOT / "reference_audit_report.md").write_text("\n".join(lines), encoding="utf-8")


def write_pending(manifest: dict, refs: list[dict], claims: list[dict]) -> None:
    rows = []
    for r in refs:
        for field, f in {**r["field_checks"], **r["additional_field_checks"]}.items():
            if f["status"] in {"verified", "not_applicable"}:
                continue
            essential = field in {"author", "title", "year", "venue", "type"}
            rows.append({"key":r["key"], "field":field, "status":f["status"], "current":f.get("current",""),
                "source_or_expected":f.get("expected",""), "evidence_url":f.get("evidence_url",""), "detail":f.get("notes",""),
                "blocking":essential, "category":"essential_identity" if essential else "optional_field_or_access_limit",
                "action":"获取字段级正式证明后补全；当前明确保留未核实，不编造。"})
    if rows:
        write_csv(WORK / "pending_reference_decisions.csv", rows)
    blockers = [r for r in rows if r["blocking"]]
    if blockers:
        raise ValueError("Unresolved essential identity fields: " + str(blockers))
    boundaries = [{"command_id":c["command_id"], "support_degree":c["support_degree"], "recommendation":c["recommendation"]}
        for c in claims if c["support_degree"] != "direct"]
    dump(WORK / "pending_reference_decisions.json", {"audit_date":AUDIT_DATE, "stage_two_complete":manifest["stage_two_complete"],
        "blocking_items":blockers, "unresolved_metadata_fields":rows, "citation_rows_with_evidence_boundary":boundaries,
        "resolved_author_decisions":[FOLLOWUP["triad_decision"]], "pending_followup_edits":[],
        "resolved_stage2_items":["Pinned preprint/technical versions","Formal PDF/HTML author and page differences adjudicated",
            "13 core eligibility reviews","Ten cases:6 agreement/4 disagreement","Necessary prose corrections implemented"],
        "out_of_scope_followup":["Full formatting","Original figure statistics/labels and font reduction","Historical search exports or independent prospective validation if later pursued"]})
    lines = ["# 第二阶段已处理事项与剩余证据限制", "", f"截至：{AUDIT_DATE}。第二阶段完成状态：{manifest['stage_two_complete']}。",
        "书目、版本、案例和必要正文修正已落实；下面未核实的字段仍不标记通过。作者分析/未来建议有明确边界，不因结构通过升级为原论文实证。", "",
        "## 已关闭事项", "", "| 项目 | 当前处理 |", "|---|---|",
        "| Triad | 作者已确认I→S；正文/CSV/Highlights同步，支持性例子保留 |",
        "| 版本选择 | GPT-4、MemGPT、ChatLaw、AgentCoder固定v1；Minsky采用所链接1988版；软件/协议采用记录的版本或日期 |",
        "| 正式PDF差异 | AutoGen14作者、AgentCoder v1五作者、GAIA六作者、DSPy题名/作者、Self-RAG与LegalBench作者表示已核；差异历史保留 |",
        "| 出版字段 | Natural Questions453–466；LLM-MedQA1–8；Memory survey Article155/155:1–155:47；EduPlanner Multiagent；其他可确认正式页码补齐 |",
        "| 重要正文归因 | Financial QA反馈及答案修订；跨reasoner比较、框架类别、知识共享/自省效果边界已修正 |",
        "| 核心纳入 | 13项按五标准重核；QA需是实质主要评估轨道，可同时包含代码/写作等任务 |",
        "| 十案例 | 固定原建议标签，来源流程统一编码；六例一致、四例不一致，不是预测准确率或混合架构验证 |", "",
        "## 剩余限制与后续范围", "",
        f"逐字段未核实记录{len(rows)}项，当前阻塞项{len(blockers)}项。条目数量不是错误文献数量，包含空白可选字段和访问限制。完整当前值、证据、原因与blocking标志见[CSV](pending_reference_decisions.csv)。",
        "部分会议论文的DOI/页码缺少正式证明；URL挑战页/访问失败不代表作品不存在。无正式页码依据的字段保持空白；既有而未证实的可选值标为未核实。Attention等未获正式页码证明的限制保留；SWE-agent已取得正式页面和官方BibTeX，旧页码限制已关闭。",
        "原始检索导出不可获得：正文只将候选和筛选数量称为历史日志，未重建或冒充当年的实际检索。十案例没有独立盲评、前瞻验证或来源编码的混合案例，已在正文声明。",
        "后续格式阶段处理长URL和版面；图片阶段缩小图中文字、同步旧84快照和相关分类标签，核实AI绘图采用来源。此次原图、隐藏章节和用户PDF保持不变。", "",
        "## 未核实字段按记录列出", "", "| key | 字段及状态 |", "|---|---|"]
    for r in refs:
        fields = [f["field"]+":"+FIELD_ZH[f["status"]] for f in rows if f["key"]==r["key"]]
        if fields:
            lines.append(f"| {r['key']} | {cell(', '.join(fields))} |")
    lines += ["", "## 正文证据边界", "", "下列均按具体语境标记为作者综合、方案建议或混合支持；没有未经处理的partial/unsupported/contradicted/not_verified事实归因。逐来源支持范围见citation_claim_audit.md。", "",
        "| 引用ID | 判断 | 保留理由 |", "|---|---|---|"]
    lines += [f"| {c['command_id']} | {DEGREE_ZH[c['support_degree']]} | {cell(c['recommendation'])} |" for c in claims if c["support_degree"] != "direct"]
    (WORK / "pending_reference_decisions.md").write_text("\n".join(lines).rstrip()+"\n", encoding="utf-8")
    write_scientific_reports()


def write_scientific_reports() -> None:
    cases = ["# 十案例控制权分类复核", "", f"日期：{AUDIT_DATE}。保留此前建议标签，来源流程使用统一规则重编码。",
        "稳定调度、审批或最终决策权归为层级；没有持续上级控制的对等更新归为扁平；混合需要实际控制权切换的证据。反馈、投票、图结构或多角色本身不足以认定混合。", "",
        "六例一致、四例不一致；来源流程9层级、1扁平、0混合。这是本文回顾性解释，不是原作者自报类别、独立盲评或预测准确率；当前样本不能验证混合分支。", "",
        "| 案例 | 角色 | 原建议 | 来源流程编码 | 匹配 | 原文位置与依据 |", "|---|---|---|---|---|---|"]
    for c in CASES["cases"]:
        cases.append(f"| {c['name']} | {c['evidence_role']} | {c['prior_proposed_label']} | {c['source_based_label']} | {'一致' if c['match']=='agreement' else '不一致'} | [{cell(c['locator'])}]({c['evidence_url']})：{cell(c['source_evidence'])} |")
    cases += ["", "Triad是单智能体多角色流程，作为S支持例子；ChatDev/AgentCoder代码任务、EduPlanner教学设计均不纳入核心QA研究。AgentCoder v1的executor是脚本，不能据三个命名角色认定三个LLM智能体。", ""]
    (WORK / "case_classification_audit.md").write_text("\n".join(cases), encoding="utf-8")
    core = ["# 核心研究纳入标准复核", "", f"日期：{AUDIT_DATE}。共{CORE['core_count']}项保留I；Triad已为S。",
        "五项标准：2019-01至2026-07；LLM主干；至少两个协作智能体；QA/问题驱动推理是实质主要评估轨道；方法及实证评估。QA不必是唯一任务。", "",
        "| key | 所用版本/年份 | 方法及评估证据 | 五项标准 | 范围限制 |", "|---|---|---|---|---|"]
    for r in CORE["records"]:
        links = "、".join(f"[来源{i+1}]({u})" for i,u in enumerate(r["sources"]))
        core.append(f"| {r['key']} | {cell(r['source_version'])} / {r['year']} | {cell(r['locator'])}：{cell(r['method_evidence'])} {links} | {cell(r['criteria'])} | {cell(r.get('scope_note',''))} |")
    core += ["", "核心I标签仅表明符合本文纳入标准，不代表临床安全、现实部署或所有机制都属于混合架构。来源页面与同一机构PDF不是独立双源；版本或获取限制在主台账另列。", ""]
    (WORK / "core_eligibility_audit.md").write_text("\n".join(core), encoding="utf-8")


if __name__ == "__main__":
    main()
