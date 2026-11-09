from pathlib import Path
import json
p=Path(r'D:\llm-gateway\private\pending-provider-keys.json')
d=json.loads(p.read_text(encoding='utf-8'))
d['keys']={k:v for k,v in d['keys'].items() if k in ('gonka','nvidia')}
d.pop('cloudflare_accounts',None)
p.write_text(json.dumps(d),encoding='utf-8')
print('Only pending Gonka and NVIDIA credentials retained.')
