from pathlib import Path
import json,sys
v=sys.stdin.readline().strip()
assert v.startswith('nvapi-')
p=Path(r'D:\llm-gateway\private\nvidia-new.json')
if p.exists(): print('Staging file exists; no change')
else:p.write_text(json.dumps({'nvidia':v}),encoding='utf8');print('NVIDIA key staged in restricted folder')
