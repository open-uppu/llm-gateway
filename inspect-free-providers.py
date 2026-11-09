from pathlib import Path
import json,urllib.request,urllib.error
k=json.loads(Path(r'D:\llm-gateway\private\pending-provider-keys.json').read_text())['keys']
def get(url, headers):
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=20) as r: return r.status,json.load(r)
 except urllib.error.HTTPError as e:return e.code,{}
 except Exception as e:return type(e).__name__,{}
status,d=get('https://generativelanguage.googleapis.com/v1beta/models',{'x-goog-api-key':k['gemini']})
print('GEMINI',status,[(m.get('name'),m.get('supportedGenerationMethods',[])) for m in d.get('models',[]) if 'flash' in m.get('name','').lower()][:20])
status,d=get('https://api.cohere.com/v2/models',{'Authorization':'Bearer '+k['cohere']})
print('COHERE',status,[(m.get('name'),m.get('endpoints_supported')) for m in d.get('models',[]) if 'chat' in m.get('endpoints_supported',[])][:25])
status,d=get('https://api.cloudflare.com/client/v4/accounts/f5ef27d87fda5df0ef4c475c3542a351/ai/models/search?per_page=100',{'Authorization':'Bearer '+k['cloudflare']})
print('CLOUDFLARE',status,'success',d.get('success'),'count',len(d.get('result') or []))
