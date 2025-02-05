"""
Écrivez un algorithme qui demande un nombre de départ, puis qui affiche ensuite les dix
nombres suivants. Par exemple, si l’utilisateur entre le nombre 33, l’algorithme affichera
les nombres 34 à 43.
__author__ = Gvanderveen
__version__ = 0.1
"""

number = int(input("Entrez un nombre : "))
max_value = number + 10
while number < max_value:
    number += 1
    print(number)
