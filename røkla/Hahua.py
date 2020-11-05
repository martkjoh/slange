import math

S_1 = 0.6472065
S_1_feil = 0.0001172578
S_2 = 0.7557831
S_2_feil = 0.0002258688
S = S_2 - S_1
S_feil = math.sqrt(S_1_feil**2 + S_2_feil**2)

T_1 = 702.3862
T_2 = 725.567
T = 1/2*(T_1 + T_2)
T_feil = math.sqrt(1/2*((T_1-(T_1+T_2)/2)**2 + (T_2 - (T_1+T_2)/2)**2))

L = 2.277
L_feil = 0.001

M = 1.5003
M_feil = 0.0001

b = 0.044
b_feil = 0.001

r = 0.050
r_feil = 0.001

G = math.pi**2*S*b**2*r/(T**2*L*M*(1-b**3/(b**2+4*r**2)**(3/2)))

G_relativ = math.sqrt((S_feil/S)**2 + (2*b_feil/b)**2 + (r_feil/r)**2 + (2*T_feil/T)**2 + (L_feil/L)**2 + (M_feil/M)**2)

G_feil = G*G_relativ

print(S)
print(G)
print(100*G_relativ, '%', sep='')
print(G_feil)
print(G+G_feil)
