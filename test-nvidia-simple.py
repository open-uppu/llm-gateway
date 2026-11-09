from pathlib import Path
import json,urllib.request,urllib.error
key=json.loads(Path(r'D:\llm-gateway\private\nvidia-new.json').read_text())['nvidia']
body={'model':'google/gemma-4-31b-it','messages':[{'role':'user','content':'Reply OK'}],'max_tokens':48}
req=urllib.request.Request('https://integrate.api.nvidia.com/v1/chat/completions',data=json.dumps(body).encode(),headers={'Authorization':'Bearer '+key,'Content-Type':'application/json'})
try:
 with urllib.request.urlopen(req,timeout=30) as r:j=json.load(r);print('HTTP',r.status,'response',bool(j.get('choices')))
except urllib.error.HTTPError as e:
 try:print('HTTP',e.code,'detail',e.read(250).decode(errors='replace').replace(key,'[redacted]'))
 except Exception:print('HTTP',e.code)
except Exception as e:print(type(e).__name__)
