"""
Écrivez un algorithme qui demande trois nombres à l’utilisateur, puis qui affiche le
nombre maximum
__author__ = Gvanderveen
__version__ = 0.1
"""

nbr1 = int(input("Entrez le premier nombre : "))
nbr2 = int(input("Entrez le deuxième nombre : "))
nbr3 = int(input("Entrez le troisième nombre : "))

if nbr1 >= nbr2 and nbr1 >= nbr3:
    print(nbr1)
elif nbr2 >= nbr1 and nbr2 >= nbr3:
    print(nbr2)
else:
    print(nbr3)

# print(max(nbr1,nbr2,nbr3))