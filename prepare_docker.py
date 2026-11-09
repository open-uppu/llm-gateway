from pathlib import Path
import yaml
root=Path(r'D:\llm-gateway')
data=yaml.safe_load((root/'config.yaml').read_text(encoding='utf-8'))
for entry in data['model_list']:
 p=entry['litellm_params']
 if 'api_base' in p:
  p['api_base']=p['api_base'].replace('http://127.0.0.1:11434','http://host.docker.internal:11434').replace('http://127.0.0.1:4002','http://host.docker.internal:4002')
(root/'config.docker.yaml').write_text(yaml.safe_dump(data,sort_keys=False,allow_unicode=True),encoding='utf-8')
print('Prepared',len(data['model_list']),'model aliases')
