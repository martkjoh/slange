from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib import style
from math import sin, factorial, pi

with plt.xkcd(1, 0.2, 1.2):
    def taylor_cos(degree, x):
        y_value = 0
        for i in range(degree):
            if i == 0:
                y_value += 0
            elif i % 2 == 1:
                if i % 4 == 1:
                    y_value += x**i / factorial(i)
                else:
                    y_value -= x**i / factorial(i)
        print(x, y_value)
        if y_value > 2 or y_value < -2:
            return None
        return y_value


    def animate(i):
        taylor_plot = [taylor_cos(i*2, x/(oppløsning/x_range)) for x in range(oppløsning)]
        taylor_plot_neg = [taylor_cos(i * 2, - x / (oppløsning / x_range)) for x in range(oppløsning)]
        ax1.clear()
        ax2.clear()
        ax3.clear()
        ax1.plot(xdata, sin_pos_list, label="sin(x)", color="red")
        ax3.plot([- x for x in xdata], sin_neg_list, color="red")
        ax2.plot(xdata, taylor_plot, label="P_"+str(i*2), color="blue")
        ax4.plot([- x for x in xdata], taylor_plot_neg, color="blue")
        plt.ylim(-2, 2)
        plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)


    taylor_grad = 20
    oppløsning = 1000
    x_range = 2*pi

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax3 = fig.add_subplot(111)
    ax2 = fig.add_subplot(111)
    ax4 = fig.add_subplot(111)
    style.use("fivethirtyeight")

    sin_pos_list = [sin(x / (oppløsning / x_range)) for x in range(oppløsning)]
    sin_neg_list = [sin(-x / (oppløsning / x_range)) for x in range(oppløsning)]
    xdata = [x / (oppløsning / x_range) for x in range(oppløsning)]
    taylor_plot = []
    taylor_plot_neg = []

    ani = animation.FuncAnimation(fig, animate, frames=(int(taylor_grad / 2)), interval=1000)
    plt.show()
