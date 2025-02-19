"""
Écrivez  un  algorithme  permettant  à  l’utilisateur  de  saisir  les  notes  d’une  classe.
L’algorithme, une fois la saisie terminée, renvoie le nombre de ces notes supérieures à la
moyenne de la classe
__author__ = Gvanderveen
__version__ = 0.1
"""

tab = []
while True:
    usr_in = int(input("Entrez un nombre ou -1 pour arrêter : "))
    if usr_in == -1:
        break
    else:
        tab.append(usr_in)

avg = sum(tab) / len(tab)

print(
    f"Les notes sont {tab}, la moyenne est {avg}, il y a {len([1 for note in tab if note > avg])} notes au dessus de la moyenne"
)
    