(() => {
  const button = document.getElementById('mode-toggle');
  const status = document.getElementById('mode-status');
  function sync() {
    const beginner = document.documentElement.dataset.mode === 'newbie';
    if (button) {
      button.setAttribute('aria-pressed', String(beginner));
      button.textContent = beginner ? '뉴비 모드 켜짐 · 기본으로' : '뉴비 모드 켜기';
    }
    if (status) status.textContent = beginner ? '뉴비 모드 · 다크 화면 + 기초 부연 설명' : '기본 모드 · 밝은 화면';
    drawWave();
  }
  button?.addEventListener('click', () => {
    const mode = document.documentElement.dataset.mode === 'newbie' ? 'standard' : 'newbie';
    document.documentElement.dataset.mode = mode;
    document.documentElement.style.colorScheme = mode === 'newbie' ? 'dark' : 'light';
    try { localStorage.setItem('mc2202-reading-mode',mode); } catch (_) {}
    sync();
    window.dispatchEvent(new Event('resize'));
  });
  window.addEventListener('storage', e => {
    if (e.key !== 'mc2202-reading-mode') return;
    document.documentElement.dataset.mode = e.newValue === 'newbie' ? 'newbie' : 'standard';
    document.documentElement.style.colorScheme = e.newValue === 'newbie' ? 'dark' : 'light';
    sync();
  });
  function drawWave() {
    const canvas=document.getElementById('fourier-canvas');
    const range=document.getElementById('term-count');
    if (!canvas || !range) return;
    const ctx=canvas.getContext('2d'); if (!ctx) return;
    const dark=document.documentElement.dataset.mode==='newbie';
    const M=Number(range.value), W=canvas.width,H=canvas.height;
    ctx.fillStyle=dark?'#202023':'#ffffff';ctx.fillRect(0,0,W,H);
    const px=x=>50+(x+Math.PI)/(2*Math.PI)*(W-90), py=y=>H/2-y*125;
    ctx.strokeStyle=dark?'#727278':'#c8c8c8';ctx.lineWidth=1;
    ctx.beginPath();ctx.moveTo(50,py(0));ctx.lineTo(W-40,py(0));ctx.moveTo(px(0),28);ctx.lineTo(px(0),H-30);ctx.stroke();
    ctx.font='18px sans-serif';ctx.fillStyle=dark?'#e8e5e5':'#4d4d4d';
    ctx.fillText('−π',46,H-18);ctx.fillText('0',px(0)-5,H-18);ctx.fillText('π',W-48,H-18);ctx.fillText('+1',12,py(1)+5);ctx.fillText('−1',12,py(-1)+5);
    ctx.strokeStyle=dark?'#e8e5e5':'#171717';ctx.lineWidth=2;ctx.setLineDash([7,5]);
    ctx.beginPath();ctx.moveTo(px(-Math.PI),py(-1));ctx.lineTo(px(0),py(-1));ctx.moveTo(px(0),py(1));ctx.lineTo(px(Math.PI),py(1));ctx.stroke();ctx.setLineDash([]);
    ctx.strokeStyle=dark?'#ff8c84':'#bf2b25';ctx.lineWidth=3;ctx.beginPath();
    for(let j=0;j<=1800;j++){
      const x=-Math.PI+2*Math.PI*j/1800;let sum=0;
      for(let k=0;k<M;k++){const n=2*k+1;sum+=4/Math.PI*Math.sin(n*x)/n;}
      if(j===0)ctx.moveTo(px(x),py(sum));else ctx.lineTo(px(x),py(sum));
    }ctx.stroke();
    document.getElementById('term-output').textContent=String(M);
    document.getElementById('wave-caption').textContent=`${M}항: 최대 주파수는 ${2*M-1}차입니다. 점프점의 급수 합은 0입니다.`;
  }
  document.getElementById('term-count')?.addEventListener('input',drawWave);
  sync();
})();
