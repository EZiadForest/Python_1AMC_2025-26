""" Module de fonctions arithmétiques
"""

def euclide(a, b):
    """ Algorithme d'Euclide étendu
        Retourne le pgcd de `a` et `b`, ainsi que les coefficients de
        Bézout `u` et ` v` tels que au + bv = pgcd(a, b).
    """
    r0, u0, v0, r1, u1, v1 = a, 1, 0, b, 0, 1
    while r1 != 0:
        q = r0 // r1
        r0, u0, v0, r1, u1, v1 = (
        r1, u1, v1, r0 - q * r1, u0 - q * u1, v0 - q * v1)
    return r0, u0, v0