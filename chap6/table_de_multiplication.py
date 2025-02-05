"""
Écrivez un algorithme qui demande un nombre de départ, puis écrit la table de multipli-
cation de ce nombre, présentée comme suit:
Table de 8:
8 × 1 = 8
8 × 2 = 16
...
8 × 10 = 80
__author__ = Gvanderveen
__version__ = 0.1
"""

number = int(input("Entrez un nombre : "))

for i in range(10):
    print(f"{number} * {i + 1} = {(i + 1) * number}")
