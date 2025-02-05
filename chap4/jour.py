"""
Écrivez un algorithme qui demande un nombre entre 1 et 7 à l’utilisateur, puis qui affiche
le jour de la semaine correspondant.
__author__ = Gvanderveen
__version__ = 0.1
"""

week = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

choice = int(input("Entrez un nombre entre 1 et 7 : "))

if 1 > choice < 7:
    print("mauvais nombre")
else:
    print(week[choice - 1])
