from pathlib import Path
import json,urllib.request,urllib.error
key=json.loads(Path(r'D:\llm-gateway\private\nvidia-new.json').read_text())['nvidia']
body={'model':'openai/gpt-oss-20b','messages':[{'role':'user','content':'Use the get_time tool.'}],'tools':[{'type':'function','function':{'name':'get_time','description':'Get current time','parameters':{'type':'object','properties':{}}}}],'tool_choice':'required','max_tokens':128}
def check(k):
 req=urllib.request.Request('https://integrate.api.nvidia.com/v1/chat/completions',data=json.dumps(body).encode(),headers={'Authorization':'Bearer '+k,'Content-Type':'application/json'})
 try:
  with urllib.request.urlopen(req,timeout=40) as r:
   j=json.load(r);return ('HTTP',r.status,'tool_calls',bool(j.get('choices',[{}])[0].get('message',{}).get('tool_calls')))
 except urllib.error.HTTPError as e:
  try:
   j=json.loads(e.read());er=j.get('error',{});return ('HTTP',e.code,'error',str(er).replace(k,'[redacted]')[:200])
  except Exception:return ('HTTP',e.code)
 except Exception as e:return ('error',type(e).__name__)
print('actual',check(key),flush=True)
print('invalid_control',check('invalid-codex-test-key'),flush=True)
