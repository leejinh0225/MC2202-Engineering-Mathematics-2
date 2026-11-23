(() => {
  const canvas = document.getElementById('ellipse-plot');
  const choice = document.getElementById('ellipse-direction');
  const caption = document.getElementById('ellipse-caption');
  const ctx = canvas.getContext('2d');
  if (!ctx) return;
  canvas.parentElement.hidden = false;

  function draw() {
    const positive = choice.value === 'positive';
    const style = getComputedStyle(document.documentElement);
    const color = name => style.getPropertyValue(name).trim();
    const width = canvas.clientWidth;
    if (!width) return;
    const height = Math.max(270, Math.round(width * 0.72));
    const density = window.devicePixelRatio || 1;
    const pxWidth = Math.round(width * density), pxHeight = Math.round(height * density);
    if (canvas.width !== pxWidth || canvas.height !== pxHeight) {
      canvas.width = pxWidth;
      canvas.height = pxHeight;
    }
    ctx.setTransform(density, 0, 0, density, 0, 0);
    const cx = width / 2, cy = height / 2;
    const unit = Math.min((width-40)/5.4, (height-48)/6);
    const ink = color('--ink'), accent = color('--crimson-deep');
    ctx.fillStyle = color('--canvas');
    ctx.fillRect(0, 0, width, height);
    ctx.font = width < 420 ? '13px sans-serif' : '18px sans-serif';
    ctx.lineWidth = 2;
    ctx.strokeStyle = color('--hairline-strong');
    ctx.beginPath();
    ctx.moveTo(8, cy); ctx.lineTo(width-8, cy);
    ctx.moveTo(cx, 10); ctx.lineTo(cx, height-10);
    ctx.stroke();
    ctx.fillStyle = ink;
    ctx.fillText('Re z', width-45, cy+24);
    ctx.fillText('Im z', cx+10, 18);
    ctx.fillText('0', cx-23, cy+23);

    ctx.lineWidth = 4;
    ctx.strokeStyle = accent;
    ctx.beginPath(); ctx.ellipse(cx, cy, unit, 3*unit, 0, 0, 2*Math.PI); ctx.stroke();
    const sign = positive ? -1 : 1;
    ctx.beginPath(); ctx.moveTo(cx+unit-10, cy-sign*12);
    ctx.lineTo(cx+unit, cy+sign*7); ctx.lineTo(cx+unit+10, cy-sign*12); ctx.stroke();

    for (const [x,y,label] of [[0,2,'2i'],[0,-2,'−2i'],[-2,0,'−2'],[2,0,'2']]) {
      const px = cx+x*unit, py = cy-y*unit, inside = x === 0;
      ctx.strokeStyle = ctx.fillStyle = inside ? accent : ink;
      ctx.lineWidth = 3;
      ctx.beginPath(); ctx.arc(px,py,4.5,0,2*Math.PI);
      if (inside) ctx.fill(); else ctx.stroke();
      ctx.fillStyle = ink;
      ctx.fillText(label,px+6,py-8);
    }
    caption.textContent = (positive ? '반시계방향' : '시계방향')+
      ' · 내부 극 ±2i · 유수의 합 −1/8 · 적분값 '+(positive ? '−πi/4' : '+πi/4');
  }
  choice.addEventListener('change', draw);
  new ResizeObserver(draw).observe(canvas);
  new MutationObserver(draw).observe(document.documentElement, {attributes:true, attributeFilter:['data-mode']});
  draw();
})();
