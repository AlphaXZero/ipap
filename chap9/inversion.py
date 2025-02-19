"""
Écrivez un algorithme qui inverse l’ordre des éléments d’un tableau préalablement saisi.
Il est interdit d’utiliser un slice ou une fonction Python existante!.
__author__ = Gvanderveen
__version__ = 0.1
"""

tab = [1, 12, 4, 5, 2, 9, -1, 9,6]

for i in range(len(tab)//2):
    tab[i] , tab[-(i+1)] = tab[-(i+1)] , tab[i]
print(tab)