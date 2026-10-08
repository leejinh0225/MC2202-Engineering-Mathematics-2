(() => {
  const canvas = document.getElementById('heat-demo');
  const range = document.getElementById('heat-time');
  if (!canvas || !range) return;
  function temperature(x, t) {
    if (t === 0) return Math.min(x, Math.PI - x);
    let sum = 0;
    for (let m = 0; m < 80; m++) {
      const n = 2 * m + 1;
      sum += (m % 2 ? -1 : 1) * Math.sin(n * x) * Math.exp(-n * n * t) / (n * n);
    }
    return 4 / Math.PI * sum;
  }
  function draw() {
    const ctx = canvas.getContext('2d');
    if (!ctx) return;
    const dark = document.documentElement.dataset.mode === 'newbie';
    const t = Number(range.value), W = canvas.width, H = canvas.height;
    const px = x => 70 + (W - 115) * x / Math.PI;
    const py = y => H - 60 - (H - 110) * y / (Math.PI / 2);
    ctx.fillStyle = dark ? '#202023' : '#ffffff'; ctx.fillRect(0, 0, W, H);
    ctx.strokeStyle = dark ? '#92929b' : '#9a9a9a'; ctx.lineWidth = 1;
    ctx.beginPath(); ctx.moveTo(px(0), py(Math.PI / 2) - 10); ctx.lineTo(px(0), py(0)); ctx.lineTo(px(Math.PI) + 15, py(0)); ctx.stroke();
    ctx.fillStyle = dark ? '#eeeaea' : '#333333'; ctx.font = '19px sans-serif';
    ctx.fillText('0', px(0) - 18, py(0) + 27); ctx.fillText('π/2', px(Math.PI / 2) - 15, py(0) + 27); ctx.fillText('π', px(Math.PI) - 4, py(0) + 27);
    ctx.fillText('π/2', 22, py(Math.PI / 2) + 6); ctx.fillText('T', 28, 25); ctx.fillText('x', W - 24, H - 37);
    ctx.strokeStyle = dark ? '#b4b0ba' : '#767676'; ctx.setLineDash([8, 6]); ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(px(0), py(0)); ctx.lineTo(px(Math.PI / 2), py(Math.PI / 2)); ctx.lineTo(px(Math.PI), py(0)); ctx.stroke(); ctx.setLineDash([]);
    ctx.strokeStyle = dark ? '#ff8c84' : '#bf2b25'; ctx.lineWidth = 3; ctx.beginPath();
    for (let j = 0; j <= 700; j++) {
      const x = Math.PI * j / 700, y = temperature(x, t);
      if (j === 0) ctx.moveTo(px(x), py(y)); else ctx.lineTo(px(x), py(y));
    }
    ctx.stroke();
    document.getElementById('heat-time-value').textContent = t.toFixed(2);
    document.getElementById('heat-caption').textContent = `t=${t.toFixed(2)} · 중앙 온도 T(π/2,t)=${temperature(Math.PI / 2,t).toFixed(5)} · 점선: 초기 삼각형 / 실선: 현재 온도. 양 끝은 항상 0입니다.`;
  }
  range.addEventListener('input', draw);
  window.addEventListener('resize', draw);
  new MutationObserver(draw).observe(document.documentElement, { attributes: true, attributeFilter: ['data-mode'] });
  draw();
})();
