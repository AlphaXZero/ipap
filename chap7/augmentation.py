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
tab1 = [4, 8, 7, 9, 1, 5, 4, 6]
tab2 = [7, 6, 5, 2, 1, 3, 7, 4]
smurf = 0

# for i in range(len(tab1)):
#     smurf += tab1[i] * tab2[i]

for i in range(len(tab1)):
        for j in range(len(tab1)):
            smurf += tab1[i] * tab2[j]

print(smurf)
