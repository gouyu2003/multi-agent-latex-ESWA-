"""One-time, lossless project organization; retained with its audit manifest."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
from functools import lru_cache

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / 'audits/organization/20261016'

EXACT = {
    'fig_reference_corpus.pdf': 'figures/figure1/fig_reference_corpus.pdf',
    'fig_reference_corpus.png': 'figures/figure1/fig_reference_corpus.png',
    'fig_reference_corpus.svg': 'figures/figure1/fig_reference_corpus.svg',
    'fig3_topology.pdf': 'figures/figure3/fig3_topology.pdf',
    'Highlights.txt': 'submission/Highlights.txt',
    'cas-model2-names.bst': 'archive/templates/cas-model2-names.bst',
    'figure_source_data.csv': 'archive/data/figure_source_data.csv',
    'APA7_MIGRATION_REPORT.md': 'audits/references/APA7_MIGRATION_REPORT.md',
    'FORMAT_REVIEW_REPORT.md': 'audits/revisions/FORMAT_REVIEW_REPORT.md',
    'reference_audit_report.md': 'audits/references/reference_audit_report.md',
}
for name in ['literature_audit.csv', 'search_log.csv', 'figure1_source_data.csv', 'apa_reference_adaptations.json']:
    EXACT[name] = 'data/' + name
for name in ['MENTOR_BASELINE_RESTORE_PLAN.md', 'MENTOR_BASELINE_RESTORE_STAGE2_REPORT.md',
             'Q4_Q5_CONSERVATIVE_RESTORE_PROPOSAL.md', 'TABLE2_MENTOR_MINIMAL_CORRECTION_PLAN.md']:
    EXACT[name] = 'audits/revisions/' + name
for name in ['change_timeline.jpg', 'classify.jpg',
             'Design logic and trade-offs among flat, hierarchical, and hybrid architectures for multi-agent collaborative QA.jpg',
             'Design logic and trade-offs.png', 'fig_architecture_tradeoffs.jpg', 'fig_flow.jpg',
             'fig_mindmap.jpg', 'fig_prisma_flowchart.pdf', 'fig_pub_overview_nature.pdf',
             'fig_pub_overview_nature.png', 'fig_pub_overview_nature.svg', 'fig2_architecture.pdf',
             'fig4_tech.pdf', 'findmap.png', 'Gemini_Generated_Image_2b3ub22b3ub22b3u.png']:
    EXACT[name] = 'archive/figures/' + name

FIGURE_RUNS = {
    2: '20261013-153831-codex-clipboard-1eb7c158-b30c-49e1-bfa6-5ae40fd6f410',
    4: '20261013-161131-Figure4_architecture_selection',
    5: '20261013-163435-Figure5_resource_map',
}
for number, names in {
    2: ['Figure2_Evolution_of_QA_Paradigms.pdf', 'codex-clipboard-1eb7c158-b30c-49e1-bfa6-5ae40fd6f410_edited.pptx'],
    4: ['Figure4_architecture_selection_authority_v2.pdf', 'Figure4_architecture_selection_authority_v2.pptx'],
    5: ['Figure5_resource_map_edited.pdf', 'Figure5_resource_map_edited.pptx'],
}.items():
    for name in names:
        EXACT[f'output/figure{number}_editable/{FIGURE_RUNS[number]}/final/{name}'] = f'figures/figure{number}/{name}'
for suffix in ['pdf', 'pptx']:
    name = 'Figure4_architecture_selection_edited.' + suffix
    EXACT[f'output/figure4_editable/{FIGURE_RUNS[4]}/final/{name}'] = 'archive/figures/figure4/' + name

PREFIX = {
    'apa7_audit/': 'audits/references/apa7/',
    'figure1_audit/': 'audits/figures/figure1/',
    'archive/ch': 'archive/chapters/ch',
    'audit_work/mentor_restore_stage2_20261013/': 'audits/revisions/mentor_restore_stage2_20261013/',
    'audit_work/table2_minimal_20261014/': 'audits/revisions/table2_minimal_20261014/',
    'audit_work/figure245_replacement_20261013/': 'audits/figures/replacement_20261013/',
    'audit_work/render_checks/': 'audits/figures/render_checks/',
    'audit_work/stage2_sources/': 'audits/references/stage2_sources/',
    'audit_work/': 'audits/references/audit_work/',
    'output/pdf/': 'audits/revisions/table2_previews/',
    'tmp/figure1_revision/python_packages/': '.cache/python/figure1/python_packages/',
    'tmp/figure1_revision/wheels/': '.cache/python/figure1/wheels/',
    'tmp/figure1_revision/mplconfig/': '.cache/python/figure1/mplconfig/',
    'tmp/figure1_revision/build/': 'build/history/figure1_revision/',
    'tmp/figure1_revision/': 'audits/figures/figure1/baseline/',
    'tmp/figure2_packages/': '.cache/python/figure2_packages/',
    'tmp/apa7_vendor/': '.cache/python/apa7_vendor/',
    'tmp/ai_disclosure_20261015/': 'audits/revisions/baselines/ai_disclosure_20261015/',
    'tmp/apa7_migration/': 'audits/references/baselines/apa7_migration/',
    'tmp/conference9_baseline/': 'audits/references/baselines/conference9_baseline/',
    'tmp/conference9_source_baseline/': 'audits/references/baselines/conference9_source_baseline/',
    'tmp/conference9_before_build/': 'audits/references/baselines/conference9_before_build/',
    'tmp/conference9_rendered/': '.cache/previews/conference9_rendered/',
    'tmp/figure5_audit/': 'audits/figures/figure5/history/',
    'tmp/pdfs/': '.cache/downloads/pdfs/',
    'tmp/apa7_build/': 'build/history/apa7_build/',
    'tmp/apa7_regression/': 'build/history/apa7_regression/',
    'tmp/table2_minimal_20261014_build/': 'build/history/table2_minimal_20261014_build/',
    'tmp/apa7_scanner_tests/': '.cache/tests/apa7_scanner_tests/',
    'tmp/reference_scan_tests/': '.cache/tests/reference_scan_tests/',
}
for number in FIGURE_RUNS:
    PREFIX[f'output/figure{number}_editable/'] = f'audits/figures/figure{number}/editable_workflow/'

def destination(old):
    if old in EXACT:
        return EXACT[old]
    if old.startswith('audit_work/before_') and old.endswith('.zip'):
        return 'audits/revisions/backups/' + Path(old).name
    if old.startswith('manuscript.') and old != 'manuscript.tex':
        return 'build/baseline_20261016/' + old
    for source in sorted(PREFIX, key=len, reverse=True):
        if old.startswith(source):
            return PREFIX[source] + old[len(source):]
    if old.startswith('tmp/'):
        return 'audits/references/scripts/' + old[len('tmp/'):]
    return old

@lru_cache(maxsize=None)
def inside(relative):
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT) or path == ROOT or path.is_relative_to(ROOT / '.git'):
        raise ValueError('Unsafe path: ' + relative)
    return path

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    if (RECORD / 'file_manifest.json').exists():
        raise SystemExit('Organization manifest already exists; do not rerun.')
    files = []
    for directory in ROOT.iterdir():
        if directory.name == '.git':
            continue
        files.extend(directory.rglob('*') if directory.is_dir() else [directory])
    files = sorted(p for p in files if p.is_file())
    tracked_result = subprocess.run(['git', 'ls-files', '-z'], cwd=ROOT, capture_output=True, check=True)
    tracked = set(tracked_result.stdout.decode('utf-8').split('\0'))
    rows = []
    targets = set()
    for index, source in enumerate(files, 1):
        old = source.relative_to(ROOT).as_posix()
        new = destination(old)
        target = inside(new)
        if new != old and target.exists():
            raise RuntimeError('Destination already exists: ' + new)
        if new.casefold() in targets:
            raise RuntimeError('Destination collision: ' + new)
        targets.add(new.casefold())
        rows.append(dict(old=old, new=new, size=source.stat().st_size, sha256=sha(source), tracked=old in tracked))
        if index % 1000 == 0:
            print('Recorded', index, 'file hashes.', flush=True)
    print(json.dumps(dict(files=len(rows), moves=sum(r['old'] != r['new'] for r in rows),
                          bytes=sum(r['size'] for r in rows)), indent=2))
    if '--apply' not in sys.argv:
        return
    RECORD.mkdir(parents=True, exist_ok=True)
    (RECORD / 'file_manifest.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    (RECORD / 'path_mapping.json').write_text(json.dumps({r['old']:r['new'] for r in rows if r['old']!=r['new']}, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    for index, row in enumerate(rows, 1):
        if row['old'] == row['new']:
            continue
        source, target = inside(row['old']), inside(row['new'])
        if sha(source) != row['sha256']:
            raise RuntimeError('Source changed during organization: ' + row['old'])
        target.parent.mkdir(parents=True, exist_ok=True)
        source.rename(target)
        if index % 1000 == 0:
            print('Moved through', index, 'manifest entries.', flush=True)
    failures = [r['new'] for r in rows if sha(inside(r['new'])) != r['sha256']]
    if failures:
        raise RuntimeError('Content mismatch: ' + repr(failures))
    # Only empty directories are removed; no file is deleted.
    for old_root in ['archive', 'audit_work', 'apa7_audit', 'figure1_audit', 'output', 'tmp']:
        parent = inside(old_root)
        if not parent.exists():
            continue
        for directory in sorted((p for p in parent.rglob('*') if p.is_dir()), key=lambda p:len(p.parts), reverse=True):
            inside(directory.relative_to(ROOT).as_posix())
            if not any(directory.iterdir()):
                directory.rmdir()
        if not any(parent.iterdir()):
            parent.rmdir()
    (RECORD / 'move_verification.json').write_text(json.dumps(dict(files=len(rows), moves=sum(r['old']!=r['new'] for r in rows),
        all_original_files_preserved=True, all_sha256_identical=True, deleted_files=0), indent=2)+'\n', encoding='utf-8')
    print('All original files verified byte-for-byte after moving.')

if __name__ == '__main__':
    main()
