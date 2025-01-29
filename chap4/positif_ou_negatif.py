"""
Écrivez un algorithme qui demande un nombre à l’utilisateur, puis qui l’informe si ce
nombre est positif ou négatif. On considère que 0 est positif.
__author__ = Gvanderveen
__version__ = 0.1
"""


nbr = int(input("Entrez un nombre : "))
if nbr >= 0:
    print("Le nombre est positif")
else:
    print("Le nombre est négatif")