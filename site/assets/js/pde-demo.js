/* Independent finite Fourier sum and odd-periodic d'Alembert solution. */
(() => {
  const canvas = document.getElementById('wave-demo');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  if (!ctx) return;
  const time = document.getElementById('wave-time');
  const terms = document.getElementById('wave-terms');
  function extension(z) {
    const r = ((z + 1) % 2 + 2) % 2 - 1;
    return Math.sign(r) * 2 * Math.min(Math.abs(r), 1 - Math.abs(r));
  }
  function draw() {
    const tau = Number(time.value), count = Number(terms.value);
    const dark = document.documentElement.dataset.mode === 'newbie';
    const ink = dark ? '#dde7f4' : '#29394b';
    const grid = dark ? '#47566d' : '#cbd5e1';
    const blue = dark ? '#75caff' : '#0876b9';
    const orange = dark ? '#ffbd80' : '#b54a14';
    const x0=70, y0=215, w=850, scale=145;
    ctx.clearRect(0,0,960,430);
    ctx.fillStyle=dark?'#152034':'#f8fafc'; ctx.fillRect(0,0,960,430);
    ctx.font='18px system-ui'; ctx.fillStyle=ink; ctx.strokeStyle=grid; ctx.lineWidth=1;
    for(const v of [-1,0,1]) { const y=y0-v*scale; ctx.beginPath(); ctx.moveTo(x0,y); ctx.lineTo(x0+w,y); ctx.stroke(); ctx.fillText(String(v),28,y+6); }
    for(const x of [0,0.25,0.5,0.75,1]) { const px=x0+x*w; ctx.beginPath(); ctx.moveTo(px,65); ctx.lineTo(px,370); ctx.stroke(); ctx.fillText(String(x),px-10,401); }
    ctx.fillText('u/k',18,30); ctx.fillText('x/L',887,424);
    const exact=[],approx=[]; let error=0;
    for(let i=0;i<=800;i++) {
      const x=i/800;
      const d=(extension(x+tau)+extension(x-tau))/2;
      let s=0;
      for(let m=0;m<count;m++) { const n=2*m+1; s+=8/Math.PI**2 * (-1)**m/n**2 * Math.sin(n*Math.PI*x)*Math.cos(n*Math.PI*tau); }
      exact.push(d); approx.push(s); error=Math.max(error,Math.abs(s-d));
    }
    function line(values,color,dash,width) {
      ctx.strokeStyle=color; ctx.setLineDash(dash); ctx.lineWidth=width; ctx.beginPath();
      values.forEach((v,i)=>{ const x=x0+w*i/800,y=y0-scale*v; if(i===0)ctx.moveTo(x,y); else ctx.lineTo(x,y); });ctx.stroke();
    }
    line(exact,orange,[9,6],4); line(approx,blue,[],2.5); ctx.setLineDash([]);
    ctx.font='17px system-ui';ctx.fillStyle=blue;ctx.fillText('Fourier (finite sum)',260,30);ctx.fillStyle=orange;ctx.fillText("D’Alembert (exact)",575,30);
    document.getElementById('wave-time-value').value=tau.toFixed(2);
    document.getElementById('wave-terms-value').value=String(count);
    const phase=Math.abs(tau-0.5)<0.001||Math.abs(tau-1.5)<0.001?'수평선을 통과하는 순간입니다. 높이가 0이어도 속도는 0이 아닙니다.':Math.abs(tau-1)<0.001?'처음 삼각형이 아래로 뒤집힌 상태입니다.':tau===0||tau===2?'처음 삼각형 모양입니다.':'파동이 고정된 끝에서 반사되며 진동합니다.';
    document.getElementById('wave-caption').textContent=`τ=${tau.toFixed(2)} · 홀수 모드 ${count}개 (최고 n=${2*count-1}) · 801개 표본에서 두 해의 최대 높이 차이 ${error.toFixed(5)}. ${phase}`;
  }
  time.addEventListener('input',draw);terms.addEventListener('input',draw);
  new MutationObserver(draw).observe(document.documentElement,{attributes:true,attributeFilter:['data-mode']});
  draw();
})();
