from Søppel.calc import *

def newtonian_gravity(m_1, m_2, r):
    return G * m_1 * m_2 / r**2


def colombs_law(q_1, q_2, r):
    return k * q_1 *q_2 / r**2