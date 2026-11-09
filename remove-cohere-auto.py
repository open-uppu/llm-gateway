from pathlib import Path
import yaml
p=Path(r'D:\llm-gateway\config.yaml'); d=yaml.safe_load(p.read_text(encoding='utf-8'))
d['model_list']=[e for e in d['model_list'] if not (e['model_name']=='auto' and e['litellm_params'].get('api_key')=='os.environ/COHERE_PROVIDER_KEY')]
p.write_text(yaml.safe_dump(d,sort_keys=False,allow_unicode=True),encoding='utf-8')
print('Auto deployments:',sum(e['model_name']=='auto' for e in d['model_list']))
