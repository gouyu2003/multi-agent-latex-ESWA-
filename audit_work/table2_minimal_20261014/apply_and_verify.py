from pathlib import Path
import collections, csv, difflib, hashlib, json, re, subprocess, sys

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from active_tex import scan_manuscript
from build_reference_inventory import balanced_entries

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(name, obj): (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf8')
def table(text):
    label = text.index(r'\label{tab:9categories}')
    start = text.rfind(r'\begin{table*}', 0, label)
    end = text.index(r'\end{table*}', label) + len(r'\end{table*}')
    return start, end, text[start:end]
def cells(tex):
    body = tex.split(r'\toprule', 1)[1].split(r'\bottomrule', 1)[0]
    body = re.sub(r'\s*\\(?:midrule|toprule)\s*', ' ', body)
    rows = [r.strip() for r in body.split(r'\\') if r.strip()]
    result = []
    last = ''
    for row in rows[1:]:
        parts = [' '.join(x.split()) for x in row.split('&')]
        assert len(parts) == 6, parts
        parts[0] = re.sub(r'\\multirow\{\d+\}\{\*\}\{\\textbf\{([^}]+)\}\}', r'\1', parts[0])
        parts[0] = re.sub(r'\\textbf\{([^}]+)\}', r'\1', parts[0])
        if not parts[0]: parts[0] = last
        else: last = parts[0]
        result.append(parts)
    assert len(result) == 8
    return result

before_bytes = ((OUT/'before_manuscript.tex') if (OUT/'before_manuscript.tex').exists() else (ROOT/'manuscript.tex')).read_bytes()
print('Read current manuscript', flush=True)
before = before_bytes.decode('utf8')
newline = '\r\n' if '\r\n' in before else '\n'
plan = (ROOT / 'TABLE2_MENTOR_MINIMAL_CORRECTION_PLAN.md').read_text(encoding='utf8')
mentor = subprocess.check_output(['git', 'show', 'f84c78b2720bd5cad8fa32eeb7eaa3a510a8263d:manuscript.tex'], cwd=ROOT).decode('utf8')
print('Read mentor baseline', flush=True)
draft = plan.split('## 8. ', 1)[1].split('```latex\n', 1)[1].split('\n```', 1)[0]
draft = draft.replace('    % UNCERTAIN R1C6: keep the current cell pending a separate decision.\n', '')
draft = draft.replace('Coordination cost and aggregation sensitivity', 'Cost and aggregation sensitivity')
draft = draft.replace('  alone do not establish Hybrid. A fixed human approver is hierarchical.',
    '  alone do not establish Hybrid. A hybrid architecture requires a demonstrated\n'
    '  change in decision authority. A fixed human approver is hierarchical.')
draft = draft.replace('\n', newline)
start, end, old_table = table(before)
intro_old = 'related mechanisms are shown separately' + newline + 'and do not define additional architecture classes.'
intro_new = 'related mechanisms' + newline + 'do not define additional architecture classes.'
assert before.count(intro_old) == 1
after = before[:start] + draft + before[end:]
after = after.replace(intro_old, intro_new, 1)
approved_content_after = after
old_columns = r'\begin{tabular}{p{1.4cm} p{2.0cm} p{2.4cm}  p{3.2cm} p{2.3cm} p{2.2cm}}'
new_columns = (r'\begin{tabular}{>{\raggedright\arraybackslash}p{1.5cm} '
    r'>{\raggedright\arraybackslash}p{2.0cm} >{\raggedright\arraybackslash}p{2.4cm} '
    r'>{\raggedright\arraybackslash}p{3.2cm} >{\raggedright\arraybackslash}p{2.3cm} '
    r'>{\raggedright\arraybackslash}p{2.2cm}}')
assert draft.count(old_columns)==1
draft = draft.replace(old_columns,new_columns,1)
after = after.replace(old_columns,new_columns,1)
assert after.replace(draft, old_table, 1).replace(intro_new, intro_old, 1) == before
mc = cells(table(mentor)[2]); nc = cells(draft)
ledger = []
for r in range(8):
    for c in range(6):
        ident = f'R{r+1}C{c+1}'
        line = next(x for x in plan.splitlines() if x.startswith('| ' + ident + ' /'))
        classification = re.search(r'\*\*(KEEP|MINIMAL FIX|STRUCTURAL FIX|UNCERTAIN)\*\*', line)[1]
        if classification == 'KEEP': assert mc[r][c] == nc[r][c], (ident, mc[r][c], nc[r][c])
        ledger.append(dict(id=ident, decision=classification, mentor=mc[r][c], after=nc[r][c], unchanged=mc[r][c] == nc[r][c]))
assert collections.Counter(x['decision'] for x in ledger) == {'KEEP':38,'MINIMAL FIX':4,'STRUCTURAL FIX':5,'UNCERTAIN':1}
assert sum(x['unchanged'] for x in ledger) == 38
fixes = {
 'R2C1':r'Hierarchical$^{a}$', 'R3C1':'---',
 'R5C2':'Staged evidence-processing pipeline',
 'R5C3':r'LONGAGENT; Chain-of-Agents; CoCoA-zero \citep{zhao2024longagent,zhang2024chain_agents,jiang2026cocoa}',
 'R6C1':'---',
 'R6C4':'GPTSwarm DAG connection optimisation; LangGraph transitions permit loops, branches, and routing policies',
 'R7C1':r'Hierarchical$^{b}$', 'R8C1':'---',
 'R8C3':r'LangGraph breakpoints \citep{langgraph2024interrupt}',
 'R1C6':'Cost and aggregation sensitivity',
}
assert all(next(x for x in ledger if x['id']==k)['after']==v for k,v in fixes.items())
assert r'\multirow{2}' in draft and 'Architecture classes}}' not in draft
snapshot = {}
print('All 48 cells checked; protecting existing files', flush=True)
if (OUT/'protected_manifest.json').exists():
    snapshot = json.loads((OUT/'protected_manifest.json').read_text(encoding='utf8'))
else:
    for p in ROOT.rglob('*'):
        if not p.is_file() or '.git' in p.relative_to(ROOT).parts or OUT in p.parents: continue
        snapshot[p.relative_to(ROOT).as_posix()] = sha(p)
        if len(snapshot) % 1000 == 0: print(f'Protected {len(snapshot)} files', flush=True)
    dump('protected_manifest.json', snapshot)
(OUT/'before_manuscript.tex').write_bytes(before_bytes)
(OUT/'mentor_table2.tex').write_text(table(mentor)[2],encoding='utf8')
(OUT/'before_table2.tex').write_bytes(old_table.encode('utf8'))
(OUT/'after_table2.tex').write_bytes(draft.encode('utf8'))
print('Scanning before source', flush=True)
scan0 = scan_manuscript(ROOT, 'audit_work/table2_minimal_20261014/before_manuscript.tex')
keys0 = sorted({k for c in scan0.citations for k in c.keys})
q5 = (ROOT/'audit_work/mentor_restore_stage2_20261013/q5_case_scores.json').read_bytes()
assert (ROOT/'manuscript.tex').read_bytes() in (before_bytes,after.encode('utf8'),approved_content_after.encode('utf8')), 'Concurrent manuscript changes; stop'
if (ROOT/'manuscript.tex').read_bytes()!=after.encode('utf8'):
    (ROOT/'manuscript.tex').write_bytes(after.encode('utf8'))
print('Scanning after source', flush=True)
scan = scan_manuscript(ROOT)
keys = sorted({k for c in scan.citations for k in c.keys})
assert keys == keys0 and len(keys) == 78
entries = balanced_entries((ROOT/'references.bib').read_text(encoding='utf8'))
roles = {r['key']:r['evidence_role'] for r in csv.DictReader((ROOT/'literature_audit.csv').open(encoding='utf-8-sig'))}
assert len(entries)==85 and sum(roles[k]=='I' for k in keys)==13 and roles['hu2024triad']=='S'
assert q5==(ROOT/'audit_work/mentor_restore_stage2_20261013/q5_case_scores.json').read_bytes()
print('Verifying protection snapshot', flush=True)
checked = {name:h for name,h in snapshot.items() if not name.startswith('tmp/')}
changed = [name for name,h in checked.items() if sha(ROOT/name)!=h]
assert changed==['manuscript.tex'], changed
dump('cell_verification.json',ledger)
dump('static_acceptance.json',dict(keep_cells_exact=38,necessary_fixes=9,approved_r1c6=nc[0][5],
  protected_files=len(snapshot),final_non_temporary_files_checked=len(checked),changed_existing_files=changed,only_table2_and_intro=True,
  bib_pool=85,active_cited=78,core=13,active_keys=keys,
  commands_before=len(scan0.citations),commands_after=len(scan.citations),
  key_occurrences_before=sum(len(c.keys) for c in scan0.citations),key_occurrences_after=sum(len(c.keys) for c in scan.citations),
  q5_source_ledger_preserved=True,manuscript_before_sha256=hashlib.sha256(before_bytes).hexdigest(),manuscript_after_sha256=sha(ROOT/'manuscript.tex')))
(OUT/'before_after.patch').write_bytes(''.join(difflib.unified_diff(before.replace('\r\n','\n').splitlines(True),after.replace('\r\n','\n').splitlines(True),fromfile='before/manuscript.tex',tofile='after/manuscript.tex')).encode('utf8'))
print(json.dumps(dict(keep_exact=38,fixes=9,r1c6=nc[0][5],protected=len(snapshot),changed=changed,bib_pool=85,active=78,core=13),ensure_ascii=False))
