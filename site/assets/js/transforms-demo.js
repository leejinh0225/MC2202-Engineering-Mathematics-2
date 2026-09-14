(() => {
  const integralCanvas = document.getElementById('integral-demo');
  const dftCanvas = document.getElementById('dft-demo');
  if (!integralCanvas || !dftCanvas) return;
  const cutoff = document.getElementById('integral-cutoff');
  const one = document.getElementById('dft-amplitude-one');
  const three = document.getElementById('dft-amplitude-three');
  // Cumulative Simpson quadrature for Si, including the removable value sinc(0)=1.
  const step = 0.01, siTable = new Float64Array(19202);
  const sinc = x => x === 0 ? 1 : Math.sin(x) / x;
  for (let j = 1; j < siTable.length; j++) {
    const x = j * step;
    siTable[j] = siTable[j-1] + step / 6 * (sinc(x-step) + 4*sinc(x-step/2) + sinc(x));
  }
  function si(x) {
    const a = Math.abs(x) / step, lo = Math.floor(a), t = a-lo;
    return Math.sign(x) * (siTable[lo]*(1-t) + siTable[lo+1]*t);
  }
  function palette() {
    return document.documentElement.dataset.mode === 'newbie'
      ? {bg:'#18181b', text:'#f2eeee', grid:'#727278', accent:'#ff8c84', second:'#9ccaff'}
      : {bg:'#ffffff', text:'#222222', grid:'#b9b9bd', accent:'#b52620', second:'#245ba2'};
  }
  function prepare(canvas) {
    const ctx = canvas.getContext('2d');
    if (!ctx) return null;
    const p = palette();
    ctx.fillStyle = p.bg; ctx.fillRect(0,0,canvas.width,canvas.height);
    ctx.font = '24px sans-serif'; ctx.lineWidth = 1.5;
    ctx.setLineDash([]); ctx.textAlign = 'left';
    return {ctx,p};
  }
  function line(ctx,x0,y0,x1,y1,color,width=1.5) {
    ctx.strokeStyle=color;ctx.lineWidth=width;ctx.beginPath();ctx.moveTo(x0,y0);ctx.lineTo(x1,y1);ctx.stroke();
  }
  function drawIntegral() {
    const state=prepare(integralCanvas); if (!state) return;
    const {ctx,p}=state, R=Number(cutoff.value);
    const px=x=>80+(x+2)*205, py=y=>325-y*230;
    const f=x=>(si(R*(1+x))+si(R*(1-x)))/Math.PI;
    line(ctx,80,py(0),900,py(0),p.grid);line(ctx,px(0),28,px(0),350,p.grid);
    ctx.fillStyle=p.text;
    for (const x of [-2,-1,0,1,2]) { ctx.fillText(String(x),px(x)-12,385); }
    for (const y of [0,0.5,1]) { ctx.fillText(String(y),15,py(y)+8); }
    ctx.fillText('x',915,385);
    ctx.setLineDash([10,7]);
    line(ctx,px(-2),py(0),px(-1),py(0),p.text,2);
    line(ctx,px(-1),py(1),px(1),py(1),p.text,2);
    line(ctx,px(1),py(0),px(2),py(0),p.text,2);
    ctx.setLineDash([]);ctx.strokeStyle=p.accent;ctx.lineWidth=3;ctx.beginPath();
    for (let j=0;j<=1200;j++) {const x=-2+4*j/1200; j ? ctx.lineTo(px(x),py(f(x))) : ctx.moveTo(px(x),py(f(x)));}
    ctx.stroke();
    for (const x of [-1,1]) {ctx.fillStyle=p.second;ctx.beginPath();ctx.arc(px(x),py(0.5),6,0,2*Math.PI);ctx.fill();}
    document.getElementById('integral-cutoff-value').textContent=String(R);
    document.getElementById('integral-demo-caption').textContent=`R=${R} · 점선: 원본 펄스 · 실선: 유한 주파수 복원. x=0에서 ${f(0).toFixed(4)}, x=1에서 ${f(1).toFixed(4)}입니다. 경계의 점 표시는 극한 목표값 0.5입니다.`;
    integralCanvas.setAttribute('aria-label',document.getElementById('integral-demo-caption').textContent);
  }
  function drawDFT() {
    const state=prepare(dftCanvas); if (!state) return;
    const {ctx,p}=state, a=Number(one.value),b=Number(three.value),N=8;
    const signal=x=>a*Math.sin(x)+b*Math.sin(3*x);
    const samples=Array.from({length:N},(_,k)=>signal(2*Math.PI*k/N));
    const X=Array.from({length:N},(_,n)=>{
      let real=0,imag=0;
      for(let k=0;k<N;k++){real+=samples[k]*Math.cos(2*Math.PI*n*k/N);imag-=samples[k]*Math.sin(2*Math.PI*n*k/N);}
      const magnitude=Math.hypot(real,imag);return magnitude<1e-10?0:magnitude;
    });
    const px=x=>85+x/(2*Math.PI)*810,py=y=>133-y*22;
    ctx.fillStyle=p.text;ctx.fillText('f(x) = a sin x + b sin 3x',85,30);
    line(ctx,85,py(0),895,py(0),p.grid);
    ctx.strokeStyle=p.accent;ctx.lineWidth=3;ctx.beginPath();
    for(let j=0;j<=800;j++){const x=2*Math.PI*j/800;j?ctx.lineTo(px(x),py(signal(x))):ctx.moveTo(px(x),py(signal(x)));}ctx.stroke();
    for(let k=0;k<N;k++){ctx.fillStyle=p.second;ctx.beginPath();ctx.arc(px(2*Math.PI*k/N),py(samples[k]),5,0,2*Math.PI);ctx.fill();}
    ctx.fillStyle=p.text;ctx.fillText('0',80,240);ctx.fillText('π',px(Math.PI)-8,240);ctx.fillText('2π',870,240);
    ctx.fillText('|Xₙ| · N = 8',85,286);
    const bx=n=>130+(n+4)*100,by=y=>444-y*17;
    line(ctx,85,by(0),895,by(0),p.grid);
    for(const height of [4,8]) {line(ctx,85,by(height),895,by(height),p.grid,1);ctx.fillStyle=p.text;ctx.fillText(String(height),42,by(height)+8);}
    for(let n=-4;n<=3;n++){
      const mag=X[(n+N)%N];line(ctx,bx(n),by(0),bx(n),by(mag),p.accent,4);
      ctx.fillStyle=p.accent;ctx.beginPath();ctx.arc(bx(n),by(mag),6,0,2*Math.PI);ctx.fill();
      ctx.fillStyle=p.text;ctx.fillText(String(n),bx(n)-13,485);
    }
    document.getElementById('dft-one-value').textContent=a.toFixed(1);
    document.getElementById('dft-three-value').textContent=b.toFixed(1);
    document.getElementById('dft-demo-caption').textContent=`N=8 · ±1번 막대 크기 ${X[1].toFixed(1)}, ±3번 막대 크기 ${X[3].toFixed(1)}. 실제 두 사인의 진폭은 각각 ${a.toFixed(1)}, ${b.toFixed(1)}입니다. 점은 8개 표본, 실선은 표본을 얻은 원래 함수입니다.`;
    dftCanvas.setAttribute('aria-label',document.getElementById('dft-demo-caption').textContent);
  }
  cutoff.addEventListener('input',drawIntegral);
  one.addEventListener('input',drawDFT);three.addEventListener('input',drawDFT);
  const redraw=()=>{drawIntegral();drawDFT();};
  new MutationObserver(redraw).observe(document.documentElement,{attributes:true,attributeFilter:['data-mode']});
  redraw();
})();
