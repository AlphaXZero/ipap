"""
Écrivez  un  algorithme  permettant  à  l’utilisateur  de  saisir  les  notes  d’une  classe.
L’algorithme, une fois la saisie terminée, renvoie le nombre de ces notes supérieures à la
moyenne de la classe
__author__ = Gvanderveen
__version__ = 0.1
"""

tab= []
while True:
    usr_in = int(input("Entrez un nombre ou -1 pour arrêter : "))
    if usr_in == -1:
        break
    else:
        tab.append(usr_in)

average = 0
for i in tab:
    average += i
average /= len(tab)

nbr_gt_avg = 0
for i in tab:
    if i > average:
        nbr_gt_avg += 1

print(f"Les notes sont {tab}, la moyenne est {average}, il y a {nbr_gt_avg} notes au dessus de la moyenne")