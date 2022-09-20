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



def makeCloud(l, m, vals, plotType):
    n = 100
    theta = np.linspace(0, 2 * pi, n)
    phi = np.linspace(0, pi, n)
    phi, theta = np.meshgrid(phi, theta)
    val = Y(m, l, theta, phi)
    if vals == "real": val = val.real
    elif vals == "imag": val = val.imag
    elif vals == "absSq": val = abs(val)**2
    else: raise Exception()

    if plotType == "radial": 
        r = R(val, theta, phi, (m, 0, - l * 1.6))
        return go.Surface(
            x=r[0], y=r[1], z=r[2],
            surfacecolor=val, 
            showscale=False, 
            colorscale="Viridis"
        )

    elif plotType == "color":
        r = R(1, theta, phi, (m * 2.5, 0, - l * 2.5))
        return go.Surface(x=r[0], y=r[1], z=r[2],
            surfacecolor = val, showscale = False, 
            colorscale = "Viridis")

# plotType determins if the value are indicated by "color" or "radial" extension
# vals determins wich values are plotted, real "real", imaginary "imag", 
# or the absolute square of the value "absSq"
def makePlot(l, plotType = "radial", vals = "absSq"):
    gos = []

    for i in range(l):
        for m in range(-i, i + 1):
            gos.append(makeCloud(i, m, plotType, vals))
    return gos

def makeLayout():
    ax = dict(
        showgrid = False,
        zeroline = False,
        showline = False,
        showticklabels = False,
        ticks = "",
    )

    return go.Layout(
        scene = dict(
            xaxis = ax,
            yaxis = ax,
            zaxis = ax,     
            aspectmode = "data",
        ),
        width=1000, 
        height=1000 
    )

# data = makePlot(5, plotType="color", vals="real")
data = [makeCloud(5, 2, "absSq", "radial")]

layout=makeLayout()
fig = go.Figure(data=data, layout=layout)
ply.plot(fig)
