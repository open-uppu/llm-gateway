import json,urllib.request,urllib.error,concurrent.futures
cases=[('kilo','https://ai-gateway.kilo.ai/api/v1','liquid/lfm-2.5-2.6b:free'),('ovh','https://oai.endpoints.kepler.ai.cloud.ovh.net/v1','gpt-oss-20b')]
def run(item):
 name,base,model=item
 data=json.dumps({'model':model,'messages':[{'role':'user','content':'Reply OK'}],'max_tokens':120}).encode()
 req=urllib.request.Request(base+'/chat/completions',data=data,headers={'Content-Type':'application/json','Authorization':''})
 try:
  with urllib.request.urlopen(req,timeout=35) as r:
   j=json.load(r); return name+' '+str(r.status)+' '+repr(j.get('choices',[{}])[0].get('message',{}).get('content',''))[:120]
 except urllib.error.HTTPError as e: return name+' HTTP '+str(e.code)+' '+e.read(300).decode(errors='replace')
 except Exception as e: return name+' '+str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 for result in pool.map(run,cases):print(result,flush=True)
