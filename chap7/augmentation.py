"""
Écrivez un algorithme qui permette la saisie d’un nombre quelconque de valeurs, sur le
principe de l’exercice tableau positif et négatif. Toutes les valeurs doivent être ensuite
augmentées de 1 et le nouveau tableau sera affiché à l’écran.
__author__ = Gvanderveen
__version__ = 0.1
"""
nbr_in = int(input("Combien de nombres allez vous saisir ? "))
tab = [i for i in range(nbr_in)]

for i in range(nbr_in):
    tab[i] = int(input(f"Entre le nombre {i+1} sur {nbr_in} : "))

tab_incr = [i+1 for i in tab]
print(tab_incr)