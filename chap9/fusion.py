"""
Écrivez un algorithme qui fusionne deux tableaux existants dans un troisième, qui sera
trié. On présume que les deux tableaux de départs sont préalablement triés
__author__ = Gvanderveen
__version__ = 0.1
"""

tab1 = [1,3,4,10,12]
tab2 = [2,5,9,10]

#plus rapide
# print(sorted(tab1+tab2)) 

tab_sorted = []
for i in range(len(tab1)+len(tab2)):
    if len(tab2)>0 and tab1[0] > tab2[0] :
        tab_sorted.append(tab2.pop(0))
    else:
        tab_sorted.append(tab1.pop(0))


print(tab_sorted)