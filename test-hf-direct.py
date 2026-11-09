from pathlib import Path
import json,urllib.request,urllib.error
key=json.loads(Path(r'D:\llm-gateway\private\additional-keys.json').read_text())['huggingface']
body={'model':'openai/gpt-oss-120b:cheapest','messages':[{'role':'user','content':'Use get_time tool.'}],'tools':[{'type':'function','function':{'name':'get_time','description':'Get current time','parameters':{'type':'object','properties':{}}}}],'tool_choice':'required','max_tokens':100}
req=urllib.request.Request('https://router.huggingface.co/v1/chat/completions',data=json.dumps(body).encode(),headers={'Authorization':'Bearer '+key,'Content-Type':'application/json'})
try:
 with urllib.request.urlopen(req,timeout=40) as r:
  d=json.load(r);print('HTTP',r.status,'tool_calls',bool(d['choices'][0]['message'].get('tool_calls')))
except urllib.error.HTTPError as e:
 try:
  d=json.loads(e.read());error=d.get('error',{});print('HTTP',e.code,'error',str(error).replace(key,'[redacted]')[:350])
 except Exception:print('HTTP',e.code)
except Exception as e:print(type(e).__name__)
