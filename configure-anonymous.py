from pathlib import Path
import json,shutil,urllib.request,yaml,datetime
p=Path(r'D:\llm-gateway\config.yaml')
d=yaml.safe_load(p.read_text(encoding='utf-8'))
def catalog(url):
 with urllib.request.urlopen(url,timeout=25) as r: return json.load(r)['data']
kilo=catalog('https://ai-gateway.kilo.ai/api/v1/models')
ovh=catalog('https://oai.endpoints.kepler.ai.cloud.ovh.net/v1/models')
llm7=catalog('https://api.llm7.io/v1/models')
new=[]
for name,model,base in [('kilo/'+x['id'],x['id'],'http://127.0.0.1:4002/kilo') for x in kilo if x.get('isFree') is True]+[('ovh/'+x['id'],x['id'],'http://127.0.0.1:4002/ovh') for x in ovh]+[('llm7/'+x['id'],x['id'],'https://api.llm7.io/v1') for x in llm7 if x.get('tier')=='turbo' and not x.get('usage_based_only') and x.get('model_type')=='chat']:
 new.append({'model_name':name,'litellm_params':{'model':'openai/'+model,'api_base':base,'api_key':'unused'}})
d['model_list']=[x for x in d['model_list'] if not x['model_name'].startswith(('kilo/','ovh/','llm7/')) and x['model_name'] not in ('kilo-liquid','ovh-gpt-oss-20b')] + new
shutil.copy2(p,p.with_name('config.before-catalog-'+datetime.datetime.now().strftime('%Y%m%d-%H%M%S')+'.yaml'))
p.write_text(yaml.safe_dump(d,sort_keys=False,allow_unicode=True),encoding='utf-8')
print('Added:',sum(x['model_name'].startswith('kilo/') for x in new),'Kilo,',sum(x['model_name'].startswith('ovh/') for x in new),'OVH,',sum(x['model_name'].startswith('llm7/') for x in new),'LLM7; total',len(d['model_list']))
