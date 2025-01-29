"""
Écrivez un algorithme qui demande trois nombres à l’utilisateur, puis qui affiche le
nombre maximum
__author__ = Gvanderveen
__version__ = 0.1
"""

nbr1 = int(input("Entrez le premier nombre : "))
nbr2 = int(input("Entrez le deuxième nombre : "))
nbr3 = int(input("Entrez le troisième nombre : "))


if nbr1 == 0 or nbr2 == 0:
    print("Le résultat est nul")
elif (nbr1 < 0) ^ (nbr2 < 0):
    print("Le résultat est négatif")
else:
    print("le résultat est positif")
