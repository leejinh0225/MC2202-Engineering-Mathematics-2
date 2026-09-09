from pathlib import Path
from pypdf import PdfReader
from PIL import Image, ImageOps, ImageDraw
import subprocess, shutil, json, sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(sys.argv[1]).resolve() if len(sys.argv)>1 else ROOT/'site/materials/Fourier series.pdf'
SKILL = Path.home()/'.codex/skills/dynamics-lecture-note'
slides = ROOT / 'site/assets/slides/fourier'
qa = ROOT / 'tmp/qa'
for folder in [slides, qa, ROOT/'site/assets/css', ROOT/'site/assets/js', ROOT/'site/materials', ROOT/'site/templates']:
    folder.mkdir(parents=True, exist_ok=True)
if SOURCE.resolve() != (ROOT/'site/materials/Fourier series.pdf').resolve():
    shutil.copy2(SOURCE, ROOT/'site/materials/Fourier series.pdf')
for src, dest in [('styles.css','site/assets/css/styles.css'), ('site.js','site/assets/js/site.js'), ('lecture-page.template.html','site/templates/lecture-page.template.html')]:
    shutil.copy2(SKILL/'assets'/src, ROOT/dest)
reader = PdfReader(SOURCE)
(qa/'source-text.json').write_text(json.dumps([p.extract_text() for p in reader.pages], ensure_ascii=False, indent=2), encoding='utf-8')
subprocess.run(['pdftoppm','-jpeg','-scale-to-x','1920','-scale-to-y','1080','-jpegopt','quality=90', str(SOURCE),str(slides/'slide')],check=True)
files=sorted(slides.glob('slide-*.jpg'))
for batch in range(0,len(files),6):
    sheet=Image.new('RGB',(1440,1296),'#dddddd')
    draw=ImageDraw.Draw(sheet)
    for j,file in enumerate(files[batch:batch+6]):
        with Image.open(file) as im:
            im.thumbnail((720,405))
            x=(j%2)*720; y=(j//2)*432
            sheet.paste(im,(x,y+24)); draw.text((x+12,y+4),f'PDF PAGE {batch+j+1}',fill='black')
    sheet.save(qa/f'contact-{batch//6+1:02}.jpg',quality=92)
print(f'Prepared {len(files)} slides and {len(range(0,len(files),6))} contact sheets')
