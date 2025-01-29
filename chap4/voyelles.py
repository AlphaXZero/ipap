"""
Écrivez un algorithme qui demande une lettre à l’utilisateur, puis qui l’informe s’il s’agit
d’une voyelle ou d’une consonne.
__author__ = Gvanderveen
__version__ = 0.1
"""

letter = input("Entrez une lettre")

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "y":
    print("c'est une voyelle")
else:
    print("c'est une consomne")

# if letter in "aeiouy":
#     print("c'est une voyelle")
# else:
#     print("c'est une consomne")