"""Independent quadrature and differential checks for the PDE III note.

Uses NumPy only. Bessel values come from an angular integral, not the
power series printed in the note. Synthetic data below are verification
fixtures, not additional public exercises.
"""
from pathlib import Path
import hashlib
import json
import math
import numpy as np
from numpy.polynomial.legendre import leggauss, Legendre

ROOT=Path(__file__).resolve().parents[1]
metrics={}
def check(name,error,tol):
    error=float(error)
    assert math.isfinite(error) and error<tol, (name,error,tol)
    metrics[name]={'max_error':error,'tolerance':tol}

nodes,weights=leggauss(180)
def quad(f,a,b):
    x=(a+b)/2+(b-a)/2*nodes
    return (b-a)/2*np.dot(weights,f(x))

# Rectangle source data: integration by parts is checked by quadrature.
def integral(L,j):
    return quad(lambda x:x*(L-x)*np.sin(j*np.pi*x/L),0,L)
coeff_errors=[]
for m in range(1,10):
    for n in range(1,10):
        numerical=.05*integral(4,m)*integral(2,n)
        expected=409.6/(np.pi**6*m**3*n**3) if m%2 and n%2 else 0
        coeff_errors.append(abs(numerical-expected))
check('rectangle_81_coefficient_integrals',max(coeff_errors),2e-13)
c2=12.5/2.5
check('rectangle_c_squared',abs(c2-5),1e-14)
check('fundamental_period',abs(2*np.pi/(np.pi*np.sqrt(5)/4*np.sqrt(5))-1.6),1e-14)

odd=np.arange(1,161,2,dtype=float)
m,n=odd[:,None],odd[None,:]
lam=np.pi*np.sqrt(5)/4*np.sqrt(m*m+4*n*n)
B=409.6/(np.pi**6*m**3*n**3)
def rectangle(x,y,t):
    return float(np.sum(B*np.sin(m*np.pi*x/4)*np.sin(n*np.pi*y/2)*np.cos(lam*t)))
check('rectangle_initial_shape',max(abs(rectangle(x,y,0)-.1*x*(4-x)*y*(2-y)) for x,y in [(2,1),(.3,.2),(1.1,1.4),(3.7,1.8)]),2e-7)
check('rectangle_four_edges',max(abs(rectangle(x,y,t)) for x,y in [(0,.7),(4,1.4),(1.3,0),(2.7,2)] for t in [0,.23,1.6]),1e-12)
check('rectangle_initial_velocity',abs((rectangle(1.1,.8,1e-5)-rectangle(1.1,.8,-1e-5))/2e-5),1e-12)
check('rectangle_center_height',abs(rectangle(2,1,0)-.4),2e-7)
# Differential residual on a finite selection avoids truncation smoothness issues.
def rectangular_mode(x,y,t):
    w=np.pi*np.sqrt(5)/4*np.sqrt(3**2+4*5**2)
    return np.sin(3*np.pi*x/4)*np.sin(5*np.pi*y/2)*(.7*np.cos(w*t)+.2*np.sin(w*t))
def d2(f,x,h=2e-5): return (f(x+h)-2*f(x)+f(x-h))/h**2
x,y,t=.83,.61,.13
res=d2(lambda v:rectangular_mode(x,y,v),t)-5*(d2(lambda v:rectangular_mode(v,y,t),x)+d2(lambda v:rectangular_mode(x,v,t),y))
check('rectangle_pde_finite_difference',abs(res),2e-5)
# Nonzero initial-velocity fixture catches the missing lambda normalization.
w=np.pi*np.sqrt(5)/4*np.sqrt(2**2+4*3**2)
g_coefficient=4/8*quad(lambda x:np.sin(2*np.pi*x/4)**2,0,4)*quad(lambda y:1.7*np.sin(3*np.pi*y/2)**2,0,2)
check('rectangle_velocity_normalization',abs(w*(g_coefficient/w)-1.7),1e-13)

# J0(z)=1/pi integral_0^pi cos(z sin theta) dtheta; J1=-J0'.
angle=(nodes+1)*np.pi/2
sin_angle=np.sin(angle)
def j0(z):
    arr=np.asarray(z)
    return np.sum(np.cos(arr[...,None]*sin_angle)*weights,axis=-1)/2
def j1(z):
    arr=np.asarray(z)
    return np.sum(np.sin(arr[...,None]*sin_angle)*sin_angle*weights,axis=-1)/2
roots=[]
for lo,hi in [(2,3),(5,6),(8,9),(11,12)]:
    for _ in range(55):
        mid=(lo+hi)/2
        if j0(lo)*j0(mid)<=0: hi=mid
        else: lo=mid
    roots.append((lo+hi)/2)
published=np.array([2.4048255577,5.5200781103,8.6537279129,11.7915344390])
check('bessel_roots',np.max(np.abs(np.array(roots)-published)),5e-11)
R=2.3
gram=np.array([[quad(lambda r:r*j0(a*r/R)*j0(b*r/R),0,R) for b in roots] for a in roots])
norms=R**2/2*j1(np.array(roots))**2
check('bessel_weighted_orthogonality_and_norm',np.max(np.abs(gram-np.diag(norms))),3e-13)
check('bessel_origin_regular',abs(j0(0)-1)+abs(j1(0)),1e-13)
a=roots[1];k=a/R;c=1.7;w=c*k;r=.73;t=.21
def circular(r,t): return j0(k*r)*(.8*np.cos(w*t)-.4*np.sin(w*t))
ur=(circular(r+2e-5,t)-circular(r-2e-5,t))/4e-5
res=d2(lambda v:circular(r,v),t)-c*c*(d2(lambda v:circular(v,t),r)+ur/r)
check('circular_pde_finite_difference',abs(res),2e-5)
check('circular_fixed_rim',max(abs(circular(R,t)) for t in [0,.2,1]),1e-13)
# Arbitrary finite modal data reconstruct independent f and nonzero g.
targetA=np.array([.3,-.9,.2,.5]);targetB=np.array([.1,.4,-.2,.3])
freq=c*np.array(roots)/R
def radial_data(r,coeff): return sum(v*j0(a*r/R) for a,v in zip(roots,coeff))
computedA=np.array([quad(lambda r:r*radial_data(r,targetA)*j0(a*r/R),0,R)/norm for a,norm in zip(roots,norms)])
computedB=np.array([quad(lambda r:r*radial_data(r,freq*targetB)*j0(a*r/R),0,R)/norm/w for a,norm,w in zip(roots,norms,freq)])
check('bessel_displacement_projection',np.max(np.abs(computedA-targetA)),1e-12)
check('bessel_velocity_projection',np.max(np.abs(computedB-targetB)),1e-12)

# Exterior sphere: Legendre orthogonality and angular-coordinate Jacobian.
polys=[Legendre.basis(l) for l in range(7)]
gram=np.array([[quad(lambda z:p(z)*q(z),-1,1) for q in polys] for p in polys])
check('legendre_norms',np.max(np.abs(gram-np.diag([2/(2*l+1) for l in range(7)]))),2e-13)
fixtures=np.array([.7,-1.1,.4,.2,-.3,.1,.5])
def surface(phi): return sum(v*p(np.cos(phi)) for v,p in zip(fixtures,polys))
coeff=np.array([(2*l+1)/2*quad(lambda phi:surface(phi)*p(np.cos(phi))*np.sin(phi),0,np.pi) for l,p in enumerate(polys)])
check('sphere_polar_coefficient_jacobian',np.max(np.abs(coeff-fixtures)),3e-13)
R=1.8
def sphere(r,phi): return sum(v*(R/r)**(l+1)*p(np.cos(phi)) for l,(v,p) in enumerate(zip(coeff,polys)))
check('sphere_surface_condition',max(abs(sphere(R,phi)-surface(phi)) for phi in [0,.31,1.1,2.3,np.pi]),1e-12)
r=2.7;phi=1.13;h=3e-5
ur=(sphere(r+h,phi)-sphere(r-h,phi))/(2*h)
up=(sphere(r,phi+h)-sphere(r,phi-h))/(2*h)
res=d2(lambda s:sphere(s,phi),r,h)+2*ur/r+(d2(lambda a:sphere(r,a),phi,h)+np.cos(phi)/np.sin(phi)*up)/r**2
check('sphere_laplacian_finite_difference',abs(res),2e-5)
check('sphere_decay_at_infinity',abs(sphere(1e9,phi)),2e-9)

pdf=ROOT/'site/materials/PDE  - III.pdf'
digest=hashlib.sha256(pdf.read_bytes()).hexdigest()
assert digest=='8828e48e25f843733620727170c5a9dc32aa7bfd718914b8fbc20f762181f6a1'
report={'source_sha256':digest,'metrics':metrics,'source_example_center_at_0_4s':rectangle(2,1,.4)}
out=ROOT/'tmp/pde3/math-check.json';out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print('PDE_III_MATH_OK '+json.dumps(report,ensure_ascii=False))
