"""
Écrivez un algorithme qui demande à l’utilisateur un nombre compris entre 1 et 3 jusqu’à
ce que la réponse convienne
__author__ = Gvanderveen
__version__ = 0.1
"""

number = -1

while not (1 <= number <= 3):
    number = int(input("Entrez un nombre entre 1 et 3 : "))
