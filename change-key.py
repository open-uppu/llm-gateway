from pathlib import Path
import yaml
p=Path(r'D:\llm-gateway\config.yaml'); d=yaml.safe_load(p.read_text())
for m in d['model_list']:
 if m['model_name'] in ('kilo-liquid','ovh-gpt-oss-20b'):
  m['litellm_params'].pop('extra_headers',None); m['litellm_params']['api_key']=''
p.write_text(yaml.safe_dump(d,sort_keys=False))
