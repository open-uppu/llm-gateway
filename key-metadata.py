from pathlib import Path
import json,urllib.request
x=json.loads(Path(r'D:\llm-gateway\private\pending-provider-keys.json').read_text())['keys']
for name,url in [('openrouter','https://openrouter.ai/api/v1/key'),('gonka','https://proxy.gonkabroker.com/test-auth')]:
 req=urllib.request.Request(url,headers={'Authorization':'Bearer '+x[name]})
 try:
  with urllib.request.urlopen(req,timeout=12) as r:d=json.load(r)
  if name=='openrouter': print(name,'free_tier_flag',d.get('data',{}).get('is_free_tier'))
  else: print(name,'response keys',','.join(d.keys()))
 except Exception as e:print(name,'error',type(e).__name__)
