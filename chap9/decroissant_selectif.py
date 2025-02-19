"""
Écrivez un algorithme qui trie un tableau dans l’ordre décroissant avec un tri par sélection
__author__ = Gvanderveen
__version__ = 0.1
"""
import math
#TODO utile le enumerate ?  
tab = [1, 12, 4, 5, 2, 9, -1, 9]
for i, initial_index in enumerate(tab):
    maxi = -math.inf
    for j in range(i, len(tab)):
        if tab[j] > maxi:
            maxi = tab[j]
            ind_actu = j
    tab[i], tab[ind_actu] = tab[ind_actu], initial_index
print(tab)
