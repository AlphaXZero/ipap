"""
À partir des deux tableaux précédents, écrivez un algorithme qui calcule le Schtroumpf des
deux tableaux. Pour calculer le Schtroumpf, il faut multiplier chaque élément du tableau
1 par chaque élément du tableau 2 et additionner le tout.
__author__ = Gvanderveen
__version__ = 0.1
"""


tab1 = [1,2]
tab2 = [7,3]
smurf = 0
for i in tab1:
    for j in tab2:
        smurf += i * j
print(smurf)
