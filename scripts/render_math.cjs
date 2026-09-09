const fs = require('fs');
const path = require('path');
const katex = require('../tmp/katex/package/dist/katex.js');
const file = path.join(__dirname, '../site/fourier-series.html');
let count=0;
let content=fs.readFileSync(file,'utf8').replace(/<div class="math-block" data-tex="([\s\S]*?)"><\/div>/g, (_,encoded)=>{
  const tex=encoded.replace(/&quot;/g,'"').replace(/&#x27;/g,"'").replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&amp;/g,'&');
  count++;
  return '<div class="math-block">'+katex.renderToString(tex,{displayMode:true,throwOnError:true,output:'htmlAndMathml',strict:'error'})+'</div>';
});
fs.writeFileSync(file,content);
console.log('STATIC_MATH_OK equations='+count);
