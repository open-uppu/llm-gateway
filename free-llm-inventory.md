# รายการ Free LLM APIs และ gateway

ตรวจสอบวันที่ 3 พฤศจิกายน 2026 จาก [awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis); ข้อมูล upstream ระบุอัปเดต 2026-10-25. รายชื่อนี้เป็น snapshot เงื่อนไข รุ่น โควตา และราคาเปลี่ยนได้ ต้องตรวจสอบกับผู้ให้บริการก่อนใช้จริง

Gateway บน Windows: `http://127.0.0.1:4000/v1` หรือจาก Tailscale `http://100.105.249.12:4000/v1`; API key อยู่ใน `D:\llm-gateway\.env`; gateway ทำงานใน Docker ชื่อโมเดลที่ส่งให้ gateway ดูด้านล่าง

## ผู้ให้บริการทั้งหมดใน repo

| ผู้ให้บริการ | เงื่อนไขเริ่มต้น |
|---|---|
| [Aion Labs](https://www.aionlabs.ai/app/api-keys/) | ต้องสมัครและสร้าง API key |
| [Cohere](https://dashboard.cohere.com/api-keys) | ต้องสมัครและสร้าง API key; ข้อจำกัดการใช้งานเชิงพาณิชย์ |
| [Google Gemini](https://aistudio.google.com/app/apikey) | ต้องสมัครและสร้าง API key |
| [Mistral AI](https://console.mistral.ai/api-keys) | ต้องสมัครและสร้าง API key |
| [Z AI (Zhipu AI)](https://open.bigmodel.cn/usercenter/apikeys) | ต้องสมัครและสร้าง API key |
| [Cloudflare Workers AI](https://dash.cloudflare.com/profile/api-tokens) | ต้องสมัคร; ใช้ API token และ account ID |
| [Gonka Broker](https://app.gonkabroker.com/signup) | ต้องสมัครและยืนยันหมายเลขโทรศัพท์ |
| [Groq](https://console.groq.com/keys) | ต้องสมัครและสร้าง API key |
| [Kilo Code](https://app.kilo.ai/profile) | รองรับ anonymous เฉพาะรุ่นฟรี; เพิ่มใน gateway แล้ว |
| [LLM7.io](https://token.llm7.io) | รองรับ anonymous ในบางรุ่น; เพิ่มใน gateway แล้ว |
| [ModelScope](https://modelscope.cn/my/myaccesstoken) | ต้องสมัคร ผูกบัญชี Alibaba Cloud และยืนยันตัวตน |
| [NVIDIA NIM](https://build.nvidia.com/explore/discover) | ต้องสมัคร NVIDIA Developer Program และสร้าง key |
| [OpenRouter](https://openrouter.ai/keys) | ต้องสมัครและสร้าง API key สำหรับการตั้งค่าทั่วไป |
| [OVHcloud AI Endpoints](https://www.ovhcloud.com/en/public-cloud/ai-endpoints/catalog/) | รองรับ anonymous ภายใต้โควตา; เพิ่มใน gateway แล้ว |
| [SiliconFlow](https://cloud.siliconflow.cn/account/ak) | ต้องสมัครและยืนยันตัวตน |

ผู้ให้บริการที่ต้องสมัครยังไม่ได้เชื่อมหรือทดสอบด้วยบัญชีของคุณ; ไม่ควรส่ง API key ในแชต

## เลือกโมเดลอัตโนมัติ

ใช้ชื่อ `auto` ใน Hermes Agent หรือ OpenAI-compatible client โดย gateway จะสุ่มระหว่าง Ollama, OVHcloud, LLM7, Kilo, OpenRouter, Gemini, Cloudflare, SambaNova, Groq และ NVIDIA มีการตั้งค่าให้ลองสลับเมื่อพบข้อผิดพลาดที่รองรับ บางคำขออาจส่งข้อความไปยังผู้ให้บริการออนไลน์; คำตอบและความสามารถแตกต่างกันระหว่างโมเดล

## โมเดลใน gateway

รายการเดิมมี 57 ชื่อ (ปัจจุบันเพิ่มเป็น 92 ชื่อใน API โดยบางชื่ออาจชี้ไปโมเดลเดียวกัน) การปรากฏในรายการไม่ได้รับประกันว่าโมเดลตอบได้ ณ เวลานั้น

### Local Ollama

- `local-qwen` → `ollama_chat/qwen2.5:7b`
- `local-qwen-14b` → `ollama_chat/qwen2.5:14b`
- `local-gemma-9b` → `ollama_chat/gemma2:9b`
- `local-llama-8b` → `ollama_chat/llama3.1:8b`

### Kilo anonymous

- `kilo/kilo-auto/free` → `openai/kilo-auto/free`
- `kilo/nvidia/nemotron-3.5-super-vl:free` → `openai/nvidia/nemotron-3.5-super-vl:free`
- `kilo/reflection/beam-free` → `openai/reflection/beam-free`
- `kilo/stealth/glyph-cluster` → `openai/stealth/glyph-cluster`
- `kilo/recursive/flint-v1.0:free` → `openai/recursive/flint-v1.0:free`
- `kilo/xingchen-agi/xing4.0-29b-a4b:free` → `openai/xingchen-agi/xing4.0-29b-a4b:free`
- `kilo/dots-studio/dots-3-note-preview:free` → `openai/dots-studio/dots-3-note-preview:free`
- `kilo/liquid/lfm-2.5-2.6b:free` → `openai/liquid/lfm-2.5-2.6b:free`
- `kilo/nvidia/nemotron-3.5-lightning:free` → `openai/nvidia/nemotron-3.5-lightning:free`
- `kilo/thinkingmachines/inkling-small:free` → `openai/thinkingmachines/inkling-small:free`
- `kilo/thinkingmachines/inkling:free` → `openai/thinkingmachines/inkling:free`
- `kilo/cohere/north-mini-code:free` → `openai/cohere/north-mini-code:free`
- `kilo/nvidia/nemotron-3.5-content-safety:free` → `openai/nvidia/nemotron-3.5-content-safety:free`
- `kilo/nvidia/nemotron-3-ultra-550b-a55b:free` → `openai/nvidia/nemotron-3-ultra-550b-a55b:free`
- `kilo/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` → `openai/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
- `kilo/google/gemma-4-31b-it:free` → `openai/google/gemma-4-31b-it:free`
- `kilo/openrouter/free` → `openai/openrouter/free`

### OVH anonymous

- `ovh/Qwen3.8-27B` → `openai/Qwen3.8-27B`
- `ovh/Qwen3.5-397B-A17B` → `openai/Qwen3.5-397B-A17B`
- `ovh/Qwen3.5-9B` → `openai/Qwen3.5-9B`
- `ovh/gpt-oss-20b` → `openai/gpt-oss-20b`
- `ovh/gpt-oss-120b` → `openai/gpt-oss-120b`
- `ovh/Meta-Llama-3_3-70B-Instruct` → `openai/Meta-Llama-3_3-70B-Instruct`
- `ovh/Qwen3Guard-Gen-8B` → `openai/Qwen3Guard-Gen-8B`
- `ovh/Qwen2.5-VL-72B-Instruct` → `openai/Qwen2.5-VL-72B-Instruct`
- `ovh/Mistral-Small-3.2-24B-Instruct-2506` → `openai/Mistral-Small-3.2-24B-Instruct-2506`
- `ovh/Mistral-Nemo-Instruct-2407` → `openai/Mistral-Nemo-Instruct-2407`
- `ovh/Qwen3Guard-Gen-0.6B` → `openai/Qwen3Guard-Gen-0.6B`
- `ovh/Qwen3.6-27B` → `openai/Qwen3.6-27B`
- `ovh/whisper-large-v3-turbo` → `openai/whisper-large-v3-turbo`
- `ovh/whisper-large-v3` → `openai/whisper-large-v3`
- `ovh/stable-diffusion-xl-base-v10` → `openai/stable-diffusion-xl-base-v10`
- `ovh/bge-m3` → `openai/bge-m3`
- `ovh/Qwen3-Embedding-8B` → `openai/Qwen3-Embedding-8B`
- `ovh/bge-multilingual-gemma2` → `openai/bge-multilingual-gemma2`
- `ovh/nvr-tts-en-us` → `openai/nvr-tts-en-us`
- `ovh/nvr-tts-de-de` → `openai/nvr-tts-de-de`
- `ovh/nvr-tts-es-es` → `openai/nvr-tts-es-es`
- `ovh/nvr-tts-it-it` → `openai/nvr-tts-it-it`

### LLM7 anonymous

- `llm7/DeepSeek-V4-Flash-0731` → `openai/DeepSeek-V4-Flash-0731`
- `llm7/GLM-5.3-Flash` → `openai/GLM-5.3-Flash`
- `llm7/codestral-latest` → `openai/codestral-latest`
- `llm7/gpt-oss:20b` → `openai/gpt-oss:20b`
- `llm7/minimax-m2.7` → `openai/minimax-m2.7`
- `llm7/mistral-Nemo-Instruct-2407` → `openai/mistral-Nemo-Instruct-2407`
- `llm7/nemotron-3-nano:30b` → `openai/nemotron-3-nano:30b`

### ชื่อเดิมที่ยังใช้งานได้

- `cloud-llm7` → `openai/gpt-oss:20b`
- `llm7-deepseek` → `openai/DeepSeek-V4-Flash-0731`
- `llm7-glm` → `openai/GLM-5.3-Flash`
- `llm7-codestral` → `openai/codestral-latest`
- `llm7-minimax` → `openai/minimax-m2.7`
- `llm7-mistral` → `openai/mistral-Nemo-Instruct-2407`
- `llm7-nemotron` → `openai/nemotron-3-nano:30b`

## โมเดลที่ repo ระบุ แยกตามผู้ให้บริการ

ชื่อด้านล่างเป็นข้อมูลใน repo ไม่ใช่ชื่อที่เรียกผ่าน gateway ได้ทุกตัว โดยเฉพาะตัวที่ยังต้องสมัคร; บางชื่อเป็นชื่อแสดงผลและอาจไม่ใช่ model ID สำหรับ API

### Aion Labs

Permanent free tier, no credit card required. 15 RPM, 20K tokens/day. Specialized for roleplay and storytelling.

API base: `https://api.aionlabs.ai/v1`

- `aion-labs/aion-2.0` — 128K context; 15 RPM, 20K TPD
- `aion-labs/aion-rp-llama-3.1-8b` — 32K context; 15 RPM, 20K TPD
- `aion-labs/aion-3.0` — 128K context; 15 RPM, 20K TPD
- `aion-labs/aion-3.0-mini` — 128K context; 15 RPM, 20K TPD

### Cohere

Free "Trial" API key, no credit card. 1,000 API calls/month. Non-commercial use only.

API base: `https://api.cohere.com/v2`

- `command-a-plus-05-2026` — 128K context; 20 RPM
- `command-a-03-2025` — 256K context; 20 RPM
- `command-r-plus-08-2024` — 128K context; 20 RPM
- `command-r-08-2024` — 128K context; 20 RPM
- `command-r7b-12-2024` — 128K context; 20 RPM
- `command-a-reasoning-08-2025` — 256K context; 20 RPM
- `command-a-translate-08-2025` — 8K context; 20 RPM
- `command-a-vision-07-2025` — 128K context; 20 RPM
- `command-r7b-arabic-02-2025` — 128K context; 20 RPM
- `c4ai-aya-expanse-32b` — 128K context; 20 RPM
- `c4ai-aya-vision-32b` — 16K context; 20 RPM

### Google Gemini

Free tier, no credit card. Free-tier prompts may be used by Google to improve products.

API base: `https://generativelanguage.googleapis.com/v1beta`

- `gemini-3.8-flash` — 1M context; —
- `gemini-3.6-flash` — 1M context; —
- `gemini-3.5-flash-lite` — 1M context; —
- `gemini-3.1-flash-lite` — 1M context; —
- `gemini-2.5-flash` — 1M context; —
- `gemini-2.5-flash-lite` — 1M context; —
- `gemma-4-31b-it` — 256K context; —
- `gemma-4-26b-a4b-it` — 256K context; —

### Mistral AI

Free mode, enabled by default, no credit card required. Free-mode prompts may be used to train Mistral models unless you opt out.

API base: `https://api.mistral.ai/v1`

- `mistral-medium-3-5` — 256K context; ~1 RPS, 500K TPM
- `mistral-small-2603` — 256K context; ~1 RPS, 500K TPM
- `mistral-large-2512` — 256K context; ~1 RPS, 500K TPM
- `ministral-8b-2512` — 256K context; ~1 RPS, 500K TPM
- `codestral-2508` — 128K context; ~1 RPS, 500K TPM
- `ministral-3b-2512` — 256K context; ~1 RPS, 500K TPM
- `ministral-14b-2512` — 256K context; ~1 RPS, 500K TPM

### Z AI (Zhipu AI)

Permanent free models, no credit card required.

API base: `https://open.bigmodel.cn/api/paas/v4`

- `glm-4.7-flash` — 200K context; 1 concurrent request
- `glm-4.5-flash` — 128K context; 1 concurrent request
- `glm-4.6v-flash` — 128K context; 1 concurrent request

### Cloudflare Workers AI

10,000 Neurons/day free, no credit card required. 60+ models available on the free tier.

API base: `https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run`

- `@cf/meta/llama-3.3-70b-instruct-fp8-fast` — 24K context; 10K neurons/day (shared)
- `@cf/meta/llama-4-scout-17b-16e-instruct` — 131K context; 10K neurons/day (shared)
- `@cf/openai/gpt-oss-120b` — 128K context; 10K neurons/day (shared)
- `@cf/google/gemma-4-26b-a4b-it` — 256K context; 10K neurons/day (shared)
- `@cf/zai-org/glm-4.7-flash` — 131K context; 10K neurons/day (shared)
- `@cf/mistralai/mistral-small-3.1-24b-instruct` — 128K context; 10K neurons/day (shared)
- `@cf/deepseek-ai/deepseek-r1-distill-qwen-32b` — 80K context; 10K neurons/day (shared)
- `+ 55 more models` — Varies context; 10K neurons/day (shared)

### Gonka Broker

Permanent free tier, no credit card required; phone verification required. ~1M tokens/month (shared, varies by model), resets monthly. Model lineup rotates with network governance — live list at /v1/models.

API base: `https://proxy.gonkabroker.com/v1`

- `MiniMaxAI/MiniMax-M2.7` — 200K context; ~1M tokens/month (shared, varies by model)
- `deepseek-ai/DeepSeek-V4-Flash-0731` — 400K context; ~1M tokens/month (shared, varies by model)
- `zai-org/GLM-5.3-Flash` — 400K context; ~1M tokens/month (shared, varies by model)
- `BAAI/bge-m3` — 8K context; ~1M tokens/month (shared, varies by model)

### Groq

Free tier, no credit card. Ultra-fast LPU inference.

API base: `https://api.groq.com/openai/v1`

- `openai/gpt-oss-120b` — 131K context; 30 RPM, 1,000 RPD
- `openai/gpt-oss-20b` — 131K context; 30 RPM, 1,000 RPD
- `qwen/qwen3.8-27b` — 131K context; 30 RPM, 1,000 RPD

### Kilo Code

Free models with no credit card and no API key required. `kilo-auto/free` auto-router dynamically routes to models in the free pool.

API base: `https://api.kilo.ai/api/gateway`

- `nvidia/nemotron-3-ultra-550b-a55b:free` — 1M context; 200 req/hr
- `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` — 256K context; 200 req/hr
- `cohere/north-mini-code:free` — 256K context; 200 req/hr
- `openrouter/free` — Varies context; 200 req/hr
- `nvidia/nemotron-3.5-lightning:free` — 1M context; 200 req/hr
- `liquid/lfm-2.5-2.6b:free` — 64K context; 200 req/hr
- `kilo-auto/free` — 256K context; 200 req/hr
- `dots-studio/dots-3-note-preview:free` — 512K context; 200 req/hr
- `recursive/flint-v1.0:free` — 262K context; 200 req/hr
- `xingchen-agi/xing4.0-29b-a4b:free` — 262K context; 200 req/hr
- `nvidia/nemotron-3.5-super-vl:free` — 1M context; 200 req/hr
- `reflection/beam-free` — 1M context; 200 req/hr
- `stealth/glyph-cluster` — 256K context; 200 req/hr

### LLM7.io

API gateway with a free tier. Anonymous access needs no key and reaches the `turbo` models; a free token from token.llm7.io raises the rate and token limits but reaches the same models.

API base: `https://api.llm7.io/v1`

- `gpt-oss:20b` — 128K context; 60 RPM, 250 req/hr (free token)
- `mistral-Nemo-Instruct-2407` — 128K context; 60 RPM, 250 req/hr (free token)
- `nemotron-3-nano:30b` — 1M context; 60 RPM, 250 req/hr (free token)
- `codestral-latest` — 32K context; 60 RPM, 250 req/hr (free token)

### ModelScope

Free API-Inference for registered users. Requires Alibaba Cloud account binding + real-name verification.

API base: `https://api-inference.modelscope.cn/v1`

- `Qwen/Qwen3.5-35B-A3B` — 256K context; 2,000 RPD total; <=500 RPD/model (dynamic)
- `Qwen/Qwen3.5-27B` — 256K context; 2,000 RPD total; <=500 RPD/model (dynamic)
- `+ API-Inference-enabled models` — Varies context; Dynamic quotas + dynamic concurrency

### NVIDIA NIM

Free with NVIDIA Developer Program membership. 100+ models. Rate-limited per model.

API base: `https://integrate.api.nvidia.com/v1`

- `google/gemma-4-31b-it` — 262K context; 40 RPM, 10,000 RPD
- `nvidia/nemotron-3-ultra-550b-a55b` — 1M context; 40 RPM, 10,000 RPD
- `openai/gpt-oss-20b` — 131K context; 40 RPM, 10,000 RPD
- `+ 92 more models` — Varies context; 40 RPM, 10,000 RPD

### OpenRouter

17 free models (marked with `:free` suffix). OpenAI SDK-compatible.

API base: `https://openrouter.ai/api/v1`

- `cohere/north-mini-code:free` — 256K context; 20 RPM, 50 RPD
- `google/gemma-4-26b-a4b-it:free` — 262K context; 20 RPM, 50 RPD
- `google/gemma-4-31b-it:free` — 262K context; 20 RPM, 50 RPD
- `dots-studio/dots-3-note-preview:free` — 512K context; 20 RPM, 50 RPD
- `liquid/lfm-2.5-2.6b:free` — 64K context; 20 RPM, 50 RPD
- `nvidia/nemotron-3.5-lightning:free` — 1M context; 20 RPM, 50 RPD
- `thinkingmachines/inkling:free` — 1M context; 20 RPM, 50 RPD
- `nvidia/nemotron-3-ultra-550b-a55b:free` — 1M context; 20 RPM, 50 RPD
- `recursive/flint-v1.0:free` — 262K context; 20 RPM, 50 RPD
- `xingchen-agi/xing4.0-29b-a4b:free` — 262K context; 20 RPM, 50 RPD
- `nvidia/nemotron-3.5-super-vl:free` — 1M context; 20 RPM, 50 RPD
- `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` — 256K context; 20 RPM, 50 RPD
- `thinkingmachines/inkling-small:free` — 1M context; 20 RPM, 50 RPD

### OVHcloud AI Endpoints

Free anonymous tier (no API key, no signup): 2 RPM per IP per model. 20+ open-weight models hosted in EU. OpenAI SDK-compatible.

API base: `https://oai.endpoints.kepler.ai.cloud.ovh.net/v1`

- `Qwen3.5-397B-A17B` — 262K context; 2 RPM (anonymous)
- `gpt-oss-120b` — 131K context; 2 RPM (anonymous)
- `gpt-oss-20b` — 131K context; 2 RPM (anonymous)
- `Meta-Llama-3_3-70B-Instruct` — 131K context; 2 RPM (anonymous)
- `Qwen3.8-27B` — 262K context; 2 RPM (anonymous)
- `Qwen3.6-27B` — 262K context; 2 RPM (anonymous)
- `Qwen3.5-9B` — 262K context; 2 RPM (anonymous)
- `Qwen2.5-VL-72B-Instruct` — 32K context; 2 RPM (anonymous)
- `Mistral-Small-3.2-24B-Instruct-2506` — 128K context; 2 RPM (anonymous)
- `Mistral-Nemo-Instruct-2407` — 118K context; 2 RPM (anonymous)

### SiliconFlow

Permanently free models, no credit card required. Identity verification required. 100+ models in the catalog, most of them paid.

API base: `https://api.siliconflow.cn/v1`

- `tencent/Hunyuan-MT-7B` — — context; —
- `XingChenAGI/Xing4.0-29B` — — context; —

## ข้อจำกัดและข้อมูลส่วนบุคคล

- โมเดลออนไลน์ส่งข้อความออกจากเครื่องไปยังผู้ให้บริการ; ตรวจสอบนโยบายข้อมูลและไม่ส่งข้อมูลลับถ้ายังไม่ยอมรับเงื่อนไข
- [Kilo ระบุ](https://kilo.ai/docs/gateway/models-and-providers) ว่า auto/free อาจส่งต่อข้อความไปยังผู้ให้บริการที่บันทึกหรือนำไปปรับปรุงบริการ และ NVIDIA free มีเงื่อนไข trial; ไม่ควรส่งข้อมูลส่วนบุคคลหรือข้อมูลลับ
- การทดสอบ ณ เวลาจัดทำ: Ollama, LLM7, OVH และ Kilo บางรุ่นตอบกลับผ่าน gateway; Kilo บางรุ่นได้รับ HTTP 429 หรือ 503 ไม่ได้รับประกันการใช้งานทุกโมเดล
- Anonymous proxy อยู่ที่ 127.0.0.1:4002 ผ่าน Windows Scheduled Task และ gateway อยู่ใน Docker โดยเปิดพอร์ตบน 127.0.0.1 และ 100.105.249.12; ต้องให้ Docker Desktop และ Windows Scheduled Task เริ่มทำงานก่อน
- อัปเดตรายการ anonymous ด้วย `D:\llm-gateway\configure-anonymous.py` แล้วรัน `D:\llm-gateway\.venv\Scripts\python.exe D:\llm-gateway\prepare_docker.py` และ `docker compose -f D:\llm-gateway\compose.yaml restart` เพื่อโหลดรายการใหม่; สคริปต์สร้าง alias ที่ขึ้นต้น `kilo/`, `ovh/`, `llm7/` ใหม่

## อัปเดต 5 พฤศจิกายน 2026

- เพิ่ม `openrouter/free` และโมเดล OpenRouter ที่ระบุ `:free` พร้อมราคา input/output เป็นศูนย์ 12 รุ่น
- เพิ่ม `openrouter/free` เข้า `auto`; ทดสอบการตอบข้อความและการเรียกเครื่องมือสำเร็จ
- เปิดใช้งานโดยใช้ key ในไฟล์ `D:\llm-gateway\private\providers.env` ซึ่งจำกัดสิทธิ์ที่ระดับโฟลเดอร์
- Gemini, Mistral, Cohere และ Gonka ยืนยัน key กับ endpoint ที่ต้องยืนยันตัวตนแล้ว แต่ยังไม่เพิ่มคำขอที่อาจคิดเงินจนกว่าจะทราบแพ็กเกจบัญชี
- Cloudflare token ผ่านการตรวจสอบ แต่ยังต้องใช้ Account ID; NVIDIA ตรวจ key จาก model catalog ไม่ได้; Groq และ Aion ได้ HTTP 403

## อัปเดต 5 พฤศจิกายน 2026: Gemini, Cohere และ Cloudflare

- เพิ่ม Gemini 4 ชื่อ, Cohere Trial 11 ชื่อ และ Cloudflare Workers Free 6 ชื่อ พร้อมเพิ่ม Gemini และ Cloudflare เข้า `auto`
- ตัวอย่างโมเดล: `google/gemini-3.5-flash-lite`, `cohere/command-a-plus-05-2026`, `cloudflare/@cf/openai/gpt-oss-20b`
- ทดสอบข้อความทั้งสามบริการผ่าน gateway สำเร็จ; Gemini และ Cloudflare ผ่านการทดสอบเรียกเครื่องมือ
- Cohere ไม่รองรับ tool_choice=required ในรุ่นที่ทดสอบ จึงไม่ใส่ใน `auto`
- Gemini Free อาจใช้ข้อความปรับปรุงบริการ และ Cohere Trial มีข้อจำกัดการใช้เชิงพาณิชย์

## อัปเดต 5 พฤศจิกายน 2026: SambaNova

- เพิ่ม SambaNova 4 โมเดลและเพิ่ม `sambanova/gemma-4-31B-it` เข้า `auto`; ทดสอบแชตและการเรียกเครื่องมือผ่าน gateway สำเร็จ
- SambaNova ใช้เครดิตทดลอง ไม่ใช่โควตาฟรีถาวร: คำขอ auto อาจใช้เครดิตหมดเร็วกว่าการเลือกโมเดลโดยตรง
- Hugging Face ตอบ HTTP 402 ให้ซื้อเครดิต จึงยังไม่เพิ่มใน gateway; Cerebras ตอบ HTTP 403 แม้ลองแบบไม่ส่ง key

## อัปเดต 5 พฤศจิกายน 2026: Groq, Aion และ NVIDIA

- เพิ่ม Groq 3 รุ่น, Aion 4 รุ่น และ NVIDIA NIM 3 รุ่น
- เพิ่ม `groq/openai/gpt-oss-20b` และ `nvidia/nvidia/nemotron-3.5-bolt-e4b` เข้า auto; ทดสอบ tool calls ผ่าน gateway สำเร็จ
- Aion ทดสอบแชตสำเร็จ แต่รุ่นที่ลองไม่ส่ง tool call จึงให้เลือกโดยตรงและยังไม่ใส่ใน auto
- NVIDIA ใช้เครดิตฟรีทดลองซึ่งมีจำกัด ควรตรวจยอดและค่าใช้จ่ายเมื่อหมดเครดิต
