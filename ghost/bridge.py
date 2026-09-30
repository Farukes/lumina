"""
Lumina Ghost - Python Native Bridge Server
Serves /ghost.js, /demo, and handles POST /api/intent for AGY and Claude Code.
"""
import os
import sys
import json
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler
import webbrowser

PORT = 3939
BASE_DIR = Path(__file__).resolve().parent
TASKS_DIR = Path.cwd() / ".agents" / "tasks"

TASKS_DIR.mkdir(parents=True, exist_ok=True)

class GhostRequestHandler(BaseHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    def do_GET(self):
        path = self.path.split("?")[0]

        if path in ("/ghost.js", "/client.js"):
            client_file = BASE_DIR / "client.js"
            if client_file.exists():
                self.send_response(200)
                self.send_header("Content-Type", "application/javascript; charset=utf-8")
                self.end_headers()
                self.wfile.write(client_file.read_bytes())
                return

        if path in ("/", "/demo", "/demo.html"):
            demo_file = BASE_DIR / "demo.html"
            if demo_file.exists():
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(demo_file.read_bytes())
                return

        if path == "/api/status":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "online", "bridge": "Lumina Ghost Python"}).encode())
            return

        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        if self.path == "/api/intent":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            
            try:
                intent = json.loads(body)
                target = intent.get("target", {})

                print("\n\033[36m🛸 LUMINA GHOST // INTENT RECEIVED FROM BROWSER\033[0m")
                print(f"\033[1m\033[32m✔ Target Component:\033[0m <{target.get('componentName')}> (\033[33m{target.get('tagName')}\033[0m)")
                print(f"\033[1m\033[35m⚡ Action:\033[0m {intent.get('action')}")
                print(f"\033[1m\033[37m💬 Directive:\033[0m \"{intent.get('prompt')}\"")

                # Format task for AGY & Claude Code
                task_content = f"""# 🛸 LUMINA GHOST: VISUAL INTENT DIRECTIVE
Timestamp: {intent.get('timestamp')}
Page URL: {intent.get('pageUrl')}

## 🎯 Target Component
- **Component / Name:** `{target.get('componentName')}`
- **Tag:** `{target.get('tagName')}`
- **Classes:** `{target.get('classes', 'none')}`
- **Text Snippet:** "{target.get('textSnippet', '')}"

## ⚡ User Action & Directive
- **Action Type:** `{intent.get('action')}`
- **Instructions:** {intent.get('prompt')}

## 🎨 Recommended Fixes:
1. If Linear Polish: Add 1px chamfer (`border border-white/[0.08] shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06)]`), dark obsidian background, and spring active scale (`active:scale-[0.98]`).
2. If Apple Glass: Add `backdrop-blur-2xl bg-white/[0.06] border border-white/[0.12] rounded-2xl`.
3. If Purge Slop: Remove generic purple/indigo gradients and enforce tight font tracking.
4. Refactor the corresponding source file and let Vite HMR update the browser.
"""
                task_file = TASKS_DIR / "ghost-intent.md"
                task_file.write_text(task_content, encoding="utf-8")
                print(f"\033[32m✔ Queued task for AGY & Claude Code -> \033[4m.agents/tasks/ghost-intent.md\033[0m\n")

                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "task": str(task_file)}).encode())
                return
            except Exception as e:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode())
                return

        self.send_response(404)
        self.end_headers()

def run_bridge(open_browser=True):
    server = HTTPServer(("127.0.0.1", PORT), GhostRequestHandler)
    print(f"""\033[1m\033[36m
  🛸 LUMINA GHOST BRIDGE ACTIVE ON http://localhost:{PORT}
  \033[0m\033[90m─────────────────────────────────────────────────────────────\033[0m
  • Client HUD Script:    \033[32mhttp://localhost:{PORT}/ghost.js\033[0m
  • Live Demo Playground: \033[32mhttp://localhost:{PORT}/demo\033[0m
  • Teleport Target:      \033[33m.agents/tasks/ghost-intent.md\033[0m
  \033[90m─────────────────────────────────────────────────────────────\033[0m
  \033[37mIn your browser, press \033[1m[Alt + Click]\033[0m\033[37m on any element to summon AI Capsule!\033[0m
  """)
    if open_browser:
        webbrowser.open(f"http://localhost:{PORT}/demo")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\033[33m🛸 Lumina Ghost Bridge stopped.\033[0m")

if __name__ == "__main__":
    run_bridge()
