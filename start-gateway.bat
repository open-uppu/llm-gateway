@echo off
cd /d D:\llm-gateway
set PYTHONUTF8=1
for /f "usebackq delims=" %%a in (".env") do set "%%a"
.venv\Scripts\litellm.exe --config config.yaml --host 127.0.0.1 --port 4000 >> gateway.log 2>&1
