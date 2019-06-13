from plotly.offline import init_notebook_mode, plot
from IPython.display import display, HTML
import numpy as np

t=np.linspace(-1,1,100)
x=t+t**2
y=t-t**2
xm=np.min(x)-1.5
xM=np.max(x)+1.5
ym=np.min(y)-1.5
yM=np.max(y)+1.5
N=50
s=np.linspace(-1,1,N)
xx=s+s**2
yy=s-s**2


data=[dict(x=x, y=y, 
           mode='lines', 
           line=dict(width=2, color='blue')
          ),
      dict(x=x, y=y, 
           mode='lines', 
           line=dict(width=2, color='blue')
          )
    ]

layout=dict(xaxis=dict(range=[xm, xM], autorange=False, zeroline=False),
            yaxis=dict(range=[ym, yM], autorange=False, zeroline=False),
            title='Kinematic Generation of a Planar Curve', hovermode='closest',
            updatemenus= [{'type': 'buttons',
                           'buttons': [{'label': 'Play',
                                        'method': 'animate',
                                        'args': [None]}]}])

frames=[dict(data=[dict(x=[xx[k]], 
                        y=[yy[k]], 
                        mode='markers', 
                        marker=dict(color='red', size=10)
                        )
                  ]) for k in range(N)]    

figure1=dict(data=data, layout=layout, frames=frames)          
plot(figure1)


N=50
s=np.linspace(-1,1,N)
vx=1+2*s
vy=1-2*s #v=(vx, vy) is the velocity
speed=np.sqrt(vx**2+vy**2)
ux=vx/speed #(ux, uy) unit tangent vector, (-uy, ux) unit normal vector
uy=vy/speed

xend=xx+ux #end coordinates for the unit tangent vector at (xx, yy)
yend=yy+uy

xnoe=xx-uy #end coordinates for the unit normal vector at (xx,yy)
ynoe=yy+ux


data=[dict(x=x, y=y,
           name='frame',
           mode='lines', 
           line=dict(width=2, color='blue')),
      dict(x=x, y=y,
           name='curve',
           mode='lines', 
           line=dict(width=2, color='blue'))
    ]

layout=dict(width=600, height=600,
            xaxis=dict(range=[xm, xM], autorange=False, zeroline=False),
            yaxis=dict(range=[ym, yM], autorange=False, zeroline=False),
            title='Moving Frenet Frame Along a Planar Curve', hovermode='closest',
            updatemenus= [{'type': 'buttons',
                           'buttons': [{'label': 'Play',
                                        'method': 'animate',
                                        'args': [None]}]}])

frames=[dict(data=[dict(x=[xx[k], xend[k], None, xx[k], xnoe[k]], 
                        y=[yy[k], yend[k], None, yy[k], ynoe[k]], 
                        mode='lines', 
                        line=dict(color='red', width=2))
                  ]) for k in range(N)]    
          
figure2=dict(data=data, layout=layout, frames=frames)          
plot(figure2)
