#!/usr/bin/env node
/**
 * LUMINA GHOST - Local Bridge Server
 * Teleports in-browser UI interactions directly into AGY & Claude Code.
 */
const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = process.env.PORT || 3939;
const CLIENT_JS_PATH = path.join(__dirname, 'client.js');
const DEMO_HTML_PATH = path.join(__dirname, 'demo.html');
const TASKS_DIR = path.join(process.cwd(), '.agents', 'tasks');

// Ensure .agents/tasks exists
if (!fs.existsSync(TASKS_DIR)) {
  fs.mkdirSync(TASKS_DIR, { recursive: true });
}

function sendJson(res, statusCode, data) {
  res.writeHead(statusCode, {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type'
  });
  res.end(JSON.stringify(data));
}

const server = http.createServer((req, res) => {
  // Handle CORS Preflight
  if (req.method === 'OPTIONS') {
    res.writeHead(204, {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type'
    });
    return res.end();
  }

  const parsedUrl = new URL(req.url, `http://${req.headers.host}`);
  const pathname = parsedUrl.pathname;

  // 1. Serve client.js
  if (pathname === '/ghost.js' || pathname === '/client.js') {
    if (fs.existsSync(CLIENT_JS_PATH)) {
      res.writeHead(200, {
        'Content-Type': 'application/javascript; charset=utf-8',
        'Access-Control-Allow-Origin': '*'
      });
      return res.end(fs.readFileSync(CLIENT_JS_PATH, 'utf-8'));
    }
  }

  // 2. Serve demo playground
  if (pathname === '/' || pathname === '/demo' || pathname === '/demo.html') {
    if (fs.existsSync(DEMO_HTML_PATH)) {
      res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
      return res.end(fs.readFileSync(DEMO_HTML_PATH, 'utf-8'));
    }
  }

  // 3. Status endpoint
  if (pathname === '/api/status') {
    return sendJson(res, 200, {
      status: 'online',
      version: '1.0.0',
      bridge: 'Lumina Ghost',
      pid: process.pid
    });
  }

  // 4. Ingest Visual Intent from Browser
  if (pathname === '/api/intent' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      try {
        const intent = JSON.parse(body);
        
        // Log to terminal with vibrant styling
        const timestamp = new Date().toLocaleTimeString();
        console.log(`\n\x1b[36m[${timestamp}] 🛸 LUMINA GHOST // INTENT RECEIVED\x1b[0m`);
        console.log(`\x1b[1m\x1b[32m✔ Target Component:\x1b[0m <${intent.target.componentName}> (\x1b[33m${intent.target.tagName}\x1b[0m)`);
        console.log(`\x1b[1m\x1b[35m⚡ Action:\x1b[0m ${intent.action}`);
        console.log(`\x1b[1m\x1b[37m💬 Directive:\x1b[0m "${intent.prompt}"`);
        if (intent.target.classes) {
          console.log(`\x1b[90mClasses: ${intent.target.classes.slice(0, 80)}...\x1b[0m`);
        }

        // Format and write high-priority AGY / Claude Code task
        const taskFile = path.join(TASKS_DIR, 'ghost-intent.md');
        const taskContent = `# 🛸 LUMINA GHOST: VISUAL INTENT DIRECTIVE
Timestamp: ${intent.timestamp}
Page URL: ${intent.pageUrl}

## 🎯 Target Component
- **Component / Name:** \`${intent.target.componentName}\`
- **Tag:** \`${intent.target.tagName}\`
- **Classes:** \`${intent.target.classes || 'none'}\`
- **Text Snippet:** "${intent.target.textSnippet || ''}"

## ⚡ User Action & Directive
- **Action Type:** \`${intent.action}\`
- **Instructions:** ${intent.prompt}

## 🎨 Recommended Fixes:
1. If Linear Polish: Add 1px chamfer (\`border border-white/[0.08] shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)]\`), dark obsidian background, and spring active scale (\`active:scale-[0.98]\`).
2. If Apple Glass: Add \`backdrop-blur-2xl bg-white/[0.06] border border-white/[0.12] rounded-2xl\`.
3. If Purge Slop: Remove generic purple/indigo gradients and enforce tight font tracking.
4. Refactor the corresponding source file and let Vite HMR update the browser.
`;

        fs.writeFileSync(taskFile, taskContent, 'utf-8');
        console.log(`\x1b[32m✔ Queued task for AGY & Claude Code -> \x1b[4m.agents/tasks/ghost-intent.md\x1b[0m`);

        // LIVE DISK AUTO-PATCHER ENGINE
        let patched = false;
        try {
          if (fs.existsSync(DEMO_HTML_PATH)) {
            let html = fs.readFileSync(DEMO_HTML_PATH, 'utf-8');
            const targetId = intent.target.id;
            const promptLower = (intent.prompt || '').toLowerCase();
            const action = intent.action;

            if (action === 'linear-polish' || promptLower.includes('linear') || promptLower.includes('chamfer')) {
              if (targetId === 'cta-button') {
                html = html.replace(/id="cta-button"[^>]*>[\s\S]*?<\/button>/,
                  `id="cta-button" class="px-6 py-3 rounded-xl bg-white hover:bg-neutral-100 text-neutral-950 font-semibold text-sm shadow-[0_1px_2px_rgba(0,0,0,0.1),0_0_20px_rgba(255,255,255,0.15)] active:scale-[0.98] transition-all flex items-center gap-2"><span>Deploy Telemetry Node</span><kbd class="text-[10px] font-mono px-1 rounded bg-black/10">⌘D</kbd></button>`);
                patched = true;
              } else if (targetId === 'hero-section' || targetId === 'secondary-btn') {
                html = html.replace(/class="p-8 rounded-2xl bg-neutral-900 border border-neutral-800/, 
                  'class="p-10 rounded-2xl bg-neutral-950/90 border border-white/[0.08] shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06),0_20px_50px_rgba(0,0,0,0.6)]');
                patched = true;
              }
            } else if (action === 'apple-glass' || promptLower.includes('apple')) {
              if (targetId === 'hero-section') {
                html = html.replace(/id="hero-section" class="[^"]*"/, 
                  `id="hero-section" class="p-10 rounded-3xl bg-white/[0.05] backdrop-blur-2xl border border-white/[0.15] shadow-[0_8px_32px_rgba(0,0,0,0.37)] text-center relative overflow-hidden group"`);
                patched = true;
              }
            } else if (action === 'purge-slop' || promptLower.includes('slop')) {
              html = html.replace(/from-purple-\d+|to-indigo-\d+|from-indigo-\d+|to-pink-\d+/g, 'from-neutral-900 to-neutral-950 border border-white/10');
              patched = true;
            }

            if (patched) {
              fs.writeFileSync(DEMO_HTML_PATH, html, 'utf-8');
              console.log(`\x1b[1m\x1b[32m✔ Auto-Patched ${targetId || 'target'} directly in demo.html on disk!\x1b[0m\n`);
            }
          }
        } catch (patchErr) {
          console.error('Auto-patch error:', patchErr);
        }

        return sendJson(res, 200, {
          success: true,
          patched: patched,
          message: patched ? 'Source file patched on disk!' : 'Intent received and queued for AGY & Claude Code',
          taskPath: '.agents/tasks/ghost-intent.md'
        });
      } catch (err) {
        console.error('Error parsing intent:', err);
        return sendJson(res, 400, { error: 'Invalid JSON payload' });
      }
    });
    return;
  }

  // 404 Fallback
  sendJson(res, 404, { error: 'Not found' });
});

server.listen(PORT, () => {
  console.log(`\x1b[1m\x1b[36m
  🛸 LUMINA GHOST BRIDGE ACTIVE ON http://localhost:${PORT}
  \x1b[0m\x1b[90m─────────────────────────────────────────────────────────────\x1b[0m
  • Client HUD Script:    \x1b[32mhttp://localhost:${PORT}/ghost.js\x1b[0m
  • Live Demo Playground: \x1b[32mhttp://localhost:${PORT}/demo\x1b[0m
  • Teleport Target:      \x1b[33m.agents/tasks/ghost-intent.md\x1b[0m
  \x1b[90m─────────────────────────────────────────────────────────────\x1b[0m
  \x1b[37mIn your browser, press \x1b[1m[Alt + Click]\x1b[0m\x1b[37m on any element to summon AI Capsule!\x1b[0m
  `);
});

module.exports = { server };
