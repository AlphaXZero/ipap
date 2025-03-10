"""
Écrivez un algorithme qui permette à l’utilisateur de supprimer une valeur d’un tableau
préalablement saisi. L’utilisateur donnera d’indice de la valeur qu’il souhaite supprimer.
Attention, il ne s’agit pas de mettre la valeur à 0, mais bel et bien supprimer la case du
tableau!. Il est interdit d’utiliser la fonction .remove() du tableau
__author__ = Gvanderveen
__version__ = 0.1
"""

tab = [1, 3, 10, 3, 2, 10]
print(tab)
#TODO pop ? del ?
ind_to_rem = int(input("Entrez l'indice de la liste que vous voulez retirer"))

tab = tab[0:ind_to_rem] + tab[ind_to_rem + 1 : len(tab)]
print(tab)
