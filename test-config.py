from pathlib import Path
import shutil,yaml
p=Path(r'D:\llm-gateway\config.yaml'); shutil.copy2(p,p.with_name('config.before-anonymous.yaml'))
d=yaml.safe_load(p.read_text(encoding='utf-8'))
for name,model,base in [('kilo-liquid','liquid/lfm-2.5-2.6b:free','https://ai-gateway.kilo.ai/api/v1'),('ovh-gpt-oss-20b','gpt-oss-20b','https://oai.endpoints.kepler.ai.cloud.ovh.net/v1')]:
 if not any(x['model_name']==name for x in d['model_list']):
  d['model_list'].append({'model_name':name,'litellm_params':{'model':'openai/'+model,'api_base':base,'api_key':'unused','extra_headers':{'Authorization':None}}})
p.write_text(yaml.safe_dump(d,sort_keys=False),encoding='utf-8')
