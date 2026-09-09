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

# Source values were visually rechecked first; these checks verify arithmetic,
# independent coordinate scales, zero coefficients, and sign-sensitive identities.
checks=0
close(np.dot([1,-2,3,-1],[4,1,-2,-4]),0,'p2 displayed calculation')
close(np.dot([1,-2,3,-1],[4,1,-2,4]),-8,'p2 separate column-vector reading')
close((1+.5)/2,.75,'p14 jump midpoint')
close(integ(lambda x:np.ones_like(x),-.25,.25),.5,'p24 c0')
close(integ(lambda x:x+pi,-pi,pi)/(2*pi),pi,'p30 mean')
for amplitude,omega in [(1.0,1.0),(3.2,2.7)]:
    L=pi/omega
    close(integ(lambda t:amplitude*np.sin(omega*t),0,L)/(2*L),amplitude/pi,'p28 mean in original t')
    close(integ(lambda t:amplitude*np.sin(omega*t)**2,0,L)/L,amplitude/2,'p28 b1 in original t')
    close(integ(lambda t:amplitude*np.sin(omega*t)*np.cos(2*omega*t),0,L)/L,-2*amplitude/(3*pi),'p28 a2 in original t')
for L,k in [(1.0,1.0),(2.3,4.1)]:
    close((integ(lambda x:2*k*x/L,0,L/2)+integ(lambda x:2*k*(L-x)/L,L/2,L))/L,k/2,'p32 mean with scale')
    close(2*k*(L/2)/L,k,'p32 left peak')
    close(2*k*(L-L/2)/L,k,'p32 right peak')
for T in [1.0,3.7]:
    close(2/T*integ(lambda t:np.cos(2*pi*t/T)**2,-T/2,T/2),1,'p23 cosine factor')
for n in [-3,-1,1,3]:
    # Integrate both real and imaginary parts of the actual complex exponential.
    close(integ(lambda x:np.cos(-2*pi*n*x),-.25,.25),np.sin(n*pi/2)/(n*pi),'p24 signed real coefficient')
    close(integ(lambda x:np.sin(-2*pi*n*x),-.25,.25),0,'p24 imaginary coefficient')
for A,B in [(.3,.7),(1.2,1.2),(-.8,2.1)]:
    close(np.sin(A)*np.cos(B),(np.sin(A+B)+np.sin(A-B))/2,'p6 product identity')
    close(np.sin(A)*np.sin(B),(np.cos(A-B)-np.cos(A+B))/2,'p7 product identity')
    close(np.sin(A)**2,(1-np.cos(2*A))/2,'p35 square identity')
print(f'SOURCE_RECHECK_MATH_OK checks={checks}')
