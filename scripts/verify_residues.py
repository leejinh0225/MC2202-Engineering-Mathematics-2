"""Check Week 13 calculations independently on the original contours and intervals."""
from cmath import cos, exp, pi, sin
from hashlib import sha256
from math import sqrt
from pathlib import Path

from verify_integration import circle, close, integrate


def midpoint(f, a, b, n=16000):
    h = (b-a)/n
    return h * sum(f(a + (j+0.5)*h) for j in range(n))


def principal_value():
    def f(x):
        return 1/((x-1)*(x-2)*(x*x+1))

    # Keep gaps around each real pole symmetric. Integrate paired evaluations
    # to avoid subtracting two individually divergent integrals.
    def paired(a):
        return midpoint(lambda h: f(a-h)+f(a+h), 0, 0.25)

    def tail(endpoint, sign):
        return midpoint(lambda u: f(endpoint+sign*u/(1-u))/(1-u)**2, 0, 1)

    return tail(0.75,-1) + paired(1) + midpoint(f,1.25,1.75) + paired(2) + tail(2.25,1)


def check_math():
    close(circle(lambda z: sin(z)/z**4, 0, 1), -pi*1j/3)
    close(circle(lambda z: (9*z+1j)/(z*(z*z+1)), 1j, 0.24)/(2j*pi), -5j)
    f = lambda z: (4-3*z)/(z*z-z)
    for center,r,answer in [(0.5,1,-6j*pi),(0,0.4,-8j*pi),(2,0.3,0)]:
        close(circle(f,center,r),answer)

    def ellipse(t):
        z = cos(t)+3j*sin(t)
        dz = -sin(t)+3j*cos(t)
        return (z*exp(pi*z)/(z**4-16)+z*exp(pi*z))*dz
    close(integrate(ellipse,0,2*pi), -1j*pi/4)
    close(integrate(ellipse,2*pi,0), 1j*pi/4)
    close(integrate(lambda t: 1/(sqrt(2)-cos(t)),0,2*pi), 2*pi)
    close(integrate(lambda t: (1-t)**2/((1-t)**4+t**4),0,1), pi/(2*sqrt(2)))
    close(principal_value(), pi/10, 5e-8)
    for s in (-2, 2):
        pole = 1+1j if s>0 else 1-1j
        residue = exp(1j*s*pole)/(2*(pole-1))
        oriented = (2j*pi if s>0 else -2j*pi)*residue
        close(oriented, pi*exp(-abs(s)+1j*s))
    close(circle(lambda z: exp(1/z),0,1), 2j*pi)
    close(circle(lambda z: pi*cos(pi*z)/(sin(pi*z)*z*z),0,0.32)/(2j*pi), -pi*pi/3)
    for z in (0.5,3,-0.4+0.8j):
        close((3*z+2)/(z*(z-1)*(z-2)), 1/z-5/(z-1)+4/(z-2))


if __name__ == '__main__':
    check_math()
    pdf = Path(__file__).resolve().parents[1]/'site/materials/Week 13.pdf'
    assert sha256(pdf.read_bytes()).hexdigest()=='eba01059fc3e3f34b4bdf3f7e0eab68f965b33c6a93b899a28e8b6859aa87762'
    print('RESIDUE_MATH_OK contour integrals, real integrals, principal value, three practice problems, PDF hash')
