# LLM Gateway

An OpenAI-compatible LiteLLM gateway for agent harnesses. Docker Compose starts the gateway and an internal proxy for the Kilo and OVH anonymous endpoints. The configuration is based on the gateway deployed on 8 November 2026; the provider catalogs and free quotas can change.

## Start

1. Install Docker with Compose. Copy `.env.example` to `.env`.
2. Set a strong `LITELLM_MASTER_KEY` and the API keys for the providers you use. The `auto` group currently uses Groq, NVIDIA NIM, and OpenRouter Free, with explicit fallbacks. NVIDIA uses trial credits, which can run out. Do not enable paid billing unless intended.
3. For Cloudflare models, set `CLOUDFLARE_API_BASE` to the Workers AI OpenAI-compatible endpoint containing your account ID and set its provider key.
4. Run `docker compose up -d`. The default endpoint is `http://127.0.0.1:4000/v1`. To stop, run `docker compose down`.

`.env` is local and ignored by Git. Leave unused provider keys blank; their models will not work until configured. Existing model aliases are retained as a snapshot, not a guarantee that every upstream endpoint is currently available. The local Ollama aliases require an Ollama service on the Docker host at port 11434 and the corresponding models installed. Docker Desktop resolves `host.docker.internal`; other hosts may require additional host routing.

To expose the API to a Tailscale address, set `GATEWAY_BIND_ADDRESS` to that machine's address in `.env` and recreate the service. The example binds to localhost only. The HTTP endpoint is not encrypted; restrict access to trusted networks and protect the master key.

## Agent harness

Use OpenAI-compatible chat completions with base URL `http://127.0.0.1:4000/v1`, model `auto`, and the master key as the API key. A harness on another machine must use the gateway host address and an appropriate bind address. `auto` supports streaming and tool calling with the tested providers, but provider capability, availability, model context sizes, and quotas can differ. Retry/fallback is bounded; a failure after streaming has started or an outage across all providers may still interrupt a request.

## Configuration

- `compose.yaml`: pinned LiteLLM and Node images; only the gateway publishes a port.
- `config.yaml`: LiteLLM model aliases, `auto` routing and fallback settings. Provider credentials and the Cloudflare endpoint are environment references.
- `anonymous-proxy.js`: strips authorization headers before forwarding supported Kilo/OVH requests. It is reachable only on the Compose network by default.

This repository is a portable configuration, not an automatic update to any existing deployment. Back up existing config before replacing it. Do not commit credentials, environment files, logs, or live provider exports.
