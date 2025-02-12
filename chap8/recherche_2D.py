"""
Écrivez un algorithme qui recherche la plus grande valeur au sein d’un tableau à deux
dimensions (12x8) préalablement rempli de valeurs numériques
__author__ = Gvanderveen
__version__ = 0.1
"""

tab = [[i for i in range(13)] for j in range(6)]

maxi = -100000000

for line in tab:
    for row in line:
        if row > maxi:
            maxi = row

print(maxi)