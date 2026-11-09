from pathlib import Path
import json,urllib.request,urllib.error,concurrent.futures
k=json.loads(Path(r'D:\llm-gateway\private\pending-provider-keys.json').read_text())['keys']
cases=[('gemini','https://generativelanguage.googleapis.com/v1beta/openai/chat/completions','gemini-3.5-flash-lite'),('cohere','https://api.cohere.ai/compatibility/v1/chat/completions','command-a-plus-05-2026'),('cloudflare','https://api.cloudflare.com/client/v4/accounts/f5ef27d87fda5df0ef4c475c3542a351/ai/v1/chat/completions','@cf/openai/gpt-oss-20b')]
def run(case):
 n,url,model=case; body={'model':model,'messages':[{'role':'user','content':'Use the get_time tool now.'}],'tools':[{'type':'function','function':{'name':'get_time','description':'Get the current time','parameters':{'type':'object','properties':{}}}}],'tool_choice':'auto','max_tokens':256}
 req=urllib.request.Request(url,data=json.dumps(body).encode(),headers={'Authorization':'Bearer '+k[n],'Content-Type':'application/json'})
 try:
  with urllib.request.urlopen(req,timeout=35) as r:
   j=json.load(r);ch=j.get('choices',[{}])[0];return n+' HTTP '+str(r.status)+' tool_calls='+str(bool(ch.get('message',{}).get('tool_calls')))
 except urllib.error.HTTPError as e:
  try: error=json.loads(e.read().decode()).get('error',{}); code=error.get('code') if isinstance(error,dict) else None
  except Exception:code=None
  return n+' HTTP '+str(e.code)+' error_code='+str(code)
 except Exception as e:return n+' '+type(e).__name__
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 for f in concurrent.futures.as_completed([pool.submit(run,c) for c in cases]): print(f.result(),flush=True)
