import plotly.offline as ply
import plotly.graph_objs as go
import numpy as np
from numpy import sin, cos, exp
from numpy import e, pi
from scipy.special import sph_harm as Y

def R(r, theta, phi, shift):
    return [
        abs(r) * cos(theta) * sin(phi) + shift[0], 
        abs(r) * sin(theta) * sin(phi) + shift[1], 
        abs(r) * cos(phi) + shift[2]
        ]

theta = np.linspace(0, 2 * pi)
phi = np.linspace(0, pi)
phi, theta = np.meshgrid(phi, theta)

gos = []

for l in range(5):
    for m in range(-l, l + 1):
        print(l, m)
        r = R(Y(m, l, theta, phi).real, theta, phi, (l, 0, m * 2))
        gos.append(go.Surface(x = r[0], y = r[1], z = r[2]))
        r = R(Y(m, l, theta, phi).imag, theta, phi, (l, 1, m * 2))
        gos.append(go.Surface(x = r[0], y = r[1], z = r[2]))

layout = go.Layout(
    scene = dict(
        aspectratio = dict(
            x = 5, 
            y = 1.5, 
            z = 10
        )
    )
)

fig = go.Figure(data = gos, layout = layout)
ply.plot(fig)
