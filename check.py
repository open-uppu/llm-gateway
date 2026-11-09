from pathlib import Path
import json, urllib.request
key = Path(r'D:\llm-gateway\.env').read_text().strip().split('=', 1)[1]
for model in ('cloud-llm7', 'local-qwen'):
    data = json.dumps({'model': model, 'messages': [{'role': 'user', 'content': 'Reply with OK'}], 'max_tokens': 256}).encode()
    req = urllib.request.Request('http://127.0.0.1:4000/v1/chat/completions', data=data, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + key})
    try:
        with urllib.request.urlopen(req, timeout=120) as res:
            result = json.load(res)
            print(model, 'PASS', repr(result['choices'][0]['message']['content']))
    except Exception as exc:
        print(model, 'FAIL', str(exc))
