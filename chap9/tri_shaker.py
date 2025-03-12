"""
Écrivez un algorithme qui trie un tableau avec le tri shaker.
__author__ = Gvanderveen
__version__ = 0.1
"""

tab = [10,2,3,5,8,9,12,7]

for i in range(len(tab)-1,0,-2):
    for j in range(0,i):
        if tab[j+1] < tab[j]:
            tab[j+1], tab[j] = tab[j], tab[j+1]
    for x in range(i-2,0,-1):

  


print(tab)