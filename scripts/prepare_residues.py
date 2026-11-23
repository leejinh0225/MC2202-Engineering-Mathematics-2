"""Preserve the Week 13 PDF and center its native slide layout in the site frame."""
from pathlib import Path
import shutil
import subprocess
import sys
from PIL import Image
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / 'site/materials/Week 13.pdf'


def main():
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else PDF
    if len(PdfReader(source).pages) != 18:
        raise ValueError('Expected 18 pages in Week 13.pdf')
    work = ROOT / 'tmp/week13'
    dest = ROOT / 'site/assets/slides/residue-integration'
    work.mkdir(parents=True, exist_ok=True)
    dest.mkdir(parents=True, exist_ok=True)
    subprocess.run(['pdftoppm', '-scale-to', '1440', '-png', str(source), str(work/'p')], check=True)
    pages = [work/f'p-{n:02}.png' for n in range(1,19)]
    for n, path in enumerate(pages, 1):
        with Image.open(path) as page:
            frame = Image.new('RGB', (1920, 1080), page.getpixel((page.width-1, 0)) if n == 1 else 'white')
            frame.paste(page, ((1920-page.width)//2, (1080-page.height)//2))
            frame.save(dest/f'slide-{n:02}.jpg', quality=94, subsampling=0)
    for start in range(0, 18, 6):
        sheet = Image.new('RGB', (1560, 1755), 'white')
        for j, path in enumerate(pages[start:start+6]):
            with Image.open(path) as page:
                page.thumbnail((780,585))
                sheet.paste(page, ((j%2)*780,(j//2)*585))
        sheet.save(work/f'contact-{start//6+1}.jpg', quality=94)
    if source.resolve() != PDF.resolve():
        shutil.copyfile(source, PDF)


if __name__ == '__main__':
    main()
