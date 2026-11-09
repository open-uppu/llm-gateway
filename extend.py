from pathlib import Path
import shutil, yaml
p = Path(r'D:\llm-gateway\config.yaml')
shutil.copy2(p, p.with_suffix('.yaml.bak'))
d = yaml.safe_load(p.read_text(encoding='utf-8'))
existing = {x['model_name'] for x in d['model_list']}
models = {
 'local-qwen-14b': ('ollama_chat/qwen2.5:14b', 'http://127.0.0.1:11434'),
 'local-gemma-9b': ('ollama_chat/gemma2:9b', 'http://127.0.0.1:11434'),
 'local-llama-8b': ('ollama_chat/llama3.1:8b', 'http://127.0.0.1:11434'),
 'llm7-deepseek': ('openai/DeepSeek-V4-Flash-0731', 'https://api.llm7.io/v1'),
 'llm7-glm': ('openai/GLM-5.3-Flash', 'https://api.llm7.io/v1'),
 'llm7-codestral': ('openai/codestral-latest', 'https://api.llm7.io/v1'),
 'llm7-minimax': ('openai/minimax-m2.7', 'https://api.llm7.io/v1'),
 'llm7-mistral': ('openai/mistral-Nemo-Instruct-2407', 'https://api.llm7.io/v1'),
 'llm7-nemotron': ('openai/nemotron-3-nano:30b', 'https://api.llm7.io/v1'),
}
for name, (model, base) in models.items():
 if name not in existing:
  params = {'model': model, 'api_base': base}
  if base.startswith('https:'): params['api_key'] = 'unused'
  d['model_list'].append({'model_name': name, 'litellm_params': params})
p.write_text(yaml.safe_dump(d, sort_keys=False), encoding='utf-8')
print('Models configured:', len(d['model_list']))
