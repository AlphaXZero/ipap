"""
Écrivez un algorithme permettant, toujours sur le même principe, à l’utilisateur de saisir
un nombre déterminé de valeurs. L’algorithme, une fois a saisie terminée, renvoie la plus
grande valeur en précisant quelle position elle occupe dans le tableau. On prendra soin
d’effectuer la saisie dans un premier temps et la recherche de la plus grande valeur du
tableau dans un second temps
__author__ = Gvanderveen
__version__ = 0.1
"""
import math
nbr_in = int(input("Combien de nombres allez vous saisir ? "))
tab = [i for i in range(nbr_in)]

for i in range(nbr_in):
    tab[i] = int(input(f"Entre le nombre {i+1} sur {nbr_in} : "))

# maxi = -math.inf
# ind = 0
# for i, nbr in enumerate(tab):
#     if nbr > maxi:
#         maxi = nbr
#         ind = i + 1
# print(f"la valeur max est {maxi} et se trouve à la {ind} ème position")

print(f"la valeur max est {max(tab)} et se trouve à la {tab.index(max(tab))+1} ème position")