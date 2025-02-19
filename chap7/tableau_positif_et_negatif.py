"""
Écrivez un algorithme permettant à l’utilisateur de saisir un nombre quelconque de valeurs
qui devront être stockés dans un tableau. L’utilisateur doit donc commencer par entrer le
nombre de valeurs qu’il compte saisir. Il effectuera ensuite cette saisie. Enfin, une fois la
saisie terminée, le programme affichera le nombre de valeurs négatives et le nombre de
valeurs positives.
__author__ = Gvanderveen
__version__ = 0.1
"""

nbr_in = int(input("Combien de nombres allez vous saisir ? "))
tab = [i for i in range(nbr_in)]

for i in range(nbr_in):
    tab[i] = int(input(f"Entrez le nombre {i + 1} sur {nbr_in} : "))

nbr_pos = 0
nbr_neg = 0

for data in tab:
    if data >= 0:
        nbr_pos += 1
    else:
        nbr_neg += 1

print(f"il y a {nbr_pos} nombres positifs et {nbr_neg} nombres négatifs")
