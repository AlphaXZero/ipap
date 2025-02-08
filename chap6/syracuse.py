"""
Écrivez un algorithme qui affiche la conjecture de Syracuse. La conjecture de Syracuse est
une suite d’entiers naturels définie de la manière suivante:
• On part d’un nombre entier plus grand que zéro;
• Si ce nombre est pair, on le divise par deux;
• Si ce nombre est impair, on le multiplie par trois et on ajoute un.
En répétant l’opération, on obtient une suite d’entiers positifs qui va finir par arriver à 1,
avant de démarrer un cycle (1,4,2,1…)
__author__ = Gvanderveen
__version__ = 0.1
"""

nbr = 10

while nbr > 1:
    print(nbr)
    if nbr % 2 == 0:
        nbr /= 2
    else:
        nbr = nbr * 3 + 1

print(1)
