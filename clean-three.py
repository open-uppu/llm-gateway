from pathlib import Path
import json
p=Path(r'D:\llm-gateway\private')
for name in ('groq-aion-keys.json','nvidia-new.json'):
 f=p/name
 if f.exists():f.unlink()
f=p/'pending-provider-keys.json'
if f.exists():
 d=json.loads(f.read_text(encoding='utf8'));d['keys'].pop('nvidia',None);f.write_text(json.dumps(d),encoding='utf8')
print('Temporary copies removed; configured credentials remain in restricted providers.env')
