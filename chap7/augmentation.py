"""
Écrivez un algorithme qui permette la saisie d’un nombre quelconque de valeurs, sur le
principe de l’exercice tableau positif et négatif. Toutes les valeurs doivent être ensuite
augmentées de 1 et le nouveau tableau sera affiché à l’écran.
__author__ = Gvanderveen
__version__ = 0.1
"""
nbr_in = int(input("Combien de nombres allez vous saisir ? "))
tab = [int(input(f"Entre le nombre {i+1} sur {nbr_in} : "))+1 for i in range(nbr_in)]
print(tab)

