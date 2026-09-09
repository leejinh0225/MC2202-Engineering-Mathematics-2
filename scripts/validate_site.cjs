const fs=require('fs'),path=require('path'),assert=require('assert');
const root=path.resolve(__dirname,'../site');
let links=0;
for(const name of ['index.html','downloads.html','fourier-series.html']){
  const html=fs.readFileSync(path.join(root,name),'utf8');
  const ids=[...html.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]);
  assert.equal(ids.length,new Set(ids).size,`${name}: duplicate ID`);
  assert(!/\{\{[A-Z_]+\}\}|data-tex=|katex-error/.test(html),`${name}: unresolved content`);
  assert(!/에델|노이슈반트|마스터|메이드/.test(html),`${name}: private persona text`);
  for(const m of html.matchAll(/\b(?:src|href)="([^"]+)"/g)){
    const url=m[1];
    if(/^(https?:|mailto:|data:)/.test(url))continue;
    if(url.startsWith('#')){assert(ids.includes(url.slice(1)),`${name}: missing ${url}`);continue;}
    const target=path.resolve(root,decodeURIComponent(url.split(/[?#]/)[0]));
    assert(fs.existsSync(target),`${name}: missing ${url}`);links++;
  }
  if(name==='fourier-series.html'){
    assert.equal((html.match(/class="source-section"/g)||[]).length,48);
    assert.equal((html.match(/class="card newbie-note"/g)||[]).length,44);
    assert.equal((html.match(/class="katex"/g)||[]).length,122);
    const ordered=['overview','concept-map','concept-summary',...Array.from({length:48},(_,i)=>`slide-${String(i+1).padStart(2,'0')}`),'exam-english','glossary','asr-log','sources'];
    let previous=-1;
    for(const id of ordered){const index=html.indexOf(`id="${id}"`);assert(index>previous,`wrong order ${id}`);previous=index;}
    assert(/class="editorial-section" id="exam-english"/.test(html));
    for(let i=1;i<=48;i++){
      const name=`slide-${String(i).padStart(2,'0')}.jpg`;
      const jpeg=fs.readFileSync(path.join(root,'assets/slides/fourier',name));
      let size;
      for(let p=2;p<jpeg.length;){
        if(jpeg[p]!==0xff){p++;continue;}
        const mark=jpeg[p+1];p+=2;
        if(mark===0xd8||mark===0xd9)continue;
        const length=jpeg.readUInt16BE(p);
        if([0xc0,0xc1,0xc2].includes(mark)){size=[jpeg.readUInt16BE(p+5),jpeg.readUInt16BE(p+3)];break;}
        p+=length;
      }
      assert.deepEqual(size,[1920,1080],`${name}: unexpected dimensions`);
    }
  }
}
console.log(`SITE_VALIDATION_OK pages=3 slides=48 newbie_cards=44 equations=122 local_links=${links}`);
