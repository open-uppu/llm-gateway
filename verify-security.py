import urllib.request,urllib.error,json
from pathlib import Path
def code(url,headers={}):
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=10) as r:return r.status
 except urllib.error.HTTPError as e:return e.code
key=Path(r'D:\llm-gateway\.env').read_text().strip().split('=',1)[1]
print('gateway without key',code('http://127.0.0.1:4000/v1/models'))
print('gateway with key',code('http://127.0.0.1:4000/v1/models',{'Authorization':'Bearer '+key}))
print('anonymous proxy rejects unknown path',code('http://127.0.0.1:4002/other/models'))
print('anonymous proxy rejects unsupported path',code('http://127.0.0.1:4002/kilo/admin'))
