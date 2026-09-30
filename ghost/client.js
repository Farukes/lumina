/**
 * LUMINA GHOST - In-Browser AI HUD & Reverse-Agent Teleport Client
 * Zero-dependency, self-contained visual inspector for AGY & Claude Code builders.
 */
(function() {
  if (window.__LUMINA_GHOST_LOADED__) return;
  window.__LUMINA_GHOST_LOADED__ = true;

  const BRIDGE_URL = 'http://localhost:3939';
  let activeElement = null;
  let inspectorActive = false;
  let overlay = null;
  let capsule = null;
  let toastEl = null;

  // Web Audio Chime Synthesizer
  function playChime(success = true) {
    try {
      const ctx = new (window.AudioContext || window.webkitAudioContext)();
      const now = ctx.currentTime;
      const osc1 = ctx.createOscillator();
      const osc2 = ctx.createOscillator();
      const gain = ctx.createGain();

      if (success) {
        osc1.frequency.setValueAtTime(587.33, now); // D5
        osc1.frequency.exponentialRampToValueAtTime(880, now + 0.12); // A5
        osc2.frequency.setValueAtTime(880, now + 0.12);
        osc2.frequency.exponentialRampToValueAtTime(1174.66, now + 0.28); // D6
      } else {
        osc1.frequency.setValueAtTime(300, now);
        osc1.frequency.exponentialRampToValueAtTime(180, now + 0.15);
      }

      gain.gain.setValueAtTime(0.08, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);

      osc1.connect(gain);
      osc2.connect(gain);
      gain.connect(ctx.destination);

      osc1.start(now);
      osc1.stop(now + 0.35);
      if (success) {
        osc2.start(now + 0.12);
        osc2.stop(now + 0.35);
      }
    } catch (e) {}
  }

  // Toast Notification
  function showToast(message, type = 'success') {
    if (!toastEl) {
      toastEl = document.createElement('div');
      toastEl.id = 'lumina-ghost-toast';
      Object.assign(toastEl.style, {
        position: 'fixed',
        top: '20px',
        right: '20px',
        zIndex: '2147483647',
        padding: '12px 18px',
        borderRadius: '12px',
        backgroundColor: '#0a0a0c',
        color: '#f4f4f5',
        border: '1px solid rgba(16, 185, 129, 0.3)',
        boxShadow: '0 10px 30px rgba(0,0,0,0.7), inset 0 1px 0 rgba(255,255,255,0.1)',
        fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
        fontSize: '13px',
        fontWeight: '500',
        display: 'flex',
        alignItems: 'center',
        gap: '10px',
        transition: 'all 0.3s cubic-bezier(0.16, 1, 0.3, 1)',
        opacity: '0',
        transform: 'translateY(-10px)'
      });
      document.body.appendChild(toastEl);
    }
    toastEl.innerHTML = `<span style="color: #10b981;">●</span> ${message}`;
    toastEl.style.opacity = '1';
    toastEl.style.transform = 'translateY(0)';
    setTimeout(() => {
      toastEl.style.opacity = '0';
      toastEl.style.transform = 'translateY(-10px)';
    }, 3200);
  }

  // Create Inspector Bounding Box Overlay
  function createOverlay() {
    overlay = document.createElement('div');
    overlay.id = 'lumina-ghost-overlay';
    Object.assign(overlay.style, {
      position: 'fixed',
      pointerEvents: 'none',
      zIndex: '2147483640',
      border: '2px solid #10b981',
      borderRadius: '8px',
      boxShadow: '0 0 20px rgba(16, 185, 129, 0.35), inset 0 1px 0 rgba(255,255,255,0.2)',
      transition: 'all 0.08s ease-out',
      display: 'none'
    });
    document.body.appendChild(overlay);
  }

  function updateOverlay(el) {
    if (!el || !overlay) return;
    const rect = el.getBoundingClientRect();
    overlay.style.top = `${rect.top}px`;
    overlay.style.left = `${rect.left}px`;
    overlay.style.width = `${rect.width}px`;
    overlay.style.height = `${rect.height}px`;
    overlay.style.display = 'block';
  }

  // Extract React Fiber component metadata if available
  function getComponentInfo(el) {
    let name = el.tagName.toLowerCase();
    for (const key of Object.keys(el)) {
      if (key.startsWith('__reactFiber$')) {
        let fiber = el[key];
        while (fiber) {
          if (typeof fiber.type === 'function' && fiber.type.name) {
            name = fiber.type.name;
            break;
          }
          fiber = fiber.return;
        }
        break;
      }
    }
    return {
      name,
      tag: el.tagName.toLowerCase(),
      classes: el.className || '',
      id: el.id || '',
      textSnippet: (el.innerText || '').slice(0, 60).trim()
    };
  }

  // Create & Position Floating Capsule
  function showCapsule(el) {
    if (!capsule) {
      capsule = document.createElement('div');
      capsule.id = 'lumina-ghost-capsule';
      Object.assign(capsule.style, {
        position: 'fixed',
        zIndex: '2147483646',
        width: '340px',
        backgroundColor: 'rgba(10, 10, 14, 0.95)',
        backdropFilter: 'blur(20px)',
        WebkitBackdropFilter: 'blur(20px)',
        border: '1px solid rgba(255, 255, 255, 0.12)',
        boxShadow: '0 25px 60px rgba(0, 0, 0, 0.8), inset 0 1px 0 0 rgba(255, 255, 255, 0.1)',
        borderRadius: '16px',
        padding: '16px',
        fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
        color: '#ededed',
        animation: 'luminaFadeIn 0.2s cubic-bezier(0.16, 1, 0.3, 1)'
      });
      document.body.appendChild(capsule);
    }

    activeElement = el;
    updateOverlay(el);
    const info = getComponentInfo(el);
    const rect = el.getBoundingClientRect();

    // Position capsule intelligently
    let top = rect.bottom + 12;
    let left = rect.left;
    if (top + 280 > window.innerHeight) top = Math.max(10, rect.top - 290);
    if (left + 350 > window.innerWidth) left = window.innerWidth - 360;
    if (left < 10) left = 10;

    capsule.style.top = `${top}px`;
    capsule.style.left = `${left}px`;
    capsule.style.display = 'block';

    capsule.innerHTML = `
      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 10px;">
        <div style="display: flex; align-items: center; gap: 8px;">
          <span style="display: inline-block; width: 7px; height: 7px; border-radius: 50%; background: #10b981; box-shadow: 0 0 8px #10b981;"></span>
          <span style="font-size: 11px; font-family: monospace; text-transform: uppercase; color: #a1a1aa; letter-spacing: 0.05em;">LUMINA GHOST</span>
        </div>
        <span style="font-size: 11px; font-family: monospace; background: rgba(255,255,255,0.06); padding: 2px 6px; border-radius: 4px; color: #34d399; border: 1px solid rgba(255,255,255,0.08);">${info.name}</span>
        <button id="lumina-close-btn" style="background: none; border: none; color: #71717a; cursor: pointer; font-size: 12px; padding: 2px;">✕</button>
      </div>

      <!-- Quick Action Buttons -->
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px; margin-bottom: 12px;">
        <button class="lumina-action-btn" data-action="linear-polish" style="display: flex; align-items: center; gap: 6px; padding: 8px 10px; border-radius: 8px; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); color: #f4f4f5; font-size: 11px; cursor: pointer; transition: all 0.15s; font-weight: 500;">
          <span>✨</span> Linear Polish
        </button>
        <button class="lumina-action-btn" data-action="apple-glass" style="display: flex; align-items: center; gap: 6px; padding: 8px 10px; border-radius: 8px; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); color: #f4f4f5; font-size: 11px; cursor: pointer; transition: all 0.15s; font-weight: 500;">
          <span>🍏</span> Apple Glass
        </button>
        <button class="lumina-action-btn" data-action="purge-slop" style="display: flex; align-items: center; gap: 6px; padding: 8px 10px; border-radius: 8px; background: rgba(239,68,68,0.08); border: 1px solid rgba(239,68,68,0.2); color: #fca5a5; font-size: 11px; cursor: pointer; transition: all 0.15s; font-weight: 500;">
          <span>🧹</span> Purge AI Slop
        </button>
        <button class="lumina-action-btn" data-action="fix-mobile" style="display: flex; align-items: center; gap: 6px; padding: 8px 10px; border-radius: 8px; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); color: #f4f4f5; font-size: 11px; cursor: pointer; transition: all 0.15s; font-weight: 500;">
          <span>📱</span> Fix Mobile
        </button>
      </div>

      <!-- Micro-Prompt Input -->
      <div style="position: relative;">
        <input 
          id="lumina-prompt-input" 
          type="text" 
          placeholder="Or type prompt: 'make this feel like Linear...'" 
          style="width: 100%; box-sizing: border-box; background: rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; padding: 8px 30px 8px 10px; font-size: 11px; color: #fff; outline: none; transition: border-color 0.2s;"
        />
        <button id="lumina-submit-prompt" style="position: absolute; right: 6px; top: 50%; transform: translateY(-50%); background: #10b981; border: none; border-radius: 4px; color: #000; width: 20px; height: 20px; font-size: 10px; cursor: pointer; display: flex; align-items: center; justify-content: center; font-weight: bold;">↵</button>
      </div>

      <div style="margin-top: 8px; font-size: 10px; color: #71717a; display: flex; justify-content: space-between;">
        <span>Teleports to AGY & Claude Code</span>
        <span style="font-family: monospace;">Alt + Click anywhere</span>
      </div>
    `;

    // Wire events
    capsule.querySelector('#lumina-close-btn').onclick = hideCapsule;

    capsule.querySelectorAll('.lumina-action-btn').forEach(btn => {
      btn.onmouseenter = () => btn.style.borderColor = 'rgba(16, 185, 129, 0.4)';
      btn.onmouseleave = () => btn.style.borderColor = 'rgba(255, 255, 255, 0.08)';
      btn.onclick = () => sendIntent(btn.dataset.action, btn.innerText.trim());
    });

    const promptInput = capsule.querySelector('#lumina-prompt-input');
    const submitBtn = capsule.querySelector('#lumina-submit-prompt');
    const submitPrompt = () => {
      const val = promptInput.value.trim();
      if (val) sendIntent('custom-prompt', val);
    };

    promptInput.onkeydown = (e) => {
      if (e.key === 'Enter') submitPrompt();
      if (e.key === 'Escape') hideCapsule();
    };
    submitBtn.onclick = submitPrompt;
    setTimeout(() => promptInput.focus(), 50);
  }

  function hideCapsule() {
    if (capsule) capsule.style.display = 'none';
    if (overlay) overlay.style.display = 'none';
    activeElement = null;
  }

  // Send Intent to AGY / Claude Code Local Bridge
  async function sendIntent(actionType, promptText) {
    if (!activeElement) return;

    const info = getComponentInfo(activeElement);
    const computed = window.getComputedStyle(activeElement);

    const payload = {
      timestamp: new Date().toISOString(),
      action: actionType,
      prompt: promptText,
      target: {
        componentName: info.name,
        tagName: info.tag,
        id: info.id,
        classes: info.classes,
        textSnippet: info.textSnippet,
        outerHTML: activeElement.outerHTML.slice(0, 400),
        computedStyles: {
          padding: computed.padding,
          margin: computed.margin,
          backgroundColor: computed.backgroundColor,
          color: computed.color,
          display: computed.display,
          borderRadius: computed.borderRadius
        }
      },
      pageUrl: window.location.href
    };

    // Client-side Instant Preview (Optimistic Feedback)
    if (actionType === 'linear-polish') {
      activeElement.style.border = '1px solid rgba(255, 255, 255, 0.08)';
      activeElement.style.boxShadow = 'inset 0 1px 0 0 rgba(255, 255, 255, 0.08), 0 10px 30px rgba(0, 0, 0, 0.5)';
      activeElement.style.borderRadius = '12px';
      activeElement.style.transition = 'transform 0.1s ease-out';
      activeElement.onmousedown = () => activeElement.style.transform = 'scale(0.98)';
      activeElement.onmouseup = () => activeElement.style.transform = 'scale(1)';
    } else if (actionType === 'apple-glass') {
      activeElement.style.backdropFilter = 'blur(20px)';
      activeElement.style.backgroundColor = 'rgba(255, 255, 255, 0.06)';
      activeElement.style.borderRadius = '20px';
      activeElement.style.border = '1px solid rgba(255, 255, 255, 0.15)';
    } else if (actionType === 'purge-slop') {
      activeElement.className = activeElement.className.replace(/from-purple-\d+|to-indigo-\d+|from-indigo-\d+|bg-gradient-[^ ]+/g, 'bg-neutral-950 border border-white/10');
    }

    playChime(true);
    showToast(`Teleported "${promptText}" to AGY & Claude Code!`);
    hideCapsule();

    // Dispatch to local bridge server
    try {
      await fetch(`${BRIDGE_URL}/api/intent`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
    } catch (err) {
      console.warn('[Lumina Ghost] Local bridge not responding on :3939. Intent logged locally.');
    }
  }

  // Floating Corner Badge (Pill)
  function createCornerBadge() {
    const badge = document.createElement('div');
    badge.id = 'lumina-ghost-badge';
    Object.assign(badge.style, {
      position: 'fixed',
      bottom: '16px',
      right: '16px',
      zIndex: '2147483630',
      padding: '8px 14px',
      borderRadius: '9999px',
      backgroundColor: 'rgba(10, 10, 14, 0.85)',
      backdropFilter: 'blur(12px)',
      border: '1px solid rgba(255, 255, 255, 0.1)',
      boxShadow: '0 8px 24px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.08)',
      fontFamily: '-apple-system, BlinkMacSystemFont, sans-serif',
      fontSize: '11px',
      fontWeight: '500',
      color: '#a1a1aa',
      display: 'flex',
      alignItems: 'center',
      gap: '8px',
      cursor: 'pointer',
      userSelect: 'none',
      transition: 'all 0.2s cubic-bezier(0.16, 1, 0.3, 1)'
    });

    badge.innerHTML = `
      <span style="display: inline-block; width: 6px; height: 6px; border-radius: 50%; background: #10b981; box-shadow: 0 0 6px #10b981;"></span>
      <span style="color: #fff; font-weight: 600;">LUMINA GHOST</span>
      <span style="color: #71717a; font-family: monospace; font-size: 10px;">[Alt + Click]</span>
    `;

    badge.onmouseenter = () => {
      badge.style.transform = 'translateY(-2px)';
      badge.style.borderColor = 'rgba(16, 185, 129, 0.4)';
    };
    badge.onmouseleave = () => {
      badge.style.transform = 'translateY(0)';
      badge.style.borderColor = 'rgba(255, 255, 255, 0.1)';
    };
    badge.onclick = () => {
      showToast('Alt + Click (Option + Click) any component to summon AI Capsule!');
      playChime(true);
    };

    document.body.appendChild(badge);
  }

  // Global Event Listeners
  function initListeners() {
    createOverlay();
    createCornerBadge();

    // Hover detection while holding Alt
    window.addEventListener('mousemove', (e) => {
      if (e.altKey) {
        const target = e.target;
        if (target && !target.closest('#lumina-ghost-capsule') && !target.closest('#lumina-ghost-badge')) {
          updateOverlay(target);
        }
      } else if (!capsule || capsule.style.display === 'none') {
        if (overlay) overlay.style.display = 'none';
      }
    });

    // Alt + Click Trigger
    window.addEventListener('click', (e) => {
      if (e.altKey) {
        const target = e.target;
        if (target.closest('#lumina-ghost-capsule') || target.closest('#lumina-ghost-badge')) return;
        e.preventDefault();
        e.stopPropagation();
        showCapsule(target);
      }
    }, true);

    // Escape closes capsule
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') hideCapsule();
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initListeners);
  } else {
    initListeners();
  }
})();
