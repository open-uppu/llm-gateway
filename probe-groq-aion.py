from pathlib import Path
import json,sys,urllib.request,urllib.error,concurrent.futures
values=json.loads(sys.stdin.readline());opener=urllib.request.build_opener(urllib.request.ProxyHandler({}))
urls={'groq':'https://api.groq.com/openai/v1/models','aion':'https://api.aionlabs.ai/v1/models'}
def run(name):
 secret=values[name]
 req=urllib.request.Request(urls[name],headers={'Authorization':'Bearer '+secret,'User-Agent':'curl/8.7.1'})
 try:
  with opener.open(req,timeout=15) as r:d=json.load(r);return name,r.status,'models='+str(len(d.get('data',[])))
 except urllib.error.HTTPError as e:
  body=e.read(250).decode(errors='replace').replace(secret,'[redacted]');return name,e.code,body[:120]
 except Exception as e:return name,type(e).__name__,''
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:results=list(ex.map(run,urls))
for x in results:print(x[0],x[1],x[2],flush=True)
valid={n:values[n] for n,status,_ in results if status==200}
p=Path(r'D:\llm-gateway\private\groq-aion-keys.json')
if valid and not p.exists():p.write_text(json.dumps(valid),encoding='utf8');print('authenticated and staged:',','.join(valid),flush=True)
