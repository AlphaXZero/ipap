"""
Écrivez un algorithme qui réponde True si un nombre donné par l’utilisateur est pair et
divisible par 5.
__author__ = Gvanderveen
__version__ = 0.1
"""

nbr = int(input("Entrez nombre"))
print(nbr % 2 != 0 or nbr % 5 == 0)
