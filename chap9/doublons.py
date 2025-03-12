"""
Écrivez un algorithme qui permette de saisir les éléments d’un tableau et qui vérifie s’ils
sont tous différents. L’algorithme affichera simplement s’il y a un ou plusieurs doublons
ou aucun doublon le cas échéant
__author__ = Gvanderveen
__version__ = 0.1
"""
#TODO break ?
is_typing = True
tab=[]
dubble = 0

while(is_typing):
    usr_in = input("Entre un nombre ou q pour arrêter : ")
    if usr_in == "q":
        is_typing = False
    else:
        if usr_in in tab:
            dubble +=1
        tab.append(usr_in)
if dubble:
    print(f"il y a {dubble} doublons")
else:
    print("il n'y a aucun doublons")