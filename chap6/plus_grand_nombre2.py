"""
Modifiez l’algorithme précédent pour qu’il affiche en plus en quelle position avait été saisie
ce nombre.
__author__ = Gvanderveen
__version__ = 0.1
"""
maxi = -100000000000
pos = 0
for i in range(20):
    in_usr = int(input(f"Entrez un {i+1}/20 nombre : "))
    if in_usr > maxi:
        pos = i+1
        maxi = in_usr
print("nbr :",maxi,"position : ", pos)