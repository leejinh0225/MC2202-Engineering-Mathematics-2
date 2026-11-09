"""Independent numeric checks of original Week 9-10 examples and delicate signs.

Uses Python's complex elementary functions and directional finite differences.
These finite samples complement, not replace, the algebra/proofs in the note.
"""
import cmath as c
import math as m
import hashlib
from pathlib import Path
from pypdf import PdfReader
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
checks=0
def close(a,b,tol=1e-9):
    global checks
    assert abs(a-b)<=tol*max(1,abs(b)),(a,b,abs(a-b))
    checks+=1
def derivative(f,z,answer):
    for theta in (0,m.pi/2,.7,2.1):
        h=1e-5*c.exp(1j*theta)
        close((f(z+h)-f(z-h))/(2*h),answer,2e-8)

# Original page 4: independently multiply the displayed quotient back.
a,b=8+3j,9-2j
for x,y in [(a+b,17+1j),(a-b,-1+5j),(a*b,78+11j),((66+43j)/85*b,a)]:close(x,y)
# Original pages 13,15,18 and 55: exact coordinates vs polar computation.
close(2*c.exp(1j*m.pi/6),m.sqrt(3)+1j)
close(2*c.exp(7j*m.pi/6),-m.sqrt(3)-1j)
close((-2+2j)*3j,-6-6j)
close((-2+2j)/(3j),2/3+2j/3)
for theta in (-2.3,-.3,0,.4,1.7):
    close(m.cos(3*theta),4*m.cos(theta)**3-3*m.cos(theta))
    close(m.sin(3*theta),3*m.sin(theta)-4*m.sin(theta)**3)
z=-m.sqrt(3)-1j
close(z**3,-8j);close(z**(-6),-1/64)
# Original pages 20-21: roots must be distinct and map to 1, not only on a circle.
for n in (3,4,5):
    roots=[c.exp(2j*m.pi*k/n) for k in range(n)]
    for root in roots: close(root**n,1)
    assert all(abs(roots[j]-roots[k])>1e-6 for j in range(n) for k in range(j))
    close(sum(roots),0)
close((1+3j)**2+3*(1+3j),-5+15j)
for z in (.2+.7j,-.4+1.2j,2-.5j):
    derivative(lambda w:w**3,z,3*z*z)
    derivative(lambda w:w*w+2j*w+3,z,2*(z+1j))
    derivative(lambda w:(w*w+2j*w+3)**4,z,8*(z*z+2j*z+3)**3*(z+1j))
    derivative(c.exp,z,c.exp(z))
    derivative(lambda w:c.exp(1j*w),z,1j*c.exp(1j*z))
    derivative(c.sqrt,z,1/(2*c.sqrt(z)))
    derivative(c.log,z,1/z)
    close(c.exp(z+2j*m.pi),c.exp(z))
    x,y=z.real,z.imag
    close(c.sin(z),m.sin(x)*m.cosh(y)+1j*m.cos(x)*m.sinh(y))
    close(c.cos(z),m.cos(x)*m.cosh(y)-1j*m.sin(x)*m.sinh(y))
    close(c.sin(1j*z),1j*c.sinh(z))
    close(c.cos(1j*z),c.cosh(z))
    close(c.cosh(z)**2-c.sinh(z)**2,1)
    t=.6-.2j
    close(c.sin(z+t),c.sin(z)*c.cos(t)+c.cos(z)*c.sin(t))
    close(c.cos(z+t),c.cos(z)*c.cos(t)-c.sin(z)*c.sin(t))
    close(c.sinh(z+t),c.sinh(z)*c.cosh(t)+c.cosh(z)*c.sinh(t))
    close(c.cosh(z+t),c.cosh(z)*c.cosh(t)+c.sinh(z)*c.sinh(t))

# Conjugation: two directional quotients disagree at every test point.
for z in (0,1+2j,-3+1j):
    h=1e-4
    close(((z+h).conjugate()-z.conjugate())/h,1)
    close(((z+1j*h).conjugate()-z.conjugate())/(1j*h),-1)
for k in range(-3,4):
    close(c.exp(.5*m.log(2)+1j*(m.pi/4+2*m.pi*k)),1+1j)
    for sign in (-1,1):
        close(c.sin(m.pi/2+2*m.pi*k+sign*1j*m.log(m.sqrt(2)+1)),m.sqrt(2))
close(c.log(-1+0j)*2,2j*m.pi);close(c.log((-1+0j)**2),0)
assert abs(c.log(-1+1e-9j)-c.log(-1-1e-9j))>6.28
# Page 51's sign: library inverse, inverse substitution and derivative agree.
atan=lambda z:.5j*c.log((1j+z)/(1j-z))
for z in (.2+.3j,-.5+.1j,.6-.4j):
    close(atan(z),c.atan(z));close(c.tan(atan(z)),z)
    derivative(atan,z,1/(1+z*z))
    derivative(c.asinh,z,1/c.sqrt(1+z*z))
    derivative(c.atanh,z,1/(1-z*z))
    derivative(c.acosh,z,1/(c.sqrt(z-1)*c.sqrt(z+1)))
    close(c.acosh(z),c.log(z+c.sqrt(z-1)*c.sqrt(z+1)))
    # All quadratic solutions, followed by logarithm, invert sinh/cosh.
    for sign in (-1,1):
        close(c.sinh(c.log(z+sign*c.sqrt(z*z+1))),z)
        close(c.cosh(c.log(z+sign*c.sqrt(z*z-1))),z)

# Page 54: exact radicals, polar/log calculation and squaring independently agree.
a=m.sqrt((m.sqrt(2)+1)/2);b=m.sqrt((m.sqrt(2)-1)/2)
close(a+1j*b,c.sqrt(1+1j));close((a+1j*b)**2,1+1j)
close(a,1.098684114,1e-9);close(b,.455089861,1e-9)
assert abs((1.09684+.45509j)**2-(1+1j))>.004
# Page 56's paths: axes agree but the diagonal gives a different constant.
for t in (1,.1,.001):
    close(t*0/(t*t),0);close(t*t/(2*t*t),.5)
# Page 57: compare actual function quotients in several directions on the axes.
def f(z):
    x,y=z.real,z.imag
    return x**3+3*x*y*y+1j*(y**3+3*x*x*y)
for z in (0,1,-2,1j,-2j): derivative(f,z,3*abs(z)**2)
for z in (1+1j,2-1j):
    h=1e-5
    dx=(f(z+h)-f(z-h))/(2*h)
    dy=(f(z+1j*h)-f(z-1j*h))/(2j*h)
    assert abs(dx-dy)>10
    checks+=1
# Original source byte identity and all original slide image frames.
pdf=ROOT/'site/materials/Week 9 - 10.pdf'
expected='eb2468739125d32b36595013a8e0bc3eeb01a0d01c6c030b349a77c36b17cbbd'
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==expected
original=Path.home()/'Downloads/Week 9 - 10.pdf'
if original.exists():assert original.read_bytes()==pdf.read_bytes()
assert len(PdfReader(pdf).pages)==58
slides=ROOT/'site/assets/slides/complex-numbers-functions'
assert len(list(slides.glob('slide-*.jpg')))==58
for n in range(1,59):
    with Image.open(slides/f'slide-{n:02}.jpg') as im:assert im.size==(1920,1080)
print(f'COMPLEX_MATH_OK independent_checks={checks} source_pages=58 source_sha256={expected}')
