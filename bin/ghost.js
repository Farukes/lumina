#!/usr/bin/env node
const path = require('path');
const serverPath = path.join(__dirname, '..', 'ghost', 'server.js');
require(serverPath);
