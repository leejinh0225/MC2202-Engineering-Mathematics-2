"""Independent quadrature, initial/boundary data and PDE residual checks."""
from pathlib import Path
import hashlib
import numpy as np
from numpy.polynomial.legendre import leggauss

nodes,weights=leggauss(160)
checks=0
def close(actual,expected,tol=1e-10):
    global checks
    error=float(np.max(np.abs(np.asarray(actual)-np.asarray(expected))))
    assert error<tol,(error,tol)
    checks+=1

def integral(fn,a,b):
    return (b-a)/2*np.sum(weights*fn((b-a)/2*nodes+(a+b)/2))

def extended(x,L,k):
    r=(np.asarray(x)+L)%(2*L)-L
    return np.sign(r)*2*k/L*np.minimum(np.abs(r),L-np.abs(r))

for L,c,k in [(1.,1.,1.),(2.3,1.7,.4),(3.1,.6,-.7)]:
    for n in range(1,41):
        a=n*np.pi/L
        numeric=2/L*(integral(lambda x:2*k/L*x*np.sin(a*x),0,L/2)+integral(lambda x:2*k/L*(L-x)*np.sin(a*x),L/2,L))
        formula=8*k/(n*n*np.pi**2)*np.sin(n*np.pi/2)
        close(numeric,formula)
    xs=np.linspace(0,L,173)
    modes=2*np.arange(2048)+1
    coeff=8*k*(-1.)**np.arange(2048)/(np.pi**2*modes**2)
    for tau in [0,.13,.5,.81,1.,1.73,2.]:
        t=tau*L/c
        direct=(extended(xs+c*t,L,k)+extended(xs-c*t,L,k))/2
        series=(np.sin(np.outer(xs,modes*np.pi/L))*(coeff*np.cos(modes*np.pi*c*t/L))).sum(axis=1)
        close(series,direct,abs(k)*1.1e-4)
        close(direct[[0,-1]],[0,0])
    close(extended(xs,L,k),2*k/L*np.minimum(xs,L-xs))
    close((extended(xs+L/2,L,k)+extended(xs-L/2,L,k))/2,0)
    close((extended(xs+L,L,k)+extended(xs-L,L,k))/2,-extended(xs,L,k))
    # The kink has a nonzero right time derivative: initial velocity is an L2 trace.
    eps=1e-6
    center_after=(extended(L/2+c*eps,L,k)+extended(L/2-c*eps,L,k))/2
    close((center_after-k)/eps,-2*k*c/L,1e-8)
    # Initial velocity coefficients must be divided by lambda_n.
    v0=.73
    for n in range(1,9):
        lam=c*n*np.pi/L
        bstar=2/(L*lam)*integral(lambda x:v0*np.sin(2*np.pi*x/L)*np.sin(n*np.pi*x/L),0,L)
        close(bstar,v0/lam if n==2 else 0)
    # A smooth mode with nonzero initial displacement and velocity.
    n=3; a=n*np.pi/L; lam=c*a; b=.7; bs=-.3
    def mode(x,t): return (b*np.cos(lam*t)+bs*np.sin(lam*t))*np.sin(a*x)
    h=2e-5
    for x,t in [(L*.21,.3),(L*.47,.9),(L*.73,1.2)]:
        utt=(mode(x,t+h)-2*mode(x,t)+mode(x,t-h))/h**2
        uxx=(mode(x+h,t)-2*mode(x,t)+mode(x-h,t))/h**2
        close(utt,c*c*uxx,2e-5)
    close(mode(xs,0),b*np.sin(a*xs))
    close((mode(xs,h)-mode(xs,-h))/(2*h),lam*bs*np.sin(a*xs),1e-7)

# Whole-line d'Alembert integral: independently integrate g(s)=s^2.
for c in [.6,1.,2.1]:
    for x,t in [(-1.,.3),(.2,.8),(1.3,1.1)]:
        f=lambda z:z**3-2*z
        computed=(f(x+c*t)+f(x-c*t))/2+integral(lambda s:s*s,x-c*t,x+c*t)/(2*c)
        explicit=x**3-2*x+3*x*c*c*t*t+t*x*x+c*c*t**3/3
        close(computed,explicit)
        close(6*x*c*c+2*c*c*t,c*c*(6*x+2*t))

# Characteristic roots with the source's 2B convention.
for A,B,C in [(1,2,1),(4,0,-1),(2,-3,1),(3,3,3)]:
    delta=B*B-A*C
    roots=[(B+np.sqrt(delta))/A,(B-np.sqrt(delta))/A]
    for m in roots: close(A*m*m-2*B*m+C,0)
    close(np.prod(roots),C/A)
for y in [-2.,0.,2.]: close(0-1*y,-y)

source=Path('C:/Users/Jinhyeong/Downloads/PDE - I.pdf')
target=Path(__file__).resolve().parents[1]/'site/materials/PDE - I.pdf'
assert hashlib.sha256(source.read_bytes()).digest()==hashlib.sha256(target.read_bytes()).digest()
print(f'PDE_MATH_OK independent_checks={checks} source_pdf_identical=True')
