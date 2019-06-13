import numpy as np
import plotly.offline as ply
import plotly.graph_objs as go

def f(x, t):
    k = 1
    w = 0.1
    return np.sin(k * x - w * t) 

n = 100
x = np.linspace(0, 10, 100)

data = [go.Scatter(
    x = x,
    y = f(x, 0)
)]

frames = []
for i in range(n):
    frames.append(dict(
        data = [dict(
            x = x,
            y = f(x, i)
        )]
    ))

layout = go.Layout(
    sliders = [dict(
        visible = True
    )]
)

fig = go.Figure(data = data, frames = frames)

ply.iplot(fig)
