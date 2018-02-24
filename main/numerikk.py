import numpy as np
import scipy.integrate


# Eulers metode på en diff ligning på formen dy/dx = f(x, y).
# Startverdier x_0, y_0, func
def eulers_metode(func, x_0, y_0, x_slutt, h, print_verdier=False, returner=True):
    precission = int(np.log(1/h, 10))
    n = int(abs(x_slutt - x_0)/h)
    x = [x_0]
    y = [y_0]
    if print_verdier:
        print("y(", x_0, ") = ", y_0, sep="")
    for a in range(n):
        y_0 += h*(func(x_0, y_0))
        x_0 += h
        x.append(x_0)
        y.append(y_0)
        if print_verdier:
            print("y(",
                  format(x_0, ("." + str(precission) + "f")),   # Teller antall 0 i h
                  ") = ", format(y_0, ".6f"), sep="")
    if returner:
        return x, y


# Kjører gjennom Newtons metode til estimatet varierer mindre en tol
# h er avstanden som brukes for å beregne den deriverte. Mindre => mer nøyaktig
def newtons_metode(func, x_0, tol=0.0001, h=0.0001):

    def derivate(h, x, func):
        return (func(x + h / 2) - func(x - h / 2)) / h

    x_n = x_0
    x_np1 = x_n - func(x_n) / derivate(h, x_n, func)
    count = 0
    x = [x_0]
    n = [count]

    while abs(x_np1 - x_n) > tol:
        x_n = x_np1
        count += 1
        n.append(count)
        x.append(x_n)
        x_np1 = x_n - func(x_n) / derivate(h, x_n, func)

    x.append(x_np1)
    n.append(count + 1)

    return x, n


# Estimerer integrale av f fra a til b med n parabler
def simposons_metode(f, a, b, n):
    h = (b - a)/n
    S_n = f(a)
    for d in range(1, n):
        if d % 2 == 0:
            S_n += 2 * f(a + d*h)
        else:
            S_n += 4 * f(a + d*h)
    S_n += f(b)
    S_n = h/3 * S_n
    return S_n


def simposons_metode_dobbel(f, a, b, c, d, n):
    h = (b - a)/n
    S_n = f(a, c)
    for i in range(1, n):
        if i % 2 == 0:
            def g(x):
                return f(x, a + i * h)
            S_n += 2 * f(c, a + i * h) * simposons_metode(g, c, d, n)
        else:
            def g(x):
                return f(x, a + i * h)
            S_n += 4 * f(c, a + i * h) * simposons_metode(g, c, d, n)
    S_n += f(b, d)
    S_n = h/3 * S_n
    return S_n


# limits are [a, b, c, d], of the from [float, float, func/ float, func, float], and the function evaluates an
# integral of the form (integral from a to b ( integral from c(y)/c to d(y)/d of f(x, y) dx) dy))
# presis til ca. 3 desimaler
def double_integral(func, limits, res=1000):
    s = 0
    a, b = limits[0], limits[1]
    ys = np.linspace(a, b, res)
    c_is_func = callable(limits[2])
    d_is_func = callable(limits[3])
    for y in ys:
        if c_is_func:
            c = limits[2](y)
        else:
            c = limits[2]
        if d_is_func:
            d = limits[3](y)
        else:
            d = limits[3]
        dA = ((b - a) / res) * ((d - c) / res)
        xs = np.linspace(c, d, res)
        s += np.sum(func(xs, y)) * dA
    return s


def double_integgral_w_simpsons(func, limits, res=1000):
    s = 0
    a, b = limits[0], limits[1]
    ys = np.linspace(a, b, res)
    c_is_func = callable(limits[2])
    d_is_func = callable(limits[3])
    for y in ys:
        if c_is_func:
            c = limits[2](y)
        else:
            c = limits[2]
        if d_is_func:
            d = limits[3](y)
        else:
            d = limits[3]
        def g(z):
            return func(z, y)
        dy = ((b - a) / res)
        a += simposons_metode(g, c, d, res) * dy
        s += a
    return s


def partia_derivative(func, p, respect_to, res=1e-10):
    h = np.zeros(len(p))
    h[respect_to - 1] = res
    return (func(*(p + h)) - func(*p)) / res


def gauss_usikkerhetsforplantning(func, p, usikkerheter):
    s = 0
    for i, val in enumerate(p):
        s += ((partia_derivative(func, p, i + 1)) * usikkerheter[i])**2
    return np.sqrt(s)


if __name__ == "__main__":

    def doub_int():
        def f(y, x):
            return np.sqrt(np.maximum(0, 4 - y ** 2 - x ** 2))
        
        def c(y):
            return np.sqrt(2 * y - y**2)

        def d(y):
            return np.sqrt(4 - y**2)
        # b d
        # S S f(x,y) dx dy
        # a c
        a, b = 0, 2
        print(double_integral(f, [a, b, c, d]), 1)
        print(scipy.integrate.dblquad(f, a, b, c, d, epsabs=1.49e-8, epsrel=1.49e-8))
    doub_int()
