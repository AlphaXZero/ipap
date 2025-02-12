"""
Écrivez un algorithme qui demande un nombre de départ, puis qui calcule la somme des
entiers jusqu’à ce nombre. On souhaite afficher uniquement le résultat. Exemple avec le
nombre 5: 1 + 2 + 3 + 4 + 5 = 15
__author__ = Gvanderveen
__version__ = 0.1
"""

number = int(input("Entrez un nombre : "))
sum_a = 0
for i in range(number):
    sum_a += i+1
print(sum_a)