"""
Écrivez un algorithme qui déclare un tableau de 9 notes, dont on fait ensuite saisir les
valeurs par l’utilisateur.
__author__ = Gvanderveen
__version__ = 0.1
"""

tab = [input(f"Entrez votre {i+1} ème résultat : ") for i in range(9)]

print(tab)