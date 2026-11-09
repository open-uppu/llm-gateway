from pathlib import Path
import json, urllib.request, yaml, shutil, datetime
root=Path(r'D:\llm-gateway'); private=root/'private'
pending=json.loads((private/'pending-provider-keys.json').read_text(encoding='utf-8'))
key=pending['keys']['openrouter']
req=urllib.request.Request('https://openrouter.ai/api/v1/key',headers={'Authorization':'Bearer '+key})
with urllib.request.urlopen(req,timeout=15) as r: assert r.status==200
with urllib.request.urlopen('https://openrouter.ai/api/v1/models',timeout=20) as r: catalog=json.load(r)['data']
free=[]
for m in catalog:
 p=m.get('pricing',{})
 if m.get('id','').endswith(':free') and p.get('prompt') is not None and p.get('completion') is not None and float(p['prompt'])==0 and float(p['completion'])==0 and 'text' in m.get('architecture',{}).get('output_modalities',[]): free.append(m['id'])
assert free, 'No zero-price free models in live catalog'
p=root/'config.yaml'; cp=root/'compose.yaml'
data=yaml.safe_load(p.read_text(encoding='utf-8')); compose=yaml.safe_load(cp.read_text(encoding='utf-8'))
stamp=datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
for f in (p,cp): shutil.copy2(f,f.with_name(f.name+'.before-openrouter-'+stamp))
models=data['model_list']
models[:]=[x for x in models if not x['model_name'].startswith('openrouter/') and not (x['model_name']=='auto' and x['litellm_params'].get('api_key')=='os.environ/OPENROUTER_API_KEY')]
def entry(name,model): return {'model_name':name,'litellm_params':{'model':'openai/'+model,'api_base':'https://openrouter.ai/api/v1','api_key':'os.environ/OPENROUTER_API_KEY'}}
models.extend(entry('openrouter/'+m,m) for m in free)
models.append(entry('openrouter/free','openrouter/free'))
auto=entry('auto','openrouter/free');auto['litellm_params']['timeout']=45;models.append(auto)
env=compose['services']['gateway']['env_file']
if './private/providers.env' not in env:env.append('./private/providers.env')
providers=private/'providers.env'
if providers.exists():
 lines=providers.read_text(encoding='utf-8').splitlines()
 lines=[line for line in lines if not line.startswith('OPENROUTER_API_KEY=')]
else: lines=[]
lines.append('OPENROUTER_API_KEY='+key)
providers.write_text('\n'.join(lines)+'\n',encoding='utf-8')
p.write_text(yaml.safe_dump(data,sort_keys=False,allow_unicode=True),encoding='utf-8')
cp.write_text(yaml.safe_dump(compose,sort_keys=False,allow_unicode=True),encoding='utf-8')
print('Configured zero-price free model IDs:',len(free),'; added free router to auto; credentials in restricted directory')
