from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def main():

    def generate(x, y, n):
        E = np.exp(np.sin(x + n) + np.cos(y - n)) + np.exp(np.sin(x + n) + np.cos(y + n))

        for a in range(len(E)):
            for b in range(len(E[a])):
                if E[a][b] > heigt*n:
                    E[a][b] = heigt*n
                if E[a][b] < -heigt*n:
                    E[a][b] = -heigt*n
        return E

    def animate(n):
        n = n/10
        ax.cla()
        ax.set_zlim(0, 15)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        x, y = np.meshgrid(x, y)
        z = generate(x, y, n)
        surf = ax.plot_surface(x, y, z, cmap="viridis", vmin=-heigt, vmax=heigt)
        if contour:
            bottom = ax.contour(x, y, z, zdir='z', offset=-10, cmap="viridis")
            return surf, bottom
        return surf

    fig = plt.figure()
    ax = Axes3D(fig)
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    contour = False
    save = False
    heigt = 10

    anim = animation.FuncAnimation(fig, animate, interval=1, blit=False, frames=80)

    if save:
        plt.rcParams['animation.ffmpeg_path'] = 'C:\\Users\Martin\\Downloads\\ffmpeg-20180203-e3d946b-win64-static' \
                                                '\\ffmpeg-20180203-e3d946b-win64-static\\bin\\ffmpeg'
        mywriter = animation.FFMpegWriter(fps=20)
        anim.save('mymovie.mp4', writer=mywriter, dpi=1000)

    plt.show()


main()
