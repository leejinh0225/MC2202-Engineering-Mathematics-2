/* Original slide examples only: cube, fourth and fifth roots of unity. */
(() => {
  const canvas=document.getElementById('roots-demo');
  const choice=document.getElementById('roots-order');
  if(!canvas || !choice) return;
  const ctx=canvas.getContext('2d');
  if(!ctx) return;
  function draw() {
    const n=Number(choice.value), w=canvas.width, h=canvas.height;
    const dark=document.documentElement.dataset.mode==='newbie';
    const bg=dark?'#101827':'#f8fafc', fg=dark?'#eef2ff':'#172438';
    const grid=dark?'#79869b':'#66758c', accent=dark?'#9cceff':'#1456a0';
    const cx=w/2, cy=h/2, r=215;
    ctx.fillStyle=bg;ctx.fillRect(0,0,w,h);ctx.lineWidth=1.5;ctx.strokeStyle=grid;
    ctx.beginPath();ctx.moveTo(cx-r-65,cy);ctx.lineTo(cx+r+65,cy);ctx.moveTo(cx,cy-r-45);ctx.lineTo(cx,cy+r+45);ctx.stroke();
    ctx.beginPath();ctx.arc(cx,cy,r,0,2*Math.PI);ctx.stroke();
    ctx.font='20px sans-serif';ctx.fillStyle=fg;ctx.fillText('Re',cx+r+70,cy+6);ctx.fillText('Im',cx+12,cy-r-40);ctx.fillText('0',cx-22,cy+24);
    const pts=Array.from({length:n},(_,k)=>[cx+r*Math.cos(2*Math.PI*k/n),cy-r*Math.sin(2*Math.PI*k/n)]);
    ctx.setLineDash([7,6]);ctx.beginPath();pts.forEach(([x,y],k)=>k?ctx.lineTo(x,y):ctx.moveTo(x,y));ctx.closePath();ctx.stroke();ctx.setLineDash([]);
    pts.forEach(([x,y],k)=>{
      ctx.fillStyle=accent;ctx.beginPath();ctx.arc(x,y,7,0,2*Math.PI);ctx.fill();
      const angle=2*Math.PI*k/n, lx=cx+(r+34)*Math.cos(angle),ly=cy-(r+34)*Math.sin(angle);
      ctx.fillStyle=fg;ctx.textAlign='center';ctx.fillText(`k=${k}`,lx,ly+7);
    });
    ctx.textAlign='left';
    const caption=`n=${n} · 각 간격 2π/${n} · k=0,…,${n-1} · 모든 근의 크기는 1이고 ${n}제곱하면 1입니다.`;
    document.getElementById('roots-caption').textContent=caption;
    canvas.setAttribute('aria-label',caption);
  }
  choice.addEventListener('change',draw);
  new MutationObserver(draw).observe(document.documentElement,{attributes:true,attributeFilter:['class','data-mode']});
  draw();
})();
