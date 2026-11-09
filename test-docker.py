import urllib.request,urllib.error,json,time,concurrent.futures
from pathlib import Path
key=Path(r'D:\llm-gateway\.env').read_text().strip().split('=',1)[1]
headers={'Authorization':'Bearer '+key,'Content-Type':'application/json'}
for i in range(25):
 try:
  with urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:4001/v1/models',headers=headers),timeout=2) as r: print('MODEL_COUNT',len(json.load(r)['data']),flush=True)
  break
 except Exception: time.sleep(1)
else: raise SystemExit('Gateway unavailable')
def test(name):
 req=urllib.request.Request('http://127.0.0.1:4001/v1/chat/completions',data=json.dumps({'model':name,'messages':[{'role':'user','content':'Say hello'}],'max_tokens':256}).encode(),headers=headers)
 try:
  with urllib.request.urlopen(req,timeout=40) as r:
   j=json.load(r); return name+' OK '+repr(j['choices'][0]['message'].get('content'))[:100]
 except urllib.error.HTTPError as e: return name+' HTTP '+str(e.code)+' '+e.read(500).decode(errors='replace')
 except Exception as e:return name+' '+str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 for x in pool.map(test,['ovh/gpt-oss-20b','llm7/gpt-oss:20b','local-qwen']):print(x,flush=True)
