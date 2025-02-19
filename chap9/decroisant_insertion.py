"""
Écrivez un algorithme qui trie un tableau dans l’ordre décroissant avec un tri par insertion
__author__ = Gvanderveen
__version__ = 0.1
"""

tab = [1,12,4,5,2,9,-1,8]

for i in range(1,len(tab)):
    for j in range(i-1,-1,-1):
        if tab[j+1]>tab[j]:
            tab[j+1] , tab[j] = tab[j],tab[j+1]
         


print(tab)
