import concurrent.futures, json, urllib.request, urllib.error, sys
values=json.loads(sys.stdin.readline())
configs={
'openrouter':('https://openrouter.ai/api/v1/models','Authorization','Bearer '),
'groq':('https://api.groq.com/openai/v1/models','Authorization','Bearer '),
'gemini':('https://generativelanguage.googleapis.com/v1beta/models','x-goog-api-key',''),
'mistral':('https://api.mistral.ai/v1/models','Authorization','Bearer '),
'cloudflare':('https://api.cloudflare.com/client/v4/accounts','Authorization','Bearer '),
'nvidia':('https://integrate.api.nvidia.com/v1/models','Authorization','Bearer '),
'cohere':('https://api.cohere.com/v2/models','Authorization','Bearer '),
'aion':('https://api.aionlabs.ai/v1/models','Authorization','Bearer '),
'gonka':('https://proxy.gonkabroker.com/v1/models','Authorization','Bearer '),
}
def test(name):
 url,header,prefix=configs[name]
 req=urllib.request.Request(url,headers={header:prefix+values[name]})
 try:
  with urllib.request.urlopen(req,timeout=20) as r:
   data=json.load(r); status=r.status
  out={'provider':name,'http':status}
  if name=='cloudflare': out['account_ids']=[x.get('id') for x in data.get('result',[]) if x.get('id')]
  return out
 except urllib.error.HTTPError as e:return {'provider':name,'http':e.code}
 except Exception as e:return {'provider':name,'error':type(e).__name__}
with concurrent.futures.ThreadPoolExecutor(max_workers=9) as pool:
 results=list(pool.map(test,configs))
print(json.dumps([{k:v for k,v in r.items() if k!='account_ids'} for r in results]),flush=True)
valid={r['provider']:values[r['provider']] for r in results if r.get('http')==200}
cloud=next((r for r in results if r['provider']=='cloudflare'),{})
# Store temporary credentials on the target, restricted to the current user by inheritance.
from pathlib import Path
p=Path(r'D:\llm-gateway\private\pending-provider-keys.json')
if p.exists():
 print('pending credentials file already exists; no write made',flush=True)
else:
 p.write_text(json.dumps({'keys':valid,'cloudflare_accounts':cloud.get('account_ids',[])}),encoding='utf-8')
 print('usable keys staged:',len(valid),'cloudflare accounts found:',len(cloud.get('account_ids',[])),flush=True)
