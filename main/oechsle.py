from matplotlib import pyplot as plt
import numpy as np

x = np.array([-10, -5, 0, 5, 10, 15, 20, 25, 30, 35])   # Grader oechsle (Delta SG * 10^3)
y = np.array([-1.3, -0.7, 0, 0.6, 1.3, 1.9, 2.6, 3.2, 3.9, 4.5])    # % alkohol per vol

a, b = np.polyfit(x, y, 1)

# Finner Alkoholprosenten so har utviklet seg
def vol_from_oechsle(Oechsle):
    return a * Oechsle +  b

# Tilregnetet saga vin, som tilsettes sukker i to omganger (Volum 1 og volum 2)
def vol_sagaVin(V_1, Oechsle_1, V_2, Oechsle_2):
    V_alkohol_1 = vol_from_oechsle(Oechsle_1)/100 * V_1
    V_alkohol_2 = vol_from_oechsle(Oechsle_2)/100 * V_2
    V_alkohol = V_alkohol_1 + V_alkohol_2
    vol = V_alkohol/V_2 * 100
    return vol, V_alkohol

Oechsle_1 = 1050 - 1030
V_1 = 16
Oechsle_2 = 1077  - 988
V_2 = 19
vol, V_alkohol = vol_sagaVin(V_1, Oechsle_1, V_2, Oechsle_2)


print("Alkoholprosenten i vinen er ", vol, "%, som gir", V_alkohol, "liter alkohol")

x_cont = np.linspace(-20, 100, 100)

plt.plot(x_cont, a*x_cont + b)
plt.plot(x, y, "xk")
plt.plot(Oechsle_1, vol_from_oechsle(Oechsle_1), "xr")
plt.plot(Oechsle_2, vol_from_oechsle(Oechsle_2), "xr")
plt.xlabel("$\\degree Oecshle$")
plt.ylabel("$\\% \\,\\, Vol \\,\\, Alk $")

plt.show()
