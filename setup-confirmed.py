from pathlib import Path
from copy import deepcopy
import json,urllib.request,yaml,datetime,shutil
root=Path(r'D:\llm-gateway'); secure=root/'private'; keys=json.loads((secure/'pending-provider-keys.json').read_text())['keys']
account='f5ef27d87fda5df0ef4c475c3542a351'
req=urllib.request.Request('https://api.cohere.com/v2/models',headers={'Authorization':'Bearer '+keys['cohere']})
with urllib.request.urlopen(req,timeout=20) as r: cohere=json.load(r)['models']
req=urllib.request.Request('https://api.cloudflare.com/client/v4/accounts/'+account+'/ai/models/search?per_page=100',headers={'Authorization':'Bearer '+keys['cloudflare']})
with urllib.request.urlopen(req,timeout=20) as r: cf=json.load(r)
assert cf.get('success') is True
available={m['name'] for m in cf['result']}
cf_names=['@cf/openai/gpt-oss-20b','@cf/openai/gpt-oss-120b','@cf/meta/llama-3.3-70b-instruct-fp8-fast','@cf/meta/llama-4-scout-17b-16e-instruct','@cf/google/gemma-4-26b-a4b-it','@cf/mistralai/mistral-small-3.1-24b-instruct']
cf_names=[m for m in cf_names if m in available]
cohere_names=[m['name'] for m in cohere if 'chat' in m.get('endpoints',[])]
gemini_names=['gemini-3.8-flash','gemini-3.5-flash','gemini-3.5-flash-lite','gemini-2.5-flash-lite']
def entry(name,model,base,env):return {'model_name':name,'litellm_params':{'model':'openai/'+model,'api_base':base,'api_key':'os.environ/'+env}}
entries=[entry('google/'+m,m,'https://generativelanguage.googleapis.com/v1beta/openai','GEMINI_PROVIDER_KEY') for m in gemini_names]
entries += [entry('cohere/'+m,m,'https://api.cohere.ai/compatibility/v1','COHERE_PROVIDER_KEY') for m in cohere_names]
entries += [entry('cloudflare/'+m,m,'https://api.cloudflare.com/client/v4/accounts/'+account+'/ai/v1','CLOUDFLARE_PROVIDER_KEY') for m in cf_names]
assert len(cf_names)>0 and len(cohere_names)>0
p=root/'config.yaml';data=yaml.safe_load(p.read_text(encoding='utf-8')); stamp=datetime.datetime.now().strftime('%Y%m%d-%H%M%S');shutil.copy2(p,p.with_name('config.before-confirmed-'+stamp+'.yaml'))
models=data['model_list']; envnames={'GEMINI_PROVIDER_KEY','COHERE_PROVIDER_KEY','CLOUDFLARE_PROVIDER_KEY'}
models[:]=[x for x in models if not x['model_name'].startswith(('google/','cohere/','cloudflare/')) and not (x['model_name']=='auto' and x['litellm_params'].get('api_key','').replace('os.environ/','') in envnames)]
models.extend(entries)
for name in ['google/gemini-3.5-flash-lite','cohere/command-a-plus-05-2026','cloudflare/@cf/openai/gpt-oss-20b']:
 model=next(x for x in entries if x['model_name']==name)
 copy=deepcopy(model);copy['model_name']='auto';copy['litellm_params']['timeout']=45;models.append(copy)
envfile=secure/'providers.env'; lines=[x for x in envfile.read_text(encoding='utf-8').splitlines() if x.split('=',1)[0] not in envnames]
for n,k in [('GEMINI_PROVIDER_KEY','gemini'),('COHERE_PROVIDER_KEY','cohere'),('CLOUDFLARE_PROVIDER_KEY','cloudflare')]: lines.append(n+'='+keys[k])
envfile.write_text('\n'.join(lines)+'\n',encoding='utf-8');p.write_text(yaml.safe_dump(data,sort_keys=False,allow_unicode=True),encoding='utf-8')
print('Configured Gemini',len(gemini_names),'Cohere',len(cohere_names),'Cloudflare',len(cf_names),'auto sources',sum(x['model_name']=='auto' for x in models))
