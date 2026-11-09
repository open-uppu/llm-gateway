from pathlib import Path
import json,urllib.request,urllib.error,concurrent.futures
keys={}
keys['nvidia']=json.loads(Path(r'D:\llm-gateway\private\nvidia-new.json').read_text())['nvidia']
cases=[('nvidia','https://integrate.api.nvidia.com/v1/chat/completions','nvidia/nemotron-3.5-bolt-e4b')]
def run(c):
 name,url,model=c; body={'model':model,'messages':[{'role':'user','content':'Use get_time tool.'}],'tools':[{'type':'function','function':{'name':'get_time','description':'Get current time','parameters':{'type':'object','properties':{}}}}],'tool_choice':'required','max_tokens':128}
 req=urllib.request.Request(url,data=json.dumps(body).encode(),headers={'Authorization':'Bearer '+keys[name],'Content-Type':'application/json','User-Agent':'curl/8.7.1'})
 try:
  with urllib.request.urlopen(req,timeout=25) as r:
   d=json.load(r);return name+' HTTP '+str(r.status)+' tools='+str(bool(d.get('choices',[{}])[0].get('message',{}).get('tool_calls')))
 except urllib.error.HTTPError as e:
  try:
   data=e.read(400).decode(errors='replace').replace(keys[name],'[redacted]');return name+' HTTP '+str(e.code)+' '+data[:200]
  except Exception:return name+' HTTP '+str(e.code)
 except Exception as e:return name+' '+type(e).__name__
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 for f in concurrent.futures.as_completed([pool.submit(run,c) for c in cases]):print(f.result(),flush=True)
