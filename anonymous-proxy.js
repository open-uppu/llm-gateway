'use strict';
const http = require('node:http');
const https = require('node:https');
const targets = { kilo: 'https://ai-gateway.kilo.ai/api/v1', ovh: 'https://oai.endpoints.kepler.ai.cloud.ovh.net/v1' };
http.createServer((req, res) => {
  const match = /^\/(kilo|ovh)(\/[^?#]*)?(\?[^#]*)?$/.exec(req.url);
  if (!match) { res.writeHead(404).end(); return; }
  const path = match[2] || '';
  if (!['/models', '/chat/completions', '/completions', '/embeddings'].includes(path)) { res.writeHead(404).end(); return; }
  const headers = { ...req.headers };
  delete headers.authorization;
  delete headers.host;
  delete headers['proxy-authorization'];
  const upstream = https.request(targets[match[1]] + path + (match[3] || ''), { method: req.method, headers }, response => {
    res.writeHead(response.statusCode, response.headers);
    response.pipe(res);
  });
  upstream.setTimeout(120000, () => upstream.destroy(new Error('Upstream timeout')));
  upstream.on('error', () => { if (!res.headersSent) res.writeHead(502); res.end(); });
  req.on('aborted', () => upstream.destroy());
  res.on('close', () => { if (!res.writableEnded) upstream.destroy(); });
  req.pipe(upstream);
}).listen(4002, '0.0.0.0');
