import concurrent.futures,json,urllib.request,urllib.error
from pathlib import Path
p=Path(r'D:\llm-gateway\private\pending-provider-keys.json'); keys=json.loads(p.read_text())['keys']
conf={'openrouter':('https://openrouter.ai/api/v1/key','Authorization','Bearer '),'gemini':('https://generativelanguage.googleapis.com/v1beta/models','x-goog-api-key',''),'mistral':('https://api.mistral.ai/v1/models','Authorization','Bearer '),'cloudflare':('https://api.cloudflare.com/client/v4/user/tokens/verify','Authorization','Bearer '),'nvidia':('https://integrate.api.nvidia.com/v1/models','Authorization','Bearer '),'cohere':('https://api.cohere.com/v2/models','Authorization','Bearer '),'gonka':('https://proxy.gonkabroker.com/test-auth','Authorization','Bearer ')}
def req(url,h,v):
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={h:v}),timeout=15) as r:
   body=json.load(r); return r.status,body.get('success') if isinstance(body,dict) else None
 except urllib.error.HTTPError as e:return e.code,None
 except Exception as e:return type(e).__name__,None
def run(n):
 url,h,prefix=conf[n]; actual=req(url,h,prefix+keys[n]); fake=req(url,h,prefix+'invalid-codex-test-key');return (n,actual,fake)
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as ex:
 for n,a,b in ex.map(run,keys):print(n,'actual',a,'invalid_control',b,flush=True)
