"""Preserve the PDE II PDF and all 22 source pages without stretching."""
from pathlib import Path
import hashlib
import shutil
import subprocess
from PIL import Image, ImageOps, ImageDraw
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path('C:/Users/Jinhyeong/Downloads/PDE - II.pdf')

def main():
    work = ROOT / 'tmp/pde2'
    dest = ROOT / 'site/assets/slides/pde-ii'
    work.mkdir(parents=True, exist_ok=True)
    dest.mkdir(parents=True, exist_ok=True)
    reader = PdfReader(SOURCE)
    assert len(reader.pages) == 22
    poppler = shutil.which('pdftoppm') or str(Path.home() / '.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe')
    subprocess.run([poppler, '-scale-to', '1440', '-jpeg', '-jpegopt', 'quality=94', str(SOURCE), str(work/'page')], check=True)
    for n in range(1, 23):
        page = Image.open(work/f'page-{n:02}.jpg').convert('RGB')
        page = ImageOps.contain(page, (1920, 1080), Image.Resampling.LANCZOS)
        frame = Image.new('RGB', (1920, 1080), page.getpixel((page.width-1, 0)) if n == 1 else 'white')
        frame.paste(page, ((1920-page.width)//2, (1080-page.height)//2))
        frame.save(dest/f'slide-{n:02}.jpg', quality=94, subsampling=0)
    for start in range(1, 23, 6):
        sheet = Image.new('RGB', (1440, 3*565), '#dce0e5')
        draw = ImageDraw.Draw(sheet)
        for j, n in enumerate(range(start, min(start+6, 23))):
            img = Image.open(work/f'page-{n:02}.jpg')
            img.thumbnail((704, 528))
            x, y = (j%2)*720+8, (j//2)*565+27
            sheet.paste(img, (x,y))
            draw.text((x,y-20), f'PDF PAGE {n:02}', fill='black')
        sheet.save(work/f'contact-{(start-1)//6+1:02}.jpg', quality=92)
    target = ROOT/'site/materials/PDE - II.pdf'
    shutil.copy2(SOURCE, target)
    digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    assert digest(SOURCE) == digest(target)
    print('PDE_II_SOURCE_OK pages=22 frame=1920x1080 sha256='+digest(target))

if __name__ == '__main__':
    main()
