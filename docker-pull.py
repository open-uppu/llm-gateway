import os,subprocess,tempfile
with tempfile.TemporaryDirectory(prefix='codex-docker-') as d:
 env=os.environ.copy(); env['PATH']=r'C:\Windows\System32;C:\Windows'
 cmd=[r'C:\Users\theup\AppData\Local\Programs\DockerDesktop\resources\bin\docker.exe','--config',d,'pull','ghcr.io/berriai/litellm:main-stable']
 raise SystemExit(subprocess.call(cmd,env=env))
