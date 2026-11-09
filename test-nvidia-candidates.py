from pathlib import Path
import json,urllib.request,urllib.error,concurrent.futures
key=json.loads(Path(r'D:\llm-gateway\private\nvidia-new.json').read_text())['nvidia']
models=['nvidia/nemotron-3.5-bolt-e4b','nvidia/nemotron-3.5-lightning-30b-a3b','google/gemma-4-31b-it']
def run(model):
 body={'model':model,'messages':[{'role':'user','content':'Reply OK'}],'max_tokens':48}
 req=urllib.request.Request('https://integrate.api.nvidia.com/v1/chat/completions',data=json.dumps(body).encode(),headers={'Authorization':'Bearer '+key,'Content-Type':'application/json','User-Agent':'curl/8.7.1'})
 try:
  with urllib.request.urlopen(req,timeout=40) as r:j=json.load(r);return model+' HTTP '+str(r.status)+' response='+str(bool(j.get('choices')))
 except urllib.error.HTTPError as e:
  return model+' HTTP '+str(e.code)+' '+e.read(150).decode(errors='replace').replace(key,'[redacted]')
 except Exception as e:return model+' '+type(e).__name__
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 for f in concurrent.futures.as_completed([ex.submit(run,m) for m in models]):print(f.result(),flush=True)
