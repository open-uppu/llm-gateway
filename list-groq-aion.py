from pathlib import Path
import json,urllib.request
keys=json.loads(Path(r'D:\llm-gateway\private\groq-aion-keys.json').read_text())
for name,url in [('groq','https://api.groq.com/openai/v1/models'),('aion','https://api.aionlabs.ai/v1/models')]:
 req=urllib.request.Request(url,headers={'Authorization':'Bearer '+keys[name],'User-Agent':'curl/8.7.1'})
 with urllib.request.urlopen(req,timeout=10) as r: print(name, [x.get('id') for x in json.load(r).get('data',[])])
