#!/usr/bin/env node
const { spawn } = require('child_process');
const path = require('path');

const projectRoot = path.join(__dirname, '..');
const cliScript = path.join(projectRoot, 'lumina', 'cli.py');

const py = spawn('python', [cliScript, ...process.argv.slice(2)], {
  stdio: 'inherit',
  cwd: process.cwd(),
  env: {
    ...process.env,
    PYTHONPATH: projectRoot
  }
});

py.on('close', code => {
  process.exit(code || 0);
});
