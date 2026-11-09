import subprocess,re,collections
r=subprocess.run(['docker','logs','--since','24h','--timestamps','llm-gateway'],capture_output=True,text=True,encoding='utf8',errors='replace')
groups=collections.defaultdict(list)
for line in (r.stdout+'\n'+r.stderr).splitlines():
 m=re.search(r'^(\S+).*?"(GET|POST|PUT|DELETE) ([^ ]+) HTTP/[^"]+" (\d{3})',line)
 if m:
  t,method,path,status=m.groups()
  if status in ('401','404') or path.startswith('/v1/chat/completions'):groups[(method,path,status)].append(t)
for (method,path,status),v in sorted(groups.items()): print(method,path,status,'count',len(v),'last',max(v))
