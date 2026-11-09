import collections,re,subprocess
p=subprocess.run(['docker','logs','--since','24h','--timestamps','llm-gateway'],capture_output=True,text=True,encoding='utf8',errors='replace')
s=p.stdout+'\n'+p.stderr
counts=collections.Counter(); endpoints=collections.Counter(); problems=collections.Counter(); last=None
for line in s.splitlines():
 m=re.search(r'^(\S+).*?"(GET|POST|PUT|DELETE) ([^ ]+) HTTP/[^"]+" (\d{3})',line)
 if m:
  date,method,path,status=m.groups();counts[status]+=1; endpoints[(method,path,status)]+=1
  if path.startswith('/v1/chat/completions'):last=date
 for label,pattern in [('rate_limit',r'RateLimitError|HTTP 429'),('timeout',r'TimeoutError|timed out'),('server_error',r'InternalServerError|ServiceUnavailableError'),('auth_failure',r'No api key passed|auth_exception_handler'),('connection',r'APIConnectionError|connection refused')]:
  if re.search(pattern,line,re.I): problems[label]+=1
print('log command:',p.returncode)
print('HTTP status counts:',dict(counts))
print('API route counts:',[(a,b,c,n) for (a,b,c),n in endpoints.items() if b.startswith('/v1/')])
print('error indicators (log lines, not requests):',dict(problems))
print('last chat request UTC:',last or 'none')
