"""
Écrivez un algorithme qui trie un tableau dans l’ordre décroissant avec un tri par insertion
__author__ = Gvanderveen
__version__ = 0.1
"""

tab = [1,12,4,5,2,9,-1,8]

for i in range(1,len(tab)):
    for j in range(i):
        if tab[j]>tab[j-1]:
            for x in range(0,i):
                if tab[j]>tab[x]:
                    tab[j],tab[x]=tab[x],tab[j]

print(tab)