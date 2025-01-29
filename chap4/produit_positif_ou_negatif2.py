"""
Écrivez un algorithme qui demande deux nombres à l’utilisateur, puis qui l’informe si leur
produit est positif, négatif ou nul. Attention, il ne faut pas calculer le produit.s
__author__ = Gvanderveen
__version__ = 0.1
"""

nbr1 = int(input("Entrez le premier nombre : "))
nbr2 = int(input("Entrez le deuxième nombre : "))


if nbr1 == 0 or nbr2 == 0:
    print("Le résultat est nul")
elif (nbr1 < 0) ^ (nbr2 < 0):
    print("Le résultat est négatif")
else:
    print("le résultat est positif")
