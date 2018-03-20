import matplotlib.pyplot as plt
import numpy as np
plt.style.use("bmh")

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

################################### Experimental data

mP = 0.0668 * 30.9737619 / 136.086    # gram KH2PO4 * molvekt P / molvekt KH2PO4
konsentrasjon_i_standard_løsning = mP / 250 * 10 ** 6       # ug/ml
Vstart = [0, 0.2, 0, 0, 0, 0]                               # ml
Vstopp = [0, 19.8, 29.9, 39.9, 50, 49.8 + (49.8 - 38.8)]    # ml
Abs470 = [0, 0.2174, 0.3263, 0.4376, 0.5454, 0.6610]            # -
Abs490 = [0, 0.1284, 0.1868, 0.2487, 0.3075, 0.3722]        # -

AbsUkjent470 = 0.3779
AbsUkjent490 = 0.2139

# AbsUkjent470 = 0.3925
# AbsUkjent490 = 0.2229


################################### Calculate

konsentrasjon = []

for i in range(len(Vstart)):
    konsentrasjon.append((Vstopp[i]-Vstart[i]) * konsentrasjon_i_standard_løsning / 100)    # ug/ml

a470, b470 = np.polyfit(konsentrasjon, Abs470, 1)   # y=ax+b
k_ukjent470 = (AbsUkjent470 - b470) / a470          # find unknown concentration from regression line
a490, b490 = np.polyfit(konsentrasjon, Abs490, 1)
k_ukjent490 = (AbsUkjent490 - b490) / a490

################################### Plot 470

plt.plot(konsentrasjon, Abs470, color='red', marker='x', linestyle='None', label='470 nm')  # plot exper. data
plt.plot([0, 40], [b470, a470*40+b470], color='red')                     # plot linear regression
plt.plot([k_ukjent470, k_ukjent470], [0, AbsUkjent470], color='red')    # guiding line
plt.plot([0, k_ukjent470], [AbsUkjent470, AbsUkjent470], color='red')   # guiding line
plt.text(k_ukjent470, AbsUkjent470 - 0.05, "%.2f mg/l" % k_ukjent470)   # result as text in plot

################################### Plot 490

plt.plot(konsentrasjon, Abs490, color='blue', marker='x', linestyle='None', label='490 nm')
plt.plot([k_ukjent490, k_ukjent490], [0, AbsUkjent490], color='blue')
plt.plot([0, k_ukjent490], [AbsUkjent490, AbsUkjent490], color='blue')
plt.plot([0, 40], [b490, a490 * 40 + b490], color='blue')
plt.text(k_ukjent490, AbsUkjent490 - 0.05, "%.2f mg/l" % k_ukjent490)

################################### Finalize and save plot

plt.legend(loc=2)
plt.ylabel('Absorbance [-]')
plt.xlabel('Concentration [mg/l]')
ax.set_ylim([0, ax.get_ylim()[1]]) # fix bottom of y-axis to 0
plt.show()