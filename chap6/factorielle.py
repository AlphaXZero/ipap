"""
Écrivez un algorithme qui demande un nombre de départ, puis qui calcule la factorielle.
Exemple avec le nombre 5: 1 ∗ 2 ∗ 3 ∗ 4 ∗ 5 = 120
__author__ = Gvanderveen
__version__ = 0.1
"""

number = int(input("Entrez un nombre : "))
tot = 1
for i in range(number):
    tot *= i+1

print(tot)