from pathlib import Path
import json,urllib.request
v=json.loads(Path(r'D:\llm-gateway\private\pending-provider-keys.json').read_text())['keys']['gonka']
with urllib.request.urlopen(urllib.request.Request('https://proxy.gonkabroker.com/test-auth',headers={'Authorization':'Bearer '+v}),timeout=12) as r:d=json.load(r)
for k in ('key','settings'):
 obj=d.get(k,{}); print(k,'keys:',list(obj) if isinstance(obj,dict) else type(obj).__name__)
