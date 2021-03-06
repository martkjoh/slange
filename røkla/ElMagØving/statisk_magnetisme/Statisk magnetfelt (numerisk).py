from matplotlib import pyplot as plt
from Søppel.ElMagØving.statisk_magnetisme.funksjoner import *
from main.numerikk import *

plt.style.use("classic")
print(plt.style.available)

# x_0 (nullpunktet) for de forskjellige ekspirimentene. x_0ab, a er oppgaven, b er de forskjellige rundene
x_01 = 29.0
x_021 = 32.9
x_022 = 34.45
x_023 = 29.8
x_03 = 29.0 - 20.3

I = 1.01                   # Strømm
R = 0.071                # Radius for spolen
R_s = 0.05              # Radius for solenoiden
l = 0.4                 # Lengden Av solenoiden

Delta_I = 0.00            # Usikkerhet for de forskjellige verdiene
Delta_R = 0.0005
Delta_x = 0.0005
Delta_a = 0.0005
Delta_l = Delta_x

# Oppretter alle figurene for de forskjellige eksperimentene
figs = [plt.figure() for x in range(5)]
axs = [fig.add_subplot(211) for fig in figs]
axs += [fig.add_subplot(212) for fig in figs]


def plotting(akse, x_målt, y_målt, x_kont, y_kont, usikkerhet_kont, diff):
    y_målt = abs(y_målt)
    axs[akse].errorbar(x_målt, y_målt, yerr=usikkerhet_målte_verdier(y_målt), markeredgewidth=0.5,
                       capsize=6, elinewidth=1, fmt="rs--", ecolor='k', capthick=0.5, linewidth=1, markersize=3)
    axs[akse].fill_between(x_kont, y_kont + usikkerhet_kont, y_kont - usikkerhet_kont, alpha=0.5, facecolors='#555555')
    axs[5 + akse].plot(x_målt, diff, "rx--", linewidth=1, markeredgecolor="k")
    axs[5 + akse].fill_between(x_kont, usikkerhet_kont, - usikkerhet_kont, alpha=0.5, facecolors='#555555')

    ylabel = "$B \,\, [G]$"
    xlabel = "$x \,\, [m]$"
    if akse == 4:
        ticks = np.linspace(-0.1, 0.5, 5)
        leg_loc = 8
    else:
        ticks = np.linspace(-0.2, 0.2, 5)
        leg_loc = 1

    axs[akse].set_xlim(min(x_kont), max(x_kont))
    axs[5 + akse].set_xlim(min(x_kont), max(x_kont))
    axs[akse].set_ylabel(ylabel, fontsize=18)
    axs[akse].xaxis.set_ticks(ticks)
    axs[5 + akse].set_ylabel(ylabel, fontsize=18)
    axs[5 + akse].xaxis.set_ticks(ticks)
    axs[5 + akse].set_xlabel(xlabel, fontsize=18)
    axs[akse].legend(["$B_T \pm \Delta B_T$", "$B_m \pm \Delta B_m$"], fontsize=14, loc=8)
    axs[5 + akse].legend(["$B_m - B_T$", "$\Delta B_T$"], fontsize=15, loc=leg_loc)


def oppgave_2():
    data, header = get_data("data/data_2gfdg.txt")

    headers = ["x [m]", "B snitt [G]", "Beregnet [G]", "Differanse [G]", "Avvik målt [%]"]
    header_placement = [1, 4, 5, 6, 7]
    for i in range(len(headers)):
        header.insert(header_placement[i], headers[i])

    data = np.insert(data, 1, (data[0] - x_01)/100, axis=0)             # Omgjøre fra mål til x
    data = np.insert(data, 4, (data[2] + data[3])/2, axis=0)            # Finne snittene av målerundene
    data = np.insert(data, 5, magnetfelt_spole(data[1], R, I), axis=0)        # Beregne B(x)
    data = np.insert(data, 6, abs(data[4]) - abs(data[5]), axis=0)      # Differanse mellom beregnede og målte verdier
    data = np.insert(data, 7, abs(data[6]/data[4]*100), axis=0)         # Prosentvis avik mellom målt og beregna

    x_kont = np.linspace(data[1][0], data[1][-1], 1000)                 # "kontinuerlige" verdier for x
    y_kont = magnetfelt_spole(x_kont, R, I)                             # Får en glatt graf for beregnede B-verider
    usikkerehet_kont = gauss_usikkerhetsforplantning(magnetfelt_spole,
                                                     (x_kont, R, I),
                                                     (Delta_x, Delta_R, Delta_I))

    print_table(data, header=header)

    plotting(0, data[1], data[4], x_kont, y_kont, usikkerehet_kont, data[6])


def oppgave_3():
    for i in range(1, 4):
        if i == 1:
            a = R
            x_02 = x_021

        elif i == 2:
            a = 2 * R
            x_02 = x_022

        else:
            a = R/2
            x_02 = x_023

        data, header = get_data("data/data_3_" + str(i) + ".txt")

        headers = ["x [m]", "Beregnet a=" + str(a) + " [G]", "Differanse [G]", "Avvik målt [%]"]
        header_placement = [1, 3, 4, 5]

        for j in range(len(headers)):
            header.insert(header_placement[j], headers[j])

        data = np.insert(data, 1, (data[0] - x_02) / 100, axis=0)                   # Finne x fra mål
        data = np.insert(data, 3,
                         magnetfelt_helmholtzspole(data[1], R, I, a),
                         axis=0)                                                    # Beregne B
        data = np.insert(data, 4, abs(data[2]) - abs(data[3]), axis=0)              # Differanse
        data = np.insert(data, 5, abs(data[4]/data[2] * 100), axis=0)               # Prosentvis differanse

        x_kont = np.linspace(data[1][0], data[1][-1], 1000)
        y_kont = magnetfelt_helmholtzspole(x_kont, R, I, a)
        usikkerehet_kont = gauss_usikkerhetsforplantning(magnetfelt_helmholtzspole,
                                                         (x_kont, R, I, a),
                                                         (Delta_x, Delta_R, Delta_I, Delta_a))

        print_table(data, header=header)

        plotting(i, data[1], data[2], x_kont, y_kont, usikkerehet_kont, data[4])


def oppgave_4():
    data, header = get_data("data/data_4.txt")

    headers = ["x [m]", "Beregnet [G]", "Differanse [G]", "Avvik målt [%]"]
    header_placement = [1, 3, 4, 5]

    for i in range(len(headers)):
        header.insert(header_placement[i], headers[i])

    data = np.insert(data, 1, (data[0] - x_03) / 100, axis=0)
    data = np.insert(data, 3, magnetflet_solenoide(data[1], R_s, I, l), axis=0)
    data = np.insert(data, 4, abs(data[2]) - abs(data[3]), axis=0)
    data = np.insert(data, 5, abs(data[4] / data[2] * 100), axis=0)

    x_kont = np.linspace(-0.1, 0.502, 1000)
    y_kont = magnetflet_solenoide(x_kont, R_s, I, l)
    usikkerehet_kont = gauss_usikkerhetsforplantning(magnetflet_solenoide,
                                                     (x_kont, R_s, I, l),
                                                     (Delta_x, Delta_R, Delta_I, Delta_l))

    print_table(data, header=header)

    plotting(4, data[1], data[2], x_kont, y_kont, usikkerehet_kont, data[4])


oppgave_2()
oppgave_3()
oppgave_4()


plt.legend()

plt.show()

for i, f in enumerate(figs):
    f.subplots_adjust(top=0.95, bottom=0.1, left=0.1, right=0.95, hspace=0.25, wspace=0.35)
    f.savefig("bestefig/fig" + str(i) + ".pdf", facecolor='w', edgecolor='w',
              orientation='landscape', format="pdf", pad_inches=0.1)
