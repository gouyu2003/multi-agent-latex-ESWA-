"""Resolve current files and legacy paths without rewriting historical records."""
from functools import lru_cache
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / 'audits/organization/20261016'

@lru_cache(maxsize=1)
def _mapping():
    return (json.loads((RECORD/'path_mapping.json').read_text(encoding='utf-8')),
            json.loads((RECORD/'directory_mapping.json').read_text(encoding='utf-8')))

def project_path(relative):
    """Return the current path; live build outputs override historical snapshots."""
    path = Path(relative)
    if path.is_absolute():
        return path
    name = path.as_posix()
    files, directories = _mapping()
    for old,new in directories['runtime'].items():
        if name == old or name.startswith(old+'/'):
            return ROOT / (new + name[len(old):])
    if name in files:
        return ROOT / files[name]
    for old,new in sorted(directories['prefixes'].items(), key=lambda item:len(item[0]), reverse=True):
        if name == old or name.startswith(old+'/'):
            return ROOT / (new + name[len(old):])
    return ROOT / name
