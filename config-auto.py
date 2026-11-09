from pathlib import Path
from copy import deepcopy
import datetime, shutil, yaml
root=Path(r'D:\llm-gateway')
p=root/'config.yaml'
data=yaml.safe_load(p.read_text(encoding='utf-8'))
sources=['local-qwen','ovh/gpt-oss-20b','llm7/gpt-oss:20b','kilo/cohere/north-mini-code:free']
by_name={e['model_name']:e for e in data['model_list']}
assert all(name in by_name for name in sources), 'Missing source model'
backup=root/('config.before-auto-'+datetime.datetime.now().strftime('%Y%m%d-%H%M%S')+'.yaml')
shutil.copy2(p,backup)
data['model_list']=[e for e in data['model_list'] if e['model_name']!='auto']
for name in sources:
 entry=deepcopy(by_name[name]); entry['model_name']='auto'; entry['litellm_params']['timeout']=45
 data['model_list'].append(entry)
data.setdefault('router_settings',{}).update({'routing_strategy':'simple-shuffle','enable_weighted_failover':True,'num_retries':2,'max_fallbacks':3})
p.write_text(yaml.safe_dump(data,sort_keys=False,allow_unicode=True),encoding='utf-8')
print('auto sources:', ', '.join(sources))
print('backup:',backup.name)
