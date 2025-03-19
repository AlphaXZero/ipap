"""
Écrivez un algorithme permettant de stocker dans une liste tous les entiers positifs de
3 chiffres tel que, pour chaque entier, la somme des chiffres est un diviseur du produit
de ces chiffres. Ex: 514 est un nombre valide, car 5 + 1 + 4 = 10 est un diviseur de 5 × 1 ×
4 = 20.
__author__ = Gvanderveen
__version__ = 0.1
"""

tab = []

for i in range(100, 1000):
    a, b, c = map(int, str(i))
    if (a * b * c) % (a + b + c) == 0:
        tab += [i]
print(tab)