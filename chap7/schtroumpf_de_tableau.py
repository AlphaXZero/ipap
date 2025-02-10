"""
À partir des deux tableaux précédents, écrivez un algorithme qui calcule le Schtroumpf des
deux tableaux. Pour calculer le Schtroumpf, il faut multiplier chaque élément du tableau
1 par chaque élément du tableau 2 et additionner le tout.
__author__ = Gvanderveen
__version__ = 0.1
"""

tab1 = [4, 8, 7, 9, 1, 5, 4, 6]
tab2 = [7, 6, 5, 2, 1, 3, 7, 4]
smurf = 0

# for i in range(len(tab1)):
#     smurf += tab1[i] * tab2[i]

for i in range(len(tab1)):
        for j in range(len(tab1)):
            smurf += tab1[i] * tab2[j]

print(smurf)
