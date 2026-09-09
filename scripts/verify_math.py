"""Independent quadrature checks of every worked Fourier example."""
import numpy as np
from numpy.polynomial.legendre import leggauss,legval
from math import pi
z,w=leggauss(180)
checks=0
def integ(f,a,b):
    x=(a+b)/2+(b-a)*z/2
    return float(np.dot(w,f(x))*(b-a)/2)
def close(actual,expected,label,tol=2e-10):
    global checks
    assert abs(actual-expected)<tol,(label,actual,expected)
    checks+=1
for n in range(1,17):
    close(2/pi*integ(lambda x:np.sin(n*x),0,pi),4/(pi*n) if n%2 else 0,f'square b{n}')
    close(1/pi*integ(lambda x:np.sin(x)*np.cos(n*x),0,pi),-2/(pi*(n*n-1)) if n%2==0 else 0,f'rectifier a{n}')
    close(1/pi*integ(lambda x:np.sin(x)*np.sin(n*x),0,pi),0.5 if n==1 else 0,f'rectifier b{n}')
    close(1/pi*integ(lambda x:(x+pi)*np.sin(n*x),-pi,pi),2*(-1)**(n+1)/n,f'saw b{n}')
    close(1/pi*integ(lambda x:(x+pi)*np.cos(n*x),-pi,pi),0,f'saw a{n}')
    # Triangular half-range: L=1, k=1; integral is split at the corner.
    tri_a=2*(integ(lambda x:2*x*np.cos(n*pi*x),0,.5)+integ(lambda x:2*(1-x)*np.cos(n*pi*x),.5,1))
    tri_b=2*(integ(lambda x:2*x*np.sin(n*pi*x),0,.5)+integ(lambda x:2*(1-x)*np.sin(n*pi*x),.5,1))
    close(tri_a,4/(n*n*pi*pi)*(2*np.cos(n*pi/2)-1-(-1)**n),f'triangle a{n}')
    close(tri_b,8/(n*n*pi*pi)*np.sin(n*pi/2),f'triangle b{n}')
    pulse=integ(lambda x:np.cos(2*n*pi*x),-.25,.25)
    close(pulse,np.sin(n*pi/2)/(n*pi),f'pulse c{n}')
for n in range(6):
    coeff=np.zeros(n+1);coeff[n]=1
    actual=(2*n+1)/2*integ(lambda x:np.sin(pi*x)*legval(x,coeff),-1,1)
    expected={1:3/pi,3:7/pi-105/pi**3,5:11/pi-1155/pi**3+10395/pi**5}.get(n,0)
    close(actual,expected,f'Legendre a{n}')
    close(integ(lambda x:legval(x,coeff)**2,-1,1),2/(2*n+1),f'Legendre norm{n}')
close(integ(lambda x:(1-4/pi*np.sin(x))**2,0,pi)*2,2*pi-16/pi,'square error')
for n in range(1,8):
    close(integ(lambda x:2/pi*np.sin(n*x)**2,0,pi),1,f'SL norm {n}')
    for k in range(1,n):close(integ(lambda x:np.sin(n*x)*np.sin(k*x),0,pi),0,f'SL orthogonality {n},{k}')
print(f'MATH_CHECKS_OK independent_quadratures={checks}')
