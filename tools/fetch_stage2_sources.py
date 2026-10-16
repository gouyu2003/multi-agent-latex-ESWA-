"""Fetch public primary evidence for the authorized stage-two reference audit."""
from project_paths import project_path
import hashlib
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import fitz
import requests

ROOT = Path(__file__).resolve().parents[1]
WORK = project_path('audit_work')
OUT = project_path('audits/references/stage2_sources')
OUT.mkdir(exist_ok=True)
request_name = sys.argv[1] if len(sys.argv) > 1 else 'stage2_source_requests.json'
output_name = sys.argv[2] if len(sys.argv) > 2 else 'stage2_source_retrieval.json'
items = json.loads((WORK / request_name).read_text(encoding='utf-8'))

def fetch(item):
    result = dict(item, retrieved_on='2026-10-10')
    try:
        response = requests.get(item['url'], timeout=(15, 45), headers={'User-Agent': 'ManuscriptReferenceAudit/1.0 (public scholarly metadata)'})
        result.update(status=response.status_code, final_url=response.url, content_type=response.headers.get('Content-Type', ''), byte_count=len(response.content))
        if response.status_code != 200:
            result['error'] = response.text[:300]
            return result
        is_pdf = response.content.startswith(b'%PDF')
        extension = '.pdf' if is_pdf else '.json' if 'json' in result['content_type'] else '.txt'
        path = OUT / (item['id'] + extension)
        path.write_bytes(response.content)
        result.update(file=path.relative_to(ROOT).as_posix(), sha256=hashlib.sha256(response.content).hexdigest())
        if is_pdf:
            with fitz.open(path) as document:
                pages = [{'page': i + 1, 'text': page.get_text()} for i, page in enumerate(document)]
            text_path = OUT / (item['id'] + '_text.json')
            text_path.write_text(json.dumps(pages, ensure_ascii=False, indent=2), encoding='utf-8')
            result.update(page_count=len(pages), text_file=text_path.relative_to(ROOT).as_posix(), text_sha256=hashlib.sha256(text_path.read_bytes()).hexdigest())
    except Exception as exc:
        result['error'] = str(exc)
    return result

with ThreadPoolExecutor(max_workers=8) as executor:
    results = list(executor.map(fetch, items))
(WORK / output_name).write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps([{'id': r['id'], 'status': r.get('status'), 'pages': r.get('page_count'), 'error': r.get('error', '')[:150]} for r in results], ensure_ascii=False))
