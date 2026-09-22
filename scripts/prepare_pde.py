"""Preserve all 4:3 source pages inside the established 1920x1080 frame."""
from pathlib import Path
import hashlib
import shutil
import subprocess
from PIL import Image
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
SOURCE=Path('C:/Users/Jinhyeong/Downloads/PDE - I.pdf')
TMP=ROOT/'tmp/pde1'
DEST=ROOT/'site/assets/slides/pde-i'

def main():
    reader=PdfReader(SOURCE)
    assert len(reader.pages)==22
    assert all(abs(float(p.mediabox.width)/float(p.mediabox.height)-4/3)<1e-8 for p in reader.pages)
    TMP.mkdir(parents=True,exist_ok=True)
    DEST.mkdir(parents=True,exist_ok=True)
    subprocess.run(['pdftoppm','-scale-to-x','1440','-scale-to-y','1080','-jpeg','-jpegopt','quality=92',str(SOURCE),str(TMP/'page')],check=True)
    for n in range(1,23):
        original=Image.open(TMP/f'page-{n:02}.jpg').convert('RGB')
        assert original.size==(1440,1080)
        bg=original.getpixel((1439,0)) if n==1 else (255,255,255)
        frame=Image.new('RGB',(1920,1080),bg)
        frame.paste(original,(240,0))
        frame.save(DEST/f'slide-{n:02}.jpg',quality=94,subsampling=0)
    target=ROOT/'site/materials/PDE - I.pdf'
    shutil.copy2(SOURCE,target)
    digest=lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    assert digest(SOURCE)==digest(target)
    print('PDE_SOURCE_OK pages=22 frame=1920x1080 preserved_aspect=4:3 sha256='+digest(target))

if __name__=='__main__': main()
