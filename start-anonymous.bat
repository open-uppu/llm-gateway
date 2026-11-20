@echo off
rem The anonymous proxy now runs as the `proxy` service in docker-compose.yml
rem (restart: unless-stopped, healthcheck on http://127.0.0.1:4002/health).
rem This script only starts the host fallback when `.use-host-proxy` exists,
rem so the logon task cannot fight the container for port 4002.
if not exist "%~dp0.use-host-proxy" exit /b 0
cd /d D:\llm-gateway
echo [%date% %time%] starting host fallback proxy >> anonymous.log
node anonymous-proxy.js >> anonymous.log 2>&1
