from pathlib import Path
import json,sys,urllib.request,urllib.error
key=sys.stdin.readline().strip()
body={'model':'gemma-4-31B-it','messages':[{'role':'user','content':'Reply OK.'}],'max_tokens':64}
req=urllib.request.Request('https://api.sambanova.ai/v1/chat/completions',data=json.dumps(body).encode(),headers={'Authorization':'Bearer '+key,'Content-Type':'application/json'})
try:
 with urllib.request.urlopen(req,timeout=25) as r:
  d=json.load(r);print('SAMBA',r.status,'has_response',bool(d.get('choices')),flush=True)
 p=Path(r'D:\llm-gateway\private\additional-keys.json');j=json.loads(p.read_text());j['sambanova']=key;p.write_text(json.dumps(j),encoding='utf8')
except urllib.error.HTTPError as e:
 try:
  d=json.loads(e.read()); error=d.get('error',{}); print('SAMBA',e.code,'error',str(error).replace(key,'[redacted]')[:350],flush=True)
 except Exception:print('SAMBA',e.code,flush=True)
except Exception as e:print('SAMBA',type(e).__name__,flush=True)
