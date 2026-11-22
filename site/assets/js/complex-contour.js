(() => {
  const canvas = document.querySelector('#contour-plot');
  const choice = document.querySelector('#contour-choice');
  const caption = document.querySelector('#contour-result');
  const ctx = canvas.getContext('2d');
  if (!ctx) return;
  function draw() {
    const shifted = choice.value === 'shifted';
    const yCenter = shifted ? 1 : 0;
    const radius = shifted ? 1 : 2;
    const style = getComputedStyle(document.documentElement);
    const color = name => style.getPropertyValue(name).trim();
    const ox = canvas.width/2, oy = canvas.height/2, scale = 101;
    ctx.fillStyle = color('--canvas');
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.lineWidth = 2;
    ctx.strokeStyle = color('--hairline-strong');
    ctx.beginPath();
    ctx.moveTo(42, oy); ctx.lineTo(canvas.width-42, oy);
    ctx.moveTo(ox, 18); ctx.lineTo(ox, canvas.height-18);
    ctx.stroke();
    ctx.fillStyle = color('--body');
    ctx.font = '20px sans-serif';
    ctx.fillText('Re z', canvas.width-82, oy+27);
    ctx.fillText('Im z', ox+12, 30);
    ctx.fillText('0', ox-20, oy+23);
    const cy = oy-yCenter*scale, r = radius*scale;
    ctx.strokeStyle = color('--crimson-deep');
    ctx.lineWidth = 4;
    ctx.beginPath(); ctx.arc(ox, cy, r, 0, 2*Math.PI); ctx.stroke();
    // On the right edge a counterclockwise path moves upward.
    ctx.beginPath(); ctx.moveTo(ox+r-8, cy+8);
    ctx.lineTo(ox+r, cy-7); ctx.lineTo(ox+r+8, cy+8); ctx.stroke();
    for (const sign of [1,-1]) {
      const y = sign*Math.SQRT2, py = oy-y*scale;
      const inside = Math.abs(y-yCenter) < radius;
      ctx.beginPath(); ctx.arc(ox, py, 7, 0, 2*Math.PI);
      ctx.strokeStyle = ctx.fillStyle = color(inside ? '--crimson-deep' : '--mute');
      if (inside) ctx.fill(); else ctx.stroke();
      ctx.fillStyle = color('--ink');
      ctx.fillText((sign===1?'i√2':'−i√2')+' · '+(inside?'내부':'외부'), ox+15, py+6);
    }
    caption.textContent = shifted ? '|z − i| = 1 · i√2만 내부 · 적분값 2πi' : '|z| = 2 · 두 점 모두 내부 · 적분값 4πi';
  }
  choice.addEventListener('change',draw);
  new MutationObserver(draw).observe(document.documentElement, {attributes:true, attributeFilter:['data-mode']});
  draw();
})();
