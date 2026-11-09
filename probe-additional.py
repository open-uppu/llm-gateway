import concurrent.futures,json,urllib.request,urllib.error,sys
from pathlib import Path
values=json.loads(sys.stdin.readline())
conf={'huggingface':'https://huggingface.co/api/whoami-v2','cerebras':'https://api.cerebras.ai/v1/models','sambanova':'https://api.sambanova.ai/v1/models'}
def test(name,secret):
 req=urllib.request.Request(conf[name],headers={'Authorization':'Bearer '+secret})
 try:
  with urllib.request.urlopen(req,timeout=20) as r:
   d=json.load(r);return r.status, len(d.get('data',[])) if isinstance(d,dict) and isinstance(d.get('data'),list) else None
 except urllib.error.HTTPError as e:return e.code,None
 except Exception as e:return type(e).__name__,None
def compare(name):return name,test(name,values[name]),test(name,'invalid-codex-test-key')
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool: results=list(pool.map(compare,conf))
for name,actual,control in results:print(name,'actual',actual,'invalid_control',control,flush=True)
valid={n:values[n] for n,a,c in results if a[0]==200 and c[0]!=200}
p=Path(r'D:\llm-gateway\private\additional-keys.json')
if p.exists():print('Staging file exists; no write',flush=True)
else:p.write_text(json.dumps(valid),encoding='utf8');print('Staged verified:',','.join(valid),flush=True)
