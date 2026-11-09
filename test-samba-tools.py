import json,urllib.request,urllib.error
from pathlib import Path
k=json.loads(Path(r'D:\llm-gateway\private\additional-keys.json').read_text())['sambanova']
body={'model':'gemma-4-31B-it','messages':[{'role':'user','content':'Use get_time tool.'}],'tools':[{'type':'function','function':{'name':'get_time','description':'Get current time','parameters':{'type':'object','properties':{}}}}],'tool_choice':'required','max_tokens':100}
req=urllib.request.Request('https://api.sambanova.ai/v1/chat/completions',data=json.dumps(body).encode(),headers={'Authorization':'Bearer '+k,'Content-Type':'application/json'})
try:
 with urllib.request.urlopen(req,timeout=30) as r:
  d=json.load(r);print('HTTP',r.status,'tool_calls',bool(d['choices'][0]['message'].get('tool_calls')))
except urllib.error.HTTPError as e:
 try:
  d=json.loads(e.read()); err=d.get('error',{});print('HTTP',e.code,'error',str(err).replace(k,'[redacted]')[:200])
 except Exception:print('HTTP',e.code)
except Exception as e:print(type(e).__name__)
