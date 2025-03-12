"""
Écrivez un algorithme qui trie un tableau dans l’ordre décroissant avec un tri par bulle
__author__ = Gvanderveen
__version__ = 0.1
"""

tab = [1,12,4,5,2,9,-1,8]

for i in range(len(tab)-1,0,-1):
    for j in range(0,i):
        if tab[j+1] > tab[j]:
            tab[j+1], tab[j] = tab[j], tab[j+1]

print(tab)