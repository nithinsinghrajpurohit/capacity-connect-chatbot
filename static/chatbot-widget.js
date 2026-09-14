(function() {
  const API = window.ASTRA_API_URL || 'http://localhost:5000';
  let open = false, user = null, sid = 'sess_' + Math.random().toString(36).slice(2, 10);
  let mode = null, quizSess = null, msgIdx = 0;

  const MODES = [['learn','Learn'],['deep','Deep'],['quiz','Quiz'],['revise','Revise'],['notes','Notes'],['path','Path'],['code','Code'],['math','Math']];

  function pageCtx() {
    const q = s => document.querySelector(s);
    return {
      page: document.title || location.pathname,
      course_title: (q('[data-astra-course]')||{}).textContent || (q('[data-course-title]')||{}).textContent || '',
      lesson_title: (q('[data-astra-lesson]')||{}).textContent || ''
    };
  }
  function esc(t) { const d = document.createElement('div'); d.textContent = t; return d.innerHTML; }
  function md(t) {
    let h = esc(t), parts = [];
    h = h.replace(/```(\w*)\n?([\s\S]*?)```/g, (m, l, c) => {
      parts.push({l: l || 'code', c: c.replace(/<[^>]*>/g, m2 => ({'&lt;':'<','&gt;':'>','&amp;':'&'}[m2]||m2))});
      return '\u0000' + (parts.length - 1) + '\u0000';
    });
    h = h.replace(/^### (.*)$/gm, '<h3>$1</h3>').replace(/^## (.*)$/gm, '<h2>$1</h2>').replace(/^# (.*)$/gm, '<h1>$1</h1>');
    h = h.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>').replace(/(^|\W)_([^_\n]+)_/g, '$1<em>$2</em>').replace(/`([^`\n]+)`/g, '<code>$1</code>');
    
    // Horizontal rules
    h = h.replace(/^---+$/gm, '<hr>');
    // Blockquotes
    h = h.replace(/^&gt; (.*)$/gm, '<blockquote>$1</blockquote>');
    // Unordered lists  
    h = h.replace(/^[\-\*] (.*)$/gm, '<li>$1</li>');
    h = h.replace(/(<li>.*<\/li>\n?)+/g, '<ul>$&</ul>');
    // Ordered lists
    h = h.replace(/^\d+\. (.*)$/gm, '<li>$1</li>');

    h = h.replace(/\n/g, '<br>');
    h = h.replace(/\u0000(\d+)\u0000/g, (m, i) => {
      const p = parts[+i];
      return '<div class="ast-code"><div class="ast-code-h"><span>' + esc(p.l) + '</span><button data-copy="' + i + '">copy</button></div><pre>' + p.c + '</pre></div>';
    });
    return h;
  }
  function init() {
    if (document.getElementById('ast-ra-widget')) return;
    const w = document.createElement('div');
    w.id = 'ast-ra-widget';
    w.innerHTML =
      '<div class="ast-badge" id="abadge"><span id="aname"></span><span class="rl" id="arole"></span></div>' +
      '<div id="ast-ra-panel"><div id="ast-ra-header"><div id="ast-ra-avatar">✦</div>' +
      '<div id="ast-ra-header-info"><h3>Sastra</h3><p><span class="dot">●</span> AI Learning Assistant</p></div>' +
      '<button class="ast-hbtn" id="abtn-new" title="New chat">＋</button>' +
      '<button class="ast-hbtn" id="abtn-exp" title="Export chat">⤓</button>' +
      '<button class="ast-hbtn" id="abtn-x" title="Close">✕</button></div>' +
      '<div id="ast-ra-modes" style="display:none">' + MODES.map(m => '<button class="ast-mode" data-m="' + m[0] + '">' + m[1] + '</button>').join('') + '</div>' +
      '<div id="ast-ra-login"><h4>Welcome to Sastra</h4>' +
      '<input id="a-user" placeholder="Username" autocomplete="off"><input id="a-pass" type="password" placeholder="Password">' +
      '<div class="ast-error" id="a-err"></div><button class="go" id="a-go">Sign In</button>' +
      '<button class="ast-skip" id="a-skip">Continue as Guest</button></div>' +
      '<div id="ast-ra-messages" style="display:none"></div>' +
      '<div class="ast-quick" id="a-quick" style="display:none"></div>' +
      '<div id="ast-ra-input-area" style="display:none"><div id="ast-ra-tools">' +
      '<button class="ast-tool" data-a="quiz">▶ Quiz session</button>' +
      '<button class="ast-tool" data-a="cards">🗂 Flashcards</button>' +
      '<button class="ast-tool" data-a="pdf">📄 PDF guide</button>' +
      '<button class="ast-tool" data-a="path">🗺 Path</button>' +
      '<button class="ast-tool" data-a="clear">🧹 Clear</button></div>' +
      '<div id="ast-ra-row"><button class="ast-ibtn" id="a-file" title="Attach .txt/.md">📎</button>' +
      '<textarea id="a-in" placeholder="Ask Astra anything..." rows="1"></textarea>' +
      '<button class="ast-ibtn" id="a-mic" title="Voice input">🎤</button>' +
      '<button class="ast-ibtn" id="ast-ra-send" title="Send"><svg viewBox="0 0 24 24"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg></button></div></div></div>' +
      '<button id="ast-ra-fab"><svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg></button>' +
      '<input type="file" id="a-upload" accept=".txt,.md,.py,.js" style="display:none">';
    document.body.appendChild(w);
    document.getElementById('ast-ra-fab').onclick = toggle;
    document.getElementById('abtn-x').onclick = () => setOpen(false);
    document.getElementById('a-go').onclick = login;
    document.getElementById('a-skip').onclick = () => { user = null; localStorage.removeItem('astra-token'); show(); say('bot', "Hello! I'm **Astra**. Try: *Explain Python functions* · *Quiz me* · *Learning path for ML* · *Flashcards for loops*"); };
    document.getElementById('ast-ra-send').onclick = send;
    document.getElementById('a-in').addEventListener('keydown', e => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); send(); } });
    document.getElementById('abtn-new').onclick = () => { sid = 'sess_' + Math.random().toString(36).slice(2, 10); quizSess = null; el('ast-ra-messages').innerHTML = ''; localStorage.removeItem('astra-token'); say('bot', 'Fresh session started. What shall we master?'); };
    document.getElementById('abtn-exp').onclick = () => {
      const token = localStorage.getItem('astra-token') || '';
      fetch(API + '/api/chat/export?user_id=' + (user ? user.id : 0) + '&session_id=' + sid, { headers: { 'Authorization': 'Bearer ' + token } })
        .then(r => r.blob()).then(b => {
          const u = URL.createObjectURL(b);
          const x = document.createElement('a');
          x.href = u; x.download = 'export.md'; x.click();
        });
    };
    document.querySelectorAll('.ast-mode').forEach(b => b.onclick = () => {
      document.querySelectorAll('.ast-mode').forEach(x => x.classList.remove('on'));
      mode = (mode === b.dataset.m) ? null : b.dataset.m;
      if (mode) b.classList.add('on');
      say('bot', mode ? '**' + b.textContent + ' mode** on. Ask your question.' : 'Mode cleared — auto-detect on.');
    });
    document.querySelectorAll('.ast-tool').forEach(b => b.onclick = () => tool(b.dataset.a));
    document.getElementById('a-mic').onclick = voice;
    document.getElementById('a-file').onclick = () => el('a-upload').click();
    document.getElementById('a-upload').onchange = attach;
    document.getElementById('ast-ra-messages').addEventListener('click', e => {
      const c = e.target.closest('[data-copy]');
      if (c) { const pre = c.closest('.ast-code').querySelector('pre').innerText; navigator.clipboard.writeText(pre); c.textContent = 'copied'; setTimeout(() => c.textContent = 'copy', 1200); return; }
      const f = e.target.closest('[data-fb]');
      if (f) { fb(f); return; }
      const s = e.target.closest('[data-s]');
      if (s) { el('a-in').value = s.dataset.s; send(); }
    });

    // Auto-detect user from host website / login page
    const hostUser = detectHostUser();
    if (hostUser) {
      setUserFromExternal(hostUser, false);
    } else {
      const sv = localStorage.getItem('astra-user') || localStorage.getItem('sastra_learner_profile');
      if (sv) {
        try {
          user = JSON.parse(sv);
          show();
          loadHistory();
          setTimeout(() => say('bot', 'Welcome back, ' + user.full_name + ' (' + (user.role || 'trainee') + '). What shall we work on?'), 300);
        } catch(e) {}
      }
    }

    // Attach listeners to host page login forms & message events
    bindHostLoginListeners();
  }

  function detectHostUser() {
    // 1. Check global window variables set by host website
    const win = window;
    const gUser = win.SASTRA_USER || win.ASTRA_USER || win.CURRENT_USER || win.LOGGED_IN_USER || win.USER_NAME || win.userName || win.username || (win.SastraConfig && win.SastraConfig.user) || (win.AstraConfig && win.AstraConfig.user);
    if (gUser) {
      if (typeof gUser === 'string') return { full_name: gUser, username: gUser, role: 'trainee' };
      if (typeof gUser === 'object') return { full_name: gUser.full_name || gUser.name || gUser.username || 'Learner', username: gUser.username || gUser.email || '', role: gUser.role || 'trainee' };
    }

    // 2. Check URL query parameters (e.g. ?username=Sneha or ?user=Mourya)
    try {
      const params = new URLSearchParams(window.location.search);
      const qUser = params.get('user') || params.get('username') || params.get('name') || params.get('user_name') || params.get('login_user');
      if (qUser && qUser.trim()) {
        const clean = qUser.trim();
        return { full_name: clean, username: clean, role: 'trainee' };
      }
    } catch(e) {}

    // 3. Check host website localStorage / sessionStorage keys
    const storageKeys = [
      'username', 'user_name', 'name', 'full_name', 'user', 'currentUser', 
      'auth_user', 'authUser', 'loggedUser', 'login_user', 'capacity_user', 
      'sastra_learner_profile', 'sastra_user', 'astra-user', 'userProfile', 'profile', 'userData'
    ];
    for (const k of storageKeys) {
      const val = localStorage.getItem(k) || sessionStorage.getItem(k);
      if (val) {
        try {
          const parsed = JSON.parse(val);
          if (parsed && typeof parsed === 'object') {
            const fn = parsed.full_name || parsed.name || parsed.username || parsed.email;
            if (fn && typeof fn === 'string') return { full_name: fn, username: parsed.username || fn, role: parsed.role || 'trainee' };
          }
        } catch(e) {
          if (typeof val === 'string' && val.length > 1 && val.length < 50 && !val.includes('{')) {
            return { full_name: val, username: val, role: 'trainee' };
          }
        }
      }
    }

    // 4. Check active DOM elements on host login page
    const loginInput = document.querySelector('input[name="username"], input[name="user"], input#username, input#user, input[autocomplete="username"], input[data-user-name]');
    if (loginInput && loginInput.value && loginInput.value.trim()) {
      const val = loginInput.value.trim();
      return { full_name: val, username: val, role: 'trainee' };
    }

    return null;
  }

  function setUserFromExternal(data, greet=true) {
    if (!data) return;
    let name = '';
    let role = 'trainee';
    let id = 0;
    if (typeof data === 'string') {
      name = data.trim();
    } else if (typeof data === 'object') {
      name = (data.full_name || data.name || data.username || 'Learner').trim();
      role = data.role || 'trainee';
      id = data.id || 0;
    }
    if (!name) return;

    user = { id: id, full_name: name, username: name.toLowerCase().replace(/\s+/g, '_'), role: role };
    try { localStorage.setItem('astra-user', JSON.stringify(user)); } catch(e) {}
    show();
    if (greet) {
      say('bot', 'Hello ' + name + '! Sastra is synced with your login session. How can I help you today?');
    }
  }

  function bindHostLoginListeners() {
    // 1. Listen for window postMessage from parent frame or host login script
    window.addEventListener('message', e => {
      if (e.data && (e.data.type === 'SASTRA_SET_USER' || e.data.type === 'ASTRA_SET_USER' || e.data.type === 'LOGIN_SUCCESS' || e.data.type === 'USER_LOGIN')) {
        const payload = e.data.user || e.data.username || e.data.user_name || e.data.full_name || e.data.name;
        if (payload) setUserFromExternal(payload, true);
      }
    });

    // 2. Watch host page login forms for user input or submit
    document.addEventListener('input', e => {
      const t = e.target;
      if (t && (t.name === 'username' || t.name === 'user' || t.id === 'username' || t.id === 'user' || t.getAttribute('data-user-name') !== null)) {
        if (t.value && t.value.trim().length >= 2) {
          const val = t.value.trim();
          user = { id: 0, full_name: val, username: val.toLowerCase().replace(/\s+/g, '_'), role: 'trainee' };
          const badg = el('abadge'); if (badg) badg.classList.add('show');
          const an = el('aname'); if (an) an.textContent = val;
        }
      }
    });

    document.addEventListener('submit', e => {
      const loginInp = document.querySelector('input[name="username"], input[name="user"], input#username, input#user, input[data-user-name]');
      if (loginInp && loginInp.value && loginInp.value.trim()) {
        setUserFromExternal(loginInp.value.trim(), true);
      }
    });

    // 3. Expose global window.Sastra & window.Astra API for host websites
    window.Sastra = window.Astra = {
      setUser: function(u) { setUserFromExternal(u, true); },
      getUser: function() { return user; },
      open: function() { setOpen(true); },
      close: function() { setOpen(false); },
      send: function(msg) { el('a-in').value = msg; send(); }
    };
  }

  function el(id) { return document.getElementById(id); }
  function toggle() { setOpen(!open); }
  function setOpen(v) { open = v; el('ast-ra-panel').classList.toggle('open', v); if (v) setTimeout(() => el('a-in') && el('a-in').focus(), 100); }
  function login() {
    const u = el('a-user').value.trim(), p = el('a-pass').value, err = el('a-err');
    if (!u || !p) { err.textContent = 'Enter username and password'; err.style.display = 'block'; return; }
    fetch(API + '/api/auth/login', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({username: u, password: p})})
      .then(r => r.json().then(d => ({ok: r.ok, d}))).then(({ok, d}) => {
        if (!ok) { err.textContent = d.error || 'Login failed'; err.style.display = 'block'; return; }
        user = d; localStorage.setItem('astra-user', JSON.stringify(user)); localStorage.setItem('astra-token', d.token || ''); show();
        say('bot', 'Welcome back, ' + user.full_name + '! Signed in as ' + user.role + '. How can I help?');
      }).catch(() => { err.textContent = 'No server — continue as guest.'; err.style.display = 'block'; });
  }
  function show() {
    el('ast-ra-login').style.display = 'none';
    el('ast-ra-messages').style.display = 'flex';
    el('a-quick').style.display = 'flex';
    el('ast-ra-input-area').style.display = 'block';
    el('ast-ra-modes').style.display = 'flex';
    if (user) { el('abadge').classList.add('show'); el('aname').textContent = user.full_name; const r = el('arole'); r.textContent = user.role; r.className = 'rl ' + user.role; }
    loadHistory();
  }
  function loadHistory() {
    if (!user) return;
    const token = localStorage.getItem('astra-token') || '';
    fetch(API + '/api/chat/history/' + user.id, { headers: { 'Authorization': 'Bearer ' + token } })
        .then(r => r.json())
        .then(msgs => {
            if (!msgs || !msgs.length) return;
            const recent = msgs.slice(-20);
            recent.forEach(m => {
                say(m.role === 'user' ? 'user' : 'bot', m.message);
            });
        })
        .catch(() => {});
  }
  function say(who, text, sug) {
    const box = el('ast-ra-messages'), d = document.createElement('div');
    d.className = 'ast-msg ' + who; msgIdx++;
    const now = new Date().toLocaleTimeString([], {hour: '2-digit', minute: '2-digit'});
    d.innerHTML = '<div class="ast-msg-bubble">' + (who === 'bot' ? md(text) : esc(text)) + '</div><div class="ast-msg-time">' + now + '</div>' +
      (who === 'bot' ? '<div class="ast-fb"><button data-fb="up" data-i="' + msgIdx + '" title="Helpful">👍</button><button data-fb="down" data-i="' + msgIdx + '" title="Not helpful">👎</button></div>' : '');
    box.appendChild(d); box.scrollTop = box.scrollHeight;
    if (sug && sug.length) chips(sug);
  }
  function chips(sug) {
    const q = el('a-quick'); q.innerHTML = '';
    sug.slice(0, 5).forEach(s => { const b = document.createElement('button'); b.textContent = s; b.onclick = () => { el('a-in').value = s; send(); }; q.appendChild(b); });
  }
  function typing(on) {
    let t = document.getElementById('ast-t');
    if (on) { const box = el('ast-ra-messages'), d = document.createElement('div'); d.id = 'ast-t'; d.className = 'ast-msg bot';
      d.innerHTML = '<div class="ast-typing"><span></span><span></span><span></span></div>'; box.appendChild(d); box.scrollTop = box.scrollHeight; }
    else if (t) t.remove();
  }
  function send() {
    const inp = el('a-in'), v = inp.value.trim();
    if (!v) return;
    if (!el('ast-ra-panel').classList.contains('open')) setOpen(true);
    if (el('ast-ra-login').style.display !== 'none') { el('a-skip').click(); }
    inp.value = ''; say('user', v); typing(true);
    if (quizSess && /^\d+$/.test(v)) return quizAns(parseInt(v, 10) - 1);
    const token = localStorage.getItem('astra-token') || '';
    const currentUserName = user ? user.full_name : ((detectHostUser() || {}).full_name || '');
    fetch(API + '/api/chat', {method: 'POST', headers: {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token},
      body: JSON.stringify({message: v, user_id: user ? user.id : null, user_name: currentUserName, session_id: sid, mode: mode, context: pageCtx()})})
      .then(r => r.json()).then(d => { typing(false); say('bot', d.reply || 'Hmm, rephrase that?', d.suggestions); })
      .catch(() => { typing(false); say('bot', 'Cannot reach server. Start backend: `python app.py`.'); });
  }
  function tool(a) {
    const token = localStorage.getItem('astra-token') || '';
    if (a === 'clear') {
        fetch(API + '/api/chat/clear', {method:'POST', headers:{'Content-Type':'application/json', 'Authorization': 'Bearer ' + token}, body: JSON.stringify({user_id: user ? user.id : 0, session_id: sid})});
        el('ast-ra-messages').innerHTML = '';
        say('bot', 'Chat cleared. What shall we work on?');
        return;
    }
    if (a === 'quiz') { qStart(); return; }
    const templates = {
        'pdf': 'PDF study guide for ',
        'cards': 'Flashcards for ',
        'path': 'Learning path for '
    };
    if (templates[a]) {
        const inp = el('a-in');
        inp.value = templates[a];
        inp.focus();
        inp.selectionStart = inp.selectionEnd = inp.value.length;
    }
  }
  function qStart() {
    typing(true);
    fetch(API + '/api/quiz/session/start', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({count: 5})})
      .then(r => r.json()).then(d => { typing(false); quizSess = d.session_id;
        say('bot', 'Quiz Session — reply with the option number.\n\nQ1. ' + d.question + '\n' + d.options.map((o, i) => (i+1) + '. ' + o).join('\n')); })
      .catch(() => { typing(false); say('bot', 'Quiz failed — server down?'); });
  }
  function quizAns(n) {
    fetch(API + '/api/quiz/session/answer', {method: 'POST', headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({session_id: quizSess, answer: n, user_id: user ? user.id : null})})
      .then(r => r.json()).then(d => { typing(false);
        if (d.done) { quizSess = null; say('bot', 'Quiz complete — ' + d.score + '% (' + d.correct + '/' + d.total + ')\n\n' + d.next, ['Revise weak topics', 'Quiz me again', 'What should I learn next?']); }
        else say('bot', d.feedback + '\n\nQ' + (d.index+1) + '. ' + d.question + '\n' + d.options.map((o, i) => (i+1) + '. ' + o).join('\n'));
      }).catch(() => typing(false));
  }
  function fb(btn) {
    btn.parentElement.querySelectorAll('button').forEach(b => b.classList.remove('sel'));
    btn.classList.add('sel');
    const token = localStorage.getItem('astra-token') || '';
    fetch(API + '/api/chat/feedback', {method: 'POST', headers: {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token},
      body: JSON.stringify({user_id: user ? user.id : 0, session_id: sid, message_index: btn.dataset.i, rating: btn.dataset.fb})}).catch(() => {});
  }
  function voice() {
    const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SR) return alert('Voice not supported in this browser.');
    const r = new SR(); r.lang = 'en-US'; el('a-mic').classList.add('live'); r.start();
    r.onresult = e => { el('a-in').value = e.results[0][0].transcript; el('a-mic').classList.remove('live'); send(); };
    r.onend = () => el('a-mic').classList.remove('live');
  }
  function attach(e) {
    const f = e.target.files[0]; if (!f) return;
    const rd = new FileReader();
    rd.onload = () => { const txt = String(rd.result).slice(0, 3000);
      el('a-in').value = 'Explain / summarize this attached content:\n\n' + txt; send(); };
    rd.readAsText(f); e.target.value = '';
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
