from pathlib import Path
import json,urllib.request
k=json.loads(Path(r'D:\llm-gateway\private\pending-provider-keys.json').read_text())['keys']['cloudflare']
u='https://api.cloudflare.com/client/v4/accounts/f5ef27d87fda5df0ef4c475c3542a351/ai/models/search?per_page=100'
with urllib.request.urlopen(urllib.request.Request(u,headers={'Authorization':'Bearer '+k}),timeout=20) as r:d=json.load(r)
for x in d.get('result',[]):
 if 'text generation' in str(x.get('task',{})).lower() or x.get('name') in ('@cf/meta/llama-3.3-70b-instruct-fp8-fast','@cf/openai/gpt-oss-120b'):
  print(x.get('name'),x.get('task'))
