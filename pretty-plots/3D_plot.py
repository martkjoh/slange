import numpy as np
from mayavi import mlab
import ffmpeg
import os


def f(x, y, t):
    r = x**2 + y**2
    return np.exp(- r**2/20) * np.sin(r + t)



def g(x, y, z, k):
    vals = 1 / (x * y + y * z + z * x)**(2 - k)
    m = 200
    mask = np.logical_or((vals > m ),(np.isnan(vals)))
    a = vals
    a[mask] = m
    print(mask)
    return a

def z(x, y):
    return 1 - x - y


def surface_plot():
    N = 100
    e = 0.01
    x, y = np.mgrid[e:1-e:N*1j, e:1-e:N*1j]

    f = lambda x, y : g(x, y, z(x, y), 0.01)
    mlab.surf(x, y, f, warp_scale="auto")
    mlab.points3d(0, 0, 0)
    mlab.show()

def surface_anim():
    path = "pretty-plots/"
    name = "waves"
    ext = ".png"
    T = 100
    N = 100
    pad = len(str(N))
    l = np.pi
    a = 10
    x, y = np.mgrid[-l:l:N*1j, -l:l:N*1j]

    plot = mlab.surf(x, y, f(x,y,0*x))
    @mlab.animate(delay=10)
    def anim():
        for i in range(T):
            plot.mlab_source.scalars = f(x, y, t=i * np.ones_like(x)/a)
            zeros = '0'*(pad - len(str(i)))
            filename = path + name + "_{}{}".format(zeros, i) + ext
            mlab.savefig(filename)
            print(i)
            yield
        
        mlab.clf()
        mlab.close(all=True)


    # anim()
    # mlab.show()

    cmnd = path + name + "_%0" + str(len(str(N))) + "d" + ext
    input = ffmpeg.input(path + name + "_%0" + str(len(str(N))) + "d" + ext)
    output = path + name + ".mp4"
    stream = ffmpeg.output(input, output, framerate=20)

    if os.path.isfile(output): os.remove(output)
    ffmpeg.run(stream)  

    [os.remove(path + f) for f in os.listdir(path) if f.endswith(ext) and f[:len(name)]==name]



# surface_plot()
surface_anim()
