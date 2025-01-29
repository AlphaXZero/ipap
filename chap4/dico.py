"""
Écrivez un algorithme qui demande trois mots à l’utilisateur, puis qui l’informe s’ils sont
rangés ou non dans l’ordre alphabétique. Attention, il ne faut pas les trier!
__author__ = input("Entrez un mot") Gvanderveen
__version__ = 0.1
"""


word1 = input("Entrez un mot")
word2 = input("Entrez un mot")
word3 = input("Entrez un mot")

if word1 < word2 and word2 < word3:
    print("alphabétique")
else:
    print("non-alphabétique")   