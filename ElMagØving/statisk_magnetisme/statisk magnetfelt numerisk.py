from ElMagØving.statisk_magnetisme.funksjoner2 import *
from main.numerikk import *
plt.style.use("classic")


def plotting(x_målt, diff, i):
    ax[i].set_xlim(-0.203, 0.2)
    ax[i].plot(x_målt, diff, "rx--", linewidth=1, markeredgecolor="k")
    ax[i].xaxis.set_ticks(np.linspace(-0.2, 0.2, 5))


x_0_lst = (29, 29, 29, 29.03)
I_lst = (1, 1, 1.01, 1.01)
R_lst = (0.07, 0.0712, 0.0712, 0.0712)
x_kont = np.linspace(-0.2, 0.2, 1000)
x_0, I, R = x_0_lst[0], I_lst[0], R_lst[0]

data, header = get_data("data/data_2gfdg.txt")
data = np.insert(data, 1, (data[0] - x_0) / 100, axis=0)
data = np.insert(data, 4, (data[2] + data[3])/2, axis=0)
data = np.insert(data, 5, magnetfelt_spole(data[1], R, I), axis=0)
data = np.insert(data, 6, abs(data[4]) - abs(data[5]), axis=0)
data = np.insert(data, 7, abs(data[6]/data[4]*100), axis=0)

headers = ["x [m]", "B snitt [gauss]", "Beregnet [gauss]", "Differanse [gauss]", "Avvik målt [%]"]
header_placement = [1, 4, 5, 6, 7]
for i in range(len(headers)):
    header.insert(header_placement[i], headers[i])

print_table(data, header=header)


fig = plt.figure()
label = ("$\\partial B/\\partial R$", "$\\partial B/\\partial I$", "$\\partial B/\\partial x$")
index = (2, 3, 1)
scale = (1, 20, -1)
style = (":", "--", "-.")
ax = [fig.add_subplot(311)]
ax[0].set_xticks([0])
ax[0].set_yticks([0])
ax[0].grid(True)
for i in range(3):
    ax[0].plot(x_kont, partial_derivative(magnetfelt_spole, (x_kont, R, I), index[i]) * scale[i], style[i], linewidth=2)
    ax[0].legend(label)

title = ("a", "b", "c", "d")
for i in range(0, 4):
    x_0, I, R = x_0_lst[i], I_lst[i], R_lst[i]
    data[1] = (data[0] - x_0) / 100
    data[5] = magnetfelt_spole(data[1], R, I)
    data[6] = abs(data[4]) - abs(data[5])
    data[7] = abs(data[6] / data[4] * 100)
    ax.append(fig.add_subplot((320 + i + 3)))
    ax[i + 1].set_title(title[i])
    ax[i + 1].set_ylabel("$B \,\, [G]$", fontsize=17)
    if i == 2 or i == 3:
        ax[i + 1].set_xlabel("$x \,\, [m]$", fontsize=17)
    plotting(data[1], data[6], i + 1)
    print(I, R, x_0)
    print_table(data, header=header)

fig.subplots_adjust(top=0.95, bottom=0.1, left=0.12, right=0.95, hspace=0.30, wspace=0.35)
#plt.tight_layout()
plt.legend()
plt.show()

fig.savefig("fig.pdf", facecolor='w', edgecolor='w', orientation='landscape', format="pdf", pad_inches=0.1)
