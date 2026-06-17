const http = require('http');
const fs = require('fs');
const path = require('path');
const { URL } = require('url');

const ROOT = __dirname;
const HOST = '127.0.0.1';
const PORT = Number(process.env.BTCC_PORT || 8080);
const STATE_FILE = path.join(ROOT, 'data', 'persisted_state.json');

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.md': 'text/markdown; charset=utf-8',
  '.txt': 'text/plain; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.webp': 'image/webp',
  '.pdf': 'application/pdf',
  '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
  '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
};

function ensureStateFile() {
  if (!fs.existsSync(path.dirname(STATE_FILE))) {
    fs.mkdirSync(path.dirname(STATE_FILE), { recursive: true });
  }
  if (!fs.existsSync(STATE_FILE)) {
    fs.writeFileSync(STATE_FILE, '{}\n', 'utf8');
  }
}

function send(res, status, body, contentType) {
  res.writeHead(status, {
    'Content-Type': contentType || 'text/plain; charset=utf-8',
    'Cache-Control': 'no-store'
  });
  res.end(body);
}

function sendJson(res, status, data) {
  send(res, status, JSON.stringify(data, null, 2), 'application/json; charset=utf-8');
}

function safePath(urlPath) {
  const decoded = decodeURIComponent(urlPath);
  const clean = decoded === '/' ? '/index.html' : decoded;
  const resolved = path.resolve(ROOT, '.' + clean);
  if (!resolved.startsWith(ROOT)) return null;
  return resolved;
}

function readBody(req) {
  return new Promise((resolve, reject) => {
    let raw = '';
    req.on('data', chunk => {
      raw += chunk;
      if (raw.length > 5 * 1024 * 1024) {
        reject(new Error('Payload demasiado grande'));
        req.destroy();
      }
    });
    req.on('end', () => resolve(raw));
    req.on('error', reject);
  });
}

ensureStateFile();

const server = http.createServer(async (req, res) => {
  const url = new URL(req.url, `http://${req.headers.host || `${HOST}:${PORT}`}`);

  if (url.pathname === '/api/state') {
    if (req.method === 'GET') {
      try {
        const raw = fs.readFileSync(STATE_FILE, 'utf8');
        return send(res, 200, raw, 'application/json; charset=utf-8');
      } catch (error) {
        return sendJson(res, 500, { error: error.message });
      }
    }

    if (req.method === 'PUT') {
      try {
        const raw = await readBody(req);
        const parsed = JSON.parse(raw || '{}');
        fs.writeFileSync(STATE_FILE, JSON.stringify(parsed, null, 2) + '\n', 'utf8');
        return sendJson(res, 200, { ok: true, keys: Object.keys(parsed).length });
      } catch (error) {
        return sendJson(res, 400, { ok: false, error: error.message });
      }
    }

    return sendJson(res, 405, { error: 'Metodo no permitido' });
  }

  if (req.method !== 'GET' && req.method !== 'HEAD') {
    return sendJson(res, 405, { error: 'Metodo no permitido' });
  }

  const filePath = safePath(url.pathname);
  if (!filePath) {
    return sendJson(res, 403, { error: 'Ruta no permitida' });
  }

  let target = filePath;
  if (fs.existsSync(target) && fs.statSync(target).isDirectory()) {
    target = path.join(target, 'index.html');
  }

  if (!fs.existsSync(target) || !fs.statSync(target).isFile()) {
    return send(res, 404, '404 Not Found');
  }

  const ext = path.extname(target).toLowerCase();
  const contentType = MIME[ext] || 'application/octet-stream';
  res.writeHead(200, { 'Content-Type': contentType, 'Cache-Control': 'no-store' });
  if (req.method === 'HEAD') return res.end();
  fs.createReadStream(target).pipe(res);
});

server.listen(PORT, HOST, () => {
  console.log(`BTCC disponible en http://${HOST}:${PORT}`);
});
