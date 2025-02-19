"""
Écrivez un algorithme qui recherche la plus grande valeur au sein d’un tableau à deux
dimensions (12x8) préalablement rempli de valeurs numériques
__author__ = Gvanderveen
__version__ = 0.1
"""
import math
tab = [[i for i in range(13)] for j in range(6)]

maxi = -math.inf

for line in tab:
    for row in line:
        if row > maxi:
            maxi = row

print(maxi)