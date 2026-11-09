from pathlib import Path
import json, urllib.request, time
key = Path(r'D:\llm-gateway\.env').read_text().strip().split('=', 1)[1]
headers = {'Authorization': 'Bearer ' + key, 'Content-Type':'application/json'}
for _ in range(20):
 try:
  req = urllib.request.Request('http://127.0.0.1:4000/v1/models',headers=headers)
  with urllib.request.urlopen(req, timeout=3) as r: print('MODELS:', ', '.join(x['id'] for x in json.load(r)['data']))
  break
 except Exception: time.sleep(2)
else: raise SystemExit('gateway did not start')
for model in ['local-qwen','llm7-glm','llm7-deepseek']:
 try:
  body=json.dumps({'model':model,'messages':[{'role':'user','content':'Say OK'}],'max_tokens':256}).encode()
  req=urllib.request.Request('http://127.0.0.1:4000/v1/chat/completions',data=body,headers=headers)
  with urllib.request.urlopen(req,timeout=75) as r: print(model, repr(json.load(r)['choices'][0]['message']['content']))
 except Exception as e: print(model, 'FAILED', str(e))
