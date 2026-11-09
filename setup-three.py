from pathlib import Path
from copy import deepcopy
import json,yaml,datetime,shutil
root=Path(r'D:\llm-gateway'); secure=root/'private'; keys=json.loads((secure/'groq-aion-keys.json').read_text());keys.update(json.loads((secure/'nvidia-new.json').read_text()))
items=[('groq',['openai/gpt-oss-20b','openai/gpt-oss-120b','qwen/qwen3.8-27b'],'https://api.groq.com/openai/v1','GROQ_PROVIDER_KEY'),('aion',['aion-labs/aion-2.0','aion-labs/aion-3.0','aion-labs/aion-3.0-mini','aion-labs/aion-rp-llama-3.1-8b'],'https://api.aionlabs.ai/v1','AION_PROVIDER_KEY'),('nvidia',['nvidia/nemotron-3.5-bolt-e4b','nvidia/nemotron-3.5-lightning-30b-a3b','google/gemma-4-31b-it'],'https://integrate.api.nvidia.com/v1','NVIDIA_PROVIDER_KEY')]
p=root/'config.yaml'; d=yaml.safe_load(p.read_text(encoding='utf8')); stamp=datetime.datetime.now().strftime('%Y%m%d-%H%M%S');shutil.copy2(p,p.with_name('config.before-three-'+stamp+'.yaml'))
ens={i[3] for i in items}; d['model_list']=[x for x in d['model_list'] if not x['model_name'].startswith(('groq/','aion/','nvidia/')) and not (x['model_name']=='auto' and x['litellm_params'].get('api_key','').replace('os.environ/','') in ens)]
new=[]
for prefix,names,base,env in items:
 for name in names:
  params={'model':'openai/'+name,'api_base':base,'api_key':'os.environ/'+env,'extra_headers':{'User-Agent':'curl/8.7.1'}}
  new.append({'model_name':prefix+'/'+name,'litellm_params':params})
d['model_list'].extend(new)
for name in ('groq/openai/gpt-oss-20b','nvidia/nvidia/nemotron-3.5-bolt-e4b'):
 e=deepcopy(next(x for x in new if x['model_name']==name));e['model_name']='auto';e['litellm_params']['timeout']=45;d['model_list'].append(e)
e=secure/'providers.env';lines=[line for line in e.read_text(encoding='utf8').splitlines() if line.split('=',1)[0] not in ens]
for env,k in [('GROQ_PROVIDER_KEY','groq'),('AION_PROVIDER_KEY','aion'),('NVIDIA_PROVIDER_KEY','nvidia')]:lines.append(env+'='+keys[k])
e.write_text('\n'.join(lines)+'\n',encoding='utf8');p.write_text(yaml.safe_dump(d,sort_keys=False,allow_unicode=True),encoding='utf8')
print('Configured aliases:',len(new),'auto deployments:',sum(x['model_name']=='auto' for x in d['model_list']))
