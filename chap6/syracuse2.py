"""
Modifiez l’algorithme précédent pour ajouter différentes informations:
• le temps de vol: c’est le nombre d’éléments de la suite jusqu’à ce que la suite atteigne 1.
• Le temps de vol en altitude: c’est le nombre d’éléments de la suite au-dessus du nombre
de base.
• l’altitude maximale: c’est la valeur maximale de la suite.
__author__ = Gvanderveen
__version__ = 0.1
"""

nbr = 10
nbr_init = nbr
fly = 0
h_fly = 0
maxi = 0

while nbr > 1:
    print(nbr)
    if nbr > nbr_init:
        h_fly += 1
    if nbr > maxi:
        maxi = nbr
    if nbr % 2 == 0:
        nbr /= 2
    else:
        nbr = nbr * 3 + 1
    fly += 1

print(1)
print(f"tps envol : {fly}, tps haut-vol : {h_fly}, max : {maxi}")