"""
Écrivez un algorithme permettant, toujours sur le même principe, à l’utilisateur de saisir
un nombre déterminé de valeurs. L’algorithme, une fois a saisie terminée, renvoie la plus
grande valeur en précisant quelle position elle occupe dans le tableau. On prendra soin
d’effectuer la saisie dans un premier temps et la recherche de la plus grande valeur du
tableau dans un second temps
__author__ = Gvanderveen
__version__ = 0.1
"""

nbr_in = int(input("Combien de nombres allez vous saisir ? "))
tab = [int(input(f"Entre le nombre {i+1} sur {nbr_in} : ")) for i in range(nbr_in)]
print(f"la valeur max est {max(tab)} et se trouve à la {tab.index(max(tab))+1} ème position")