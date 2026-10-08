"""Independent quadrature, finite-difference PDE and source-data checks for PDE II."""
from pathlib import Path
import hashlib
import math
import numpy as np
from numpy.polynomial.legendre import leggauss

ROOT=Path(__file__).resolve().parents[1]
nodes,weights=leggauss(240)
checks=0
def close(actual,expected,tol=1e-9):
    global checks
    error=float(np.max(np.abs(np.asarray(actual)-np.asarray(expected))))
    assert error < tol,(error,tol,actual,expected)
    checks+=1
def integral(fn,a,b):
    return (b-a)/2*np.sum(weights*fn((b-a)/2*nodes+(a+b)/2))

# Piecewise integration independently confirms the triangle coefficient and its sign.
for L,c in [(1.,.7),(np.pi,1.),(3.4,1.6)]:
    for n in range(1,41):
        k=n*np.pi/L
        value=2/L*(integral(lambda x:x*np.sin(k*x),0,L/2)+integral(lambda x:(L-x)*np.sin(k*x),L/2,L))
        close(value,4*L/(n*n*np.pi**2)*np.sin(n*np.pi/2))
    n=2*np.arange(2000)+1
    k=n*np.pi/L
    coeff=4*L*(-1.)**np.arange(len(n))/(n*n*np.pi**2)
    def tri(x,t):
        return float(np.sum(coeff*np.sin(k*x)*np.exp(-c*c*k*k*t)))
    for x in np.linspace(0,L,51):
        close(tri(x,0),min(x,L-x),2e-4)
    for t in [.02,.1,.5,2.]:
        close(tri(0,t),0);close(tri(L,t),0)
        for x in [L*.2,L*.43,L*.7]:
            close(tri(x,t),tri(L-x,t))
            dt=1e-5;dx=1e-4
            ut=(tri(x,t+dt)-tri(x,t-dt))/(2*dt)
            uxx=(tri(x+dx,t)-2*tri(x,t)+tri(x-dx,t))/(dx*dx)
            close(ut,c*c*uxx,3e-6)

# Rectangle: project a boundary mixture, then check all boundaries and Laplace residual.
a,b=2.3,1.4
amps={1:1.2,2:-.4,5:.3}
f=lambda x:sum(v*np.sin(n*np.pi*x/a) for n,v in amps.items())
for n in range(1,12):
    close(2/a*integral(lambda x:f(x)*np.sin(n*np.pi*x/a),0,a),amps.get(n,0))
def rect(x,y):
    return sum(v*np.sin(n*np.pi*x/a)*np.sinh(n*np.pi*y/a)/np.sinh(n*np.pi*b/a) for n,v in amps.items())
for x in np.linspace(0,a,11):
    close(rect(x,0),0);close(rect(x,b),f(x))
for y in np.linspace(0,b,11):
    close(rect(0,y),0);close(rect(a,y),0)
for x,y in [(.3,.2),(.9,.6),(1.7,1.1)]:
    h=1e-4
    lap=(rect(x+h,y)+rect(x-h,y)+rect(x,y+h)+rect(x,y-h)-4*rect(x,y))/h**2
    close(lap,0,2e-6)

# Original pulse: independently integrate the Gaussian rather than an erf formula.
def pulse(x,t,c,U):
    return U/2*(math.erf((1-x)/(2*c*math.sqrt(t)))+math.erf((1+x)/(2*c*math.sqrt(t))))
for c in [.6,1.,1.8]:
    for t in [.03,.5,1.,8.]:
        for x in [-2.,-1.,-.2,0.,.6,1.,2.3]:
            numeric=integral(lambda v:np.exp(-(x-v)**2/(4*c*c*t)),-1,1)/(2*c*np.sqrt(np.pi*t))
            close(pulse(x,t,c,1),numeric)
            close(pulse(-x,t,c,1),numeric)
            h=1e-4;dt=1e-5
            ut=(pulse(x,t+dt,c,1)-pulse(x,t-dt,c,1))/(2*dt)
            uxx=(pulse(x+h,t,c,1)-2*pulse(x,t,c,1)+pulse(x-h,t,c,1))/h**2
            close(ut,c*c*uxx,3e-6)
        radius=1+12*c*np.sqrt(t)
        close(integral(lambda x:np.array([pulse(z,t,c,1) for z in x]),-radius,radius),2.,2e-8)
for x,expected in [(-2,0),(-1,.5),(0,1),(1,.5),(2,0)]:
    close(pulse(x,1e-7,1,1),expected)
for t,expected in [(.5,68.2689492137),(1,52.0499877813),(8,19.7412651366)]:
    close(pulse(0,t,1,100),expected,1e-8)

# Copper: source units, projection, analytic time, and SI conversion agree.
rho,cp,conductivity,L=8.92,.092,.95,80.
alpha=conductivity/(rho*cp)
rate=alpha*(np.pi/L)**2
time=np.log(2)/rate
close(alpha,1.1576330668746344)
close(time,388.2708317573018)
close(100*np.exp(-rate*time),50.)
for n in range(1,9):
    close(2/L*integral(lambda x:100*np.sin(np.pi*x/L)*np.sin(n*np.pi*x/L),0,L),100 if n==1 else 0)
alpha_si=(conductivity*4.184*100)/((rho*1000)*(cp*4184))
close(alpha_si,alpha/10000)
close(np.log(2)/(alpha_si*(np.pi/.8)**2),time)
pdf=ROOT/'site/materials/PDE - II.pdf'
original=Path('C:/Users/Jinhyeong/Downloads/PDE - II.pdf')
assert hashlib.sha256(pdf.read_bytes()).digest()==hashlib.sha256(original.read_bytes()).digest()
print(f'PDE_II_MATH_OK independent_checks={checks} copper_half_seconds={time:.10f} source_pdf_identical=True')
