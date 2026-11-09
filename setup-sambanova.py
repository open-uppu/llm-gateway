from pathlib import Path
from copy import deepcopy
import json,urllib.request,yaml,datetime,shutil
root=Path(r'D:\llm-gateway');secure=root/'private';keys=json.loads((secure/'additional-keys.json').read_text(encoding='utf8')); key=keys['sambanova']
with urllib.request.urlopen('https://api.sambanova.ai/v1/models',timeout=15) as r: models=json.load(r)['data']
names=[m['id'] for m in models if m.get('id')]
assert 'gemma-4-31B-it' in names
p=root/'config.yaml';d=yaml.safe_load(p.read_text(encoding='utf8'));stamp=datetime.datetime.now().strftime('%Y%m%d-%H%M%S');shutil.copy2(p,p.with_name('config.before-sambanova-'+stamp+'.yaml'))
d['model_list']=[m for m in d['model_list'] if not m['model_name'].startswith('sambanova/') and not (m['model_name']=='auto' and m['litellm_params'].get('api_key')=='os.environ/SAMBANOVA_PROVIDER_KEY')]
def model(name):return {'model_name':'sambanova/'+name,'litellm_params':{'model':'openai/'+name,'api_base':'https://api.sambanova.ai/v1','api_key':'os.environ/SAMBANOVA_PROVIDER_KEY'}}
d['model_list'].extend(model(n) for n in names)
auto=deepcopy(model('gemma-4-31B-it'));auto['model_name']='auto';auto['litellm_params']['timeout']=45;d['model_list'].append(auto)
e=secure/'providers.env'; lines=[s for s in e.read_text(encoding='utf8').splitlines() if not s.startswith('SAMBANOVA_PROVIDER_KEY=')];lines.append('SAMBANOVA_PROVIDER_KEY='+key);e.write_text('\n'.join(lines)+'\n',encoding='utf8')
p.write_text(yaml.safe_dump(d,sort_keys=False,allow_unicode=True),encoding='utf8')
print('SambaNova model aliases',len(names),'auto sources',sum(m['model_name']=='auto' for m in d['model_list']))
