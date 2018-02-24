from matplotlib import pyplot as plt
from math import log as ln

u = -2.58 * 10**3
beta = -1.32 * 10**4
g = -9.81
m_0 = 3.04 * 10**6
t_f = 150
dt = 0.1

def a(t):
    return (u * beta) / (m_0 + beta * t) + g

def a_lin(t):
    return a(0) - u * beta**2 / m_0**2 * t

def m(t):
    m = m_0 + beta * t
    return m

def v(t):
    return - u * ln(m_0/m(t)) + g * t

def v_lin(t):
    return (a_lin(0) + a_lin(t)) / 2 * t

def h(t):
    return - u * ln(m_0) * t + 1/2 * g * t**2 + u/beta * ((m(t) * ln(m(t)) - m(t)) - (m_0 * (ln(m_0)) - m_0))

def h_num(t):
    h = 0
    for delta in range(int(t / dt)):
        h += (v((delta + 1) * dt) + v(delta * dt)) / 2 * dt
    return h

print(h(t_f))
print(h_num(t_f))

t_liste = [t*dt for t in range(t_f * int(1/dt))]
a_liste = [a(t) for t in t_liste]
a_lin_liste = [a_lin(t) for t in t_liste]
v_liste = [v(t) for t in t_liste]
v_lin_liste = [v_lin(t) for t in t_liste]
h_liste = [h(t) for t in t_liste]
h_num_liste = [h_num(t) for t in t_liste]

aks = plt.figure(1)
plt.plot(t_liste, a_liste, label="a(t)")
plt.plot(t_liste, a_lin_liste, label="a_lin(t)")
plt.legend()

fart = plt.figure(2)
plt.plot(t_liste, v_liste, label="v(t)")
plt.plot(t_liste, v_lin_liste, label="v_lin(t)")
plt.legend()

høyde = plt.figure(3)
plt.plot(t_liste, h_liste, label="h(t)")
plt.plot(t_liste, h_num_liste, label="h_num(t)")
plt.legend()

plt.show()
