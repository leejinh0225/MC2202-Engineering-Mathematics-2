"""Independent checks for the source examples in the Week 11–12 lecture."""
from cmath import atan, cos, exp, pi, sin, sqrt
from fractions import Fraction
from hashlib import sha256
from math import comb, factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def close(value, expected, tolerance=1e-8):
    if abs(value - expected) > tolerance:
        raise AssertionError((value, expected))


def integrate(f, a, b, count=4096):
    # Composite Simpson rule with an even number of panels.
    h = (b - a) / count
    middle = sum((4 if j % 2 else 2) * f(a + j*h) for j in range(1, count))
    return h * (f(a) + middle + f(b)) / 3


def circle(f, center, radius):
    def integrand(t):
        w = radius * exp(1j*t)
        return f(center + w)*1j*w
    return integrate(integrand, 0, 2*pi)


def check_integrals():
    close(integrate(lambda t: t*exp(1j*t), 2*pi, 4*pi), -2j*pi)
    close(integrate(lambda t: exp(1j*t), 0, pi), 2j)
    close(circle(lambda z: z*z, 0, 1), 0)
    close(integrate(lambda t: 1j*exp(1j*t)/(2+exp(1j*t)-2), 0, pi), 1j*pi)
    for n in (1, 2, 3, 4):
        close(circle(lambda z: (z-1j)**(-n), 1j, 0.75), 2j*pi if n == 1 else 0)
    rational = lambda z: 2*z/(z*z+2)
    close(circle(rational, 0, 2), 4j*pi)
    close(circle(rational, 1j, 1), 2j*pi)
    close(integrate(lambda t: cos(1+(1j-1)*t)*(1j-1), 0, 1), sin(1j)-sin(1))
    close(circle(lambda z: exp(z)/(z-1), 0, 2), 2j*pi*exp(1))
    close(circle(lambda z: (z**3-6)/(2*z-1j), 0, 2), pi/8-6j*pi)
    close(circle(lambda z: exp(z*z)/(z-1j)**4, 0, 2), -4*pi/(3*exp(1)))
    vertices = (-1+1j, -1, 1+1j, 3-1j)
    for start, delta, end in zip(vertices, (-1j, 2+1j, 2-2j), vertices[1:]):
        close(start+delta, end)
    close(integrate(lambda t: (-1-1j+(4+2j)*t)*(4+2j), 0, 1), 4+2j)
    close(integrate(lambda y: (y*y+2*y+1j*y)*(2*y+2+1j), -1, 1), 4+2j)
    a, b = 0.4+0.3j, -0.6+0.1j
    close(circle(lambda z: exp(z)/((z-a)*(z-b)), 0, 2)/(2j*pi), (exp(b)-exp(a))/(b-a))


def check_series():
    n = 500
    close(abs(100+75j), 125)
    close(Fraction(comb(2*n,n), comb(2*n+2,n+1)), Fraction((n+1)**2,(2*n+2)*(2*n+1)))
    close(comb(2*n,n)/comb(2*n+2,n+1), 1/4, 0.0003)
    close((sqrt(10**12)+1j*(10**12+1))/10**12, 1j, 0.000002)
    close(sum(((1-1j)/2)**k for k in range(150)), 1-1j)
    z = 0.42+0.23j
    close(sum(z**k/factorial(k) for k in range(24)), exp(z))
    close(sum((-z*z)**k for k in range(32)), 1/(1+z*z))
    close(sum((-1)**k*z**(2*k+1)/(2*k+1) for k in range(32)), atan(z))
    close(sum((-1)**k*z**(2*k)/factorial(2*k) for k in range(12)), cos(z))
    close(sum((-1)**k*z**(2*k+1)/factorial(2*k+1) for k in range(12)), sin(z))
    close(sum((-1)**k*z**(2*k-4)/factorial(2*k+1) for k in range(12)), sin(z)/z**5)
    cube = [Fraction((-1)**k*(3-3**(2*k+1)),4*factorial(2*k+1)) for k in range(16)]
    assert cube[:4] == [0, 1, Fraction(-1,2), Fraction(13,120)]
    close(sum(c*z**(2*k+1) for k,c in enumerate(cube)), sin(z)**3)
    a,c = 0.2j, 1.6-0.3j
    close(sum((z-a)**k/(c-a)**(k+1) for k in range(40)), 1/(c-z))
    close(sum(z**(2-k)/factorial(k) for k in range(32)), z*z*exp(1/z))
    close(sum(z**(k-3) for k in range(60)), 1/(z**3-z**4))
    z = 2.1-0.4j
    close(-sum(z**(-4-k) for k in range(50)), 1/(z**3-z**4))


if __name__ == '__main__':
    check_integrals()
    check_series()
    pdf = ROOT / 'site/materials/Week 11 - 12 (1).pdf'
    assert sha256(pdf.read_bytes()).hexdigest() == '62b511bf87b26aef0d7657f37edc31c0b095a46d1cc1dea49b49adc746cc351a'
    print('INTEGRATION_MATH_OK contour quadrature, practice answers, power series, Laurent annuli, source PDF')
