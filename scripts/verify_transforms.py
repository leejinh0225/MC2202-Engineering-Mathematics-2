"""Independent numerical verification; no content-module formulas are imported."""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss

z, weights = leggauss(240)
checks = 0
def integral(f, lo, hi):
    x=(lo+hi)/2+(hi-lo)*z/2
    return np.dot(weights,f(x))*(hi-lo)/2

def close(actual, expected, label, tol=2e-9):
    global checks
    error=np.max(np.abs(np.asarray(actual)-np.asarray(expected)))
    assert error<tol,(label, actual, expected, error)
    checks+=1

s=math.sqrt(2/math.pi)
norm=math.sqrt(2*math.pi)
for a in [.7, 1., 2.]:
    for w in [0., .3, 1., 3.]:
        C=s*integral(lambda x:np.exp(-a*x)*np.cos(w*x),0,45/a)
        S=s*integral(lambda x:np.exp(-a*x)*np.sin(w*x),0,45/a)
        close(C,s*a/(a*a+w*w),'p11/14 cosine exponential')
        close(S,s*w/(a*a+w*w),'p11 sine exponential')
        close(-a*C,w*S-s,'p9/10 cosine derivative and boundary')
        close(-a*S,-w*C,'p9/10 sine derivative uses cosine')
        close(a*a*C,-w*w*C+s*a,'p9/10 cosine second derivative')
        close(a*a*S,-w*w*S+s*w,'p9/10 sine second derivative squared frequency')
        one=integral(lambda x:np.exp(-a*x-1j*w*x),0,45/a)/norm
        close(one,1/(norm*(a+1j*w)),'p18 unilateral transform')
        two=(integral(lambda x:np.exp(a*x-1j*w*x),-45/a,0)+integral(lambda x:np.exp(-a*x-1j*w*x),0,45/a))/norm
        close(two,s*a/(a*a+w*w),'p19 bilateral exponential')

for width in [.4,1.,2.]:
    k=1.3
    for w in [0.,.2,1.,3.]:
        close(s*integral(lambda x:k*np.cos(w*x),0,width),s*k*width if w==0 else s*k*np.sin(width*w)/w,'p13 box cosine')
        close(s*integral(lambda x:k*np.sin(w*x),0,width),0 if w==0 else s*k*(1-np.cos(width*w))/w,'p13 box sine')
for w in [0,.2,1,3,9]:
    close(integral(lambda x:np.cos(w*x),-1,1)/math.pi,2/math.pi if w==0 else 2*np.sin(w)/(math.pi*w),'p6 pulse density')

# Independent Ei power series and long oscillatory quadrature for the exact p11 numerator.
# Tail bound for monotone 1/(k^2+w^2) times sin(xw): <= 2/[x(k^2+W^2)].
def ei_real(x):
    term=x
    result=float(np.euler_gamma)+math.log(abs(x))
    for n in range(1,200):
        result+=term/n
        term*=x/(n+1)
        if abs(term)<1e-17:break
    return result

panel_z,panel_weights=leggauss(32)
for k,x in [(1.,1.),(.7,.4),(2.,1.2),(1.3,2.)]:
    stop=20000.
    n=math.ceil(stop/min(1.,math.pi/x))
    edges=np.linspace(0,stop,n+1)
    middle=(edges[:-1]+edges[1:])/2
    half=(edges[1:]-edges[:-1])/2
    omega=middle[:,None]+half[:,None]*panel_z
    exact_J=(math.exp(-k*x)*ei_real(k*x)-math.exp(k*x)*ei_real(-k*x))/(2*k)
    numerical_J=np.sum(half*np.sum(panel_weights*np.sin(omega*x)/(k*k+omega*omega),axis=1))
    numerical_C=np.sum(half*np.sum(panel_weights*np.cos(omega*x)/(k*k+omega*omega),axis=1))
    close(numerical_J,exact_J,'p11 original unweighted sine integral',2e-8)
    close(numerical_C,math.pi/(2*k)*math.exp(-k*x),'p11 cosine inversion',2e-8)
    if k==x==1:
        close(exact_J,.6467611227791301,'p11 published decimal',1e-12)
        assert abs(exact_J-math.pi/(2*math.e))>.06

# Gaussian transforms and properties, with real numerical integration on a large finite interval.
def G(w):return math.exp(-w*w/4)/math.sqrt(2)
for w in [-4,-1,0,.7,3]:
    close(integral(lambda x:np.exp(-x*x-1j*w*x),-12,12)/norm,G(w),'p34 Gaussian base')
    close(integral(lambda x:x*np.exp(-x*x-1j*w*x),-12,12)/norm,-1j*w*G(w)/2,'p34 xe^-x^2 sign')
    close(integral(lambda x:-2*x*np.exp(-x*x-1j*w*x),-12,12)/norm,1j*w*G(w),'p20 derivative')
    close(integral(lambda x:np.exp(-(x-1.2)**2-1j*w*x),-15,15)/norm,np.exp(-1j*w*1.2)*G(w),'p21 time shift')
    close(integral(lambda x:np.exp(-x*x+1j*.8*x-1j*w*x),-12,12)/norm,G(w-.8),'p21 modulation imaginary unit')
    for lam in [-2.,.7,2.]:
        close(integral(lambda x:np.exp(-(lam*x)**2-1j*w*x),-20,20)/norm,G(w/lam)/abs(lam),'p22 signed scaling')

# Convolution direct overlap and exponential integral vs separate transformed factors.
for x in [-1,.2,.9,1.,1.7,2.,3.]:
    overlap=max(0,min(1,x)-max(0,x-1))
    triangular=0 if x<0 or x>2 else x if x<=1 else 2-x
    close(overlap,triangular,'p23 box overlap')
for a,b in [(.7,1.2),(2.,.8),(1.,1.)]:
    for x in [0,.4,2.]:
        result=integral(lambda p:np.exp(-a*p-b*(x-p)),0,x)
        closed=x*math.exp(-a*x) if a==b else (math.exp(-a*x)-math.exp(-b*x))/(b-a)
        close(result,closed,'p24 exponential convolution')
    for w in [0,.5,2.]:
        def h(t):
            return t*np.exp(-a*t) if a==b else (np.exp(-a*t)-np.exp(-b*t))/(b-a)
        close(integral(lambda t:h(t)*np.exp(-1j*w*t),0,50/min(a,b))/norm,1/(norm*(a+1j*w)*(b+1j*w)),'p24 convolution theorem factor')

# Source N=4 example: direct matrix, inverse, normalized coefficients, radix-2 split.
data=np.array([0,1,4,9])
W=np.exp(-2j*np.pi*np.outer(np.arange(4),np.arange(4))/4)
X=W@data
expected=np.array([14,-4+8j,-6,-4-8j])
close(X,expected,'p28 source direct DFT')
close(X/4,[3.5,-1+2j,-1.5,-1-2j],'p28 normalized coefficients')
close(W.conj()@X/4,data,'p28 inverse')
E=np.array([data[0]+data[2],data[0]-data[2]])
O=np.array([data[1]+data[3],data[1]-data[3]])
factor=np.exp(-2j*np.pi*np.arange(2)/4)
close(np.r_[E+factor*O,E-factor*O],expected,'p30 FFT source signs')

def radix2(data):
    if len(data)==1:return data
    E=radix2(data[::2]);O=radix2(data[1::2])
    rotated=np.exp(-2j*np.pi*np.arange(len(data)//2)/len(data))*O
    return np.r_[E+rotated,E-rotated]

rng=np.random.default_rng(2202)
for N in [2,4,8,16,32]:
    W=np.exp(-2j*np.pi*np.outer(np.arange(N),np.arange(N))/N)
    close(W.conj().T@W,N*np.eye(N),'p26/27 discrete orthogonality')
    samples=rng.normal(size=N)+1j*rng.normal(size=N)
    close(radix2(samples),W@samples,'p29 radix2 vs matrix')
    close(radix2(samples),np.fft.fft(samples),'p29 radix2 vs NumPy')

N=8
k=np.arange(N);x=2*np.pi*k/N
signal=np.sin(x)+np.sin(3*x)
close(signal,[0,math.sqrt(2),0,math.sqrt(2),0,-math.sqrt(2),0,-math.sqrt(2)],'p31 sample vector')
close(np.fft.fft(signal),[0,-4j,0,-4j,0,4j,0,4j],'p31 sine complex bins')
close(np.fft.fftshift(np.abs(np.fft.fft(signal))),[0,4,0,4,0,4,0,4],'p31 shifted magnitude')
close(np.fft.ifft(np.fft.fft(signal)),signal,'p31 inverse reconstruction')

# p36 is not silently altered: this checks only the explicitly separate sine inverse.
for a in [.6,1.,2.]:
    for x in [-2.,0.,.3,1.]:
        H=integral(lambda w:np.exp(-a*w)*x*np.sinc(w*x/math.pi),0,50/a)
        close(H,math.atan(x/a),'p36 conditional sine inverse')
close(integral(lambda t:np.sinc(t/math.pi),0,math.pi)/math.pi-.5,.08948987223608362,'p7 Gibbs overshoot')
print(f'TRANSFORMS_MATH_OK checks={checks}; original problem numerators preserved; MATLAB-equivalent DFT checked with NumPy')
