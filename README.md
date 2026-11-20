# LLM Gateway

OpenAI-compatible LiteLLM gateway for free and anonymous providers. Two containers run from one Compose file: `gateway` (LiteLLM) and `proxy` (Kilo/OVH anonymous endpoints), both with `restart: unless-stopped`.

## Layout

- `docker-compose.yml` — gateway mounts `config.docker.yaml`; proxy is published only on `127.0.0.1:4002` and has a `/health` healthcheck.
- `config.docker.yaml` — configuration used inside the container. Kilo/OVH point at `http://host.docker.internal:4002/...`.
- `config.yaml` — same catalog for running LiteLLM directly on the host (`127.0.0.1:4002`), e.g. without Docker.
- `anonymous-proxy.js` — strips `Authorization` and forwards `/kilo` and `/ovh`. `PROXY_HOST`/`PROXY_PORT` control the listener (default `127.0.0.1:4002`); `GET /health` returns `{"status":"ok"}` without calling upstream.

## Start

1. Install Docker with Compose.
2. Copy `.env.example` to `.env` and set `LITELLM_MASTER_KEY`.
3. Create `private/providers.env` with the provider keys (same names as `.env.example`). Compose loads it as a second `env_file`; directory `private/` is ignored by Git.
4. `docker compose up -d`.

The gateway publishes `127.0.0.1:4000` and `100.105.249.12:4000` (Tailscale). Edit the second mapping in `docker-compose.yml` to your address or remove it.

## Routing

`auto` has three deployments (Groq `gpt-oss-20b`, NVIDIA `nemotron-3.5-bolt-e4b`, OpenRouter `free`) and falls back to `auto-reserve-1` → `auto-reserve-2` → `auto-reserve-3`. Note that `auto-reserve-1` currently duplicates the Groq primary, so a Groq outage burns one redundant fallback hop. Direct model names (e.g. `kilo/...`, `ovh/...`) have no fallback by design: if the proxy or upstream is down the request fails with `No fallback was attempted`.

## Verify

```powershell
docker compose ps
curl http://127.0.0.1:4002/health          # proxy
curl http://127.0.0.1:4000/health/liveliness
```

To prove the fallback chain without touching the live gateway, copy `config.docker.yaml` and point the three `auto` deployments at a dead port, start a second container on another port with that file mounted, and call `auto`. The response should be `200` with `x-litellm-model-group: auto-reserve-1` and `x-litellm-attempted-fallbacks: 1`.

## Notes

- `.env`, `private/`, logs and `config.*.before-*` backups are ignored; do not commit credentials.
- The proxy adds no authentication and is reachable only from the host loopback; keep it that way.
- Images are pinned by digest; update both the digest and the version comment together.
