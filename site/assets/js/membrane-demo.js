(() => {
  const canvas = document.getElementById('membrane-demo');
  const range = document.getElementById('membrane-time');
  if (!canvas || !range) return;
  // Source page 10; y = 1 ft. Both odd indices run from 1 through 79.
  const modes = Array.from({length: 40}, (_, j) => 2 * j + 1);
  const scale = 409.6 / Math.PI ** 6;
  function amplitudes(t) {
    return modes.map(m => scale / m ** 3 * modes.reduce((sum, n, j) =>
      sum + (j % 2 ? -1 : 1) * Math.cos(Math.PI * Math.sqrt(5) / 4 * Math.sqrt(m*m + 4*n*n) * t) / n ** 3, 0));
  }
  function displacement(x, t, coeff) {
    if (t === 0) return 0.1 * x * (4 - x);
    return modes.reduce((sum, m, j) => sum + coeff[j] * Math.sin(m * Math.PI * x / 4), 0);
  }
  function draw() {
    const ctx = canvas.getContext('2d');
    if (!ctx) return;
    const t = Number(range.value), coeff = amplitudes(t), W = canvas.width, H = canvas.height;
    const dark = document.documentElement.dataset.mode === 'newbie';
    const px = x => 78 + (W - 125) * x / 4, py = u => H/2 - u * 420;
    ctx.fillStyle = dark ? '#202023' : '#ffffff'; ctx.fillRect(0,0,W,H);
    ctx.font = '19px sans-serif'; ctx.fillStyle = dark ? '#eeeaea' : '#333333';
    ctx.strokeStyle = dark ? '#66666e' : '#cccccc'; ctx.lineWidth = 1;
    for (const u of [-0.4,-0.2,0,0.2,0.4]) {
      ctx.beginPath(); ctx.moveTo(px(0),py(u)); ctx.lineTo(px(4),py(u)); ctx.stroke();
      ctx.fillText(u.toFixed(1), 25, py(u)+6);
    }
    for (const x of [0,1,2,3,4]) ctx.fillText(String(x),px(x)-5,H-27);
    ctx.fillText('u (ft)',20,30); ctx.fillText('x (ft) · y = 1 ft',W-190,H-2);
    ctx.beginPath(); ctx.moveTo(px(0),py(-0.4)); ctx.lineTo(px(0),py(0.4)); ctx.stroke();
    const curve = (fn,color,dashed) => {
      ctx.strokeStyle=color; ctx.lineWidth=dashed?2:3; ctx.setLineDash(dashed?[8,6]:[]); ctx.beginPath();
      for (let j=0;j<=600;j++) { const x=4*j/600; if(j===0)ctx.moveTo(px(x),py(fn(x)));else ctx.lineTo(px(x),py(fn(x))); }
      ctx.stroke(); ctx.setLineDash([]);
    };
    curve(x=>0.1*x*(4-x),dark?'#b4b0ba':'#767676',true);
    curve(x=>displacement(x,t,coeff),dark?'#ff8c84':'#bf2b25',false);
    document.getElementById('membrane-time-value').textContent=t.toFixed(2);
    document.getElementById('membrane-caption').textContent=`t=${t.toFixed(2)} s · 중앙 변위 u(2,1,t)=${displacement(2,t,coeff).toFixed(5)} ft · 점선: 처음 / 실선: 현재. 1.6초는 기본 모드의 주기이며 전체 해의 반복 주기는 아닙니다.`;
  }
  range.addEventListener('input',draw);
  new MutationObserver(draw).observe(document.documentElement,{attributes:true,attributeFilter:['data-mode']});
  draw();
})();
