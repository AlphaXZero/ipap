"""
Écrivez un algorithme qui recherche la plus grande valeur au sein d’un tableau à deux
dimensions (12x8) préalablement rempli de valeurs numériques
__author__ = Gvanderveen
__version__ = 0.1
"""
import random
import math
tab = [[random.randint(0,400) for i in range(12)] for j in range(8)]
print(tab)
def max_finder(inp: list) -> int:
    """
    Iterate through a 2D list and return its maximum value
    """
    maxi = -math.inf
    for line in inp:
        if max(line) > maxi:
            maxi = max(line)
    return maxi

print(max_finder(tab))