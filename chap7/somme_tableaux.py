"""
Écrivez  un  algorithme  constituant  un  tableau  à  partir  des  deux  tableaux  suivants.  Le
nouveau tableau contiendra la somme des éléments des deux tableaux de départ
__author__ = Gvanderveen
__version__ = 0.1
"""

tab1 = [4,8,7,9,1,5,4,6]
tab2 = [7,6,5,2,1,3,7,4]    
tab_summed = []
for i in range(len(tab1)):
    tab_summed.append(tab1[i]+tab2[i])
print(tab_summed)