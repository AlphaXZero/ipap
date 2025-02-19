"""
Écrivez un algorithme qui permette de saisir un nombre quelconque de valeurs et qui les
range au fur et à mesure dans un tableau. L’algorithme, une fois la saisie terminée, doit
dire si les éléments du tableau sont tous consécutifs ou non. Par exemple, si le tableau est:
12 13 14 15 16 17 18
ses éléments sont consécutifs. En revanche, si le tableau est:
9 10 11 15 16 17 18
ses éléments ne sont pas tous consécutifs
__author__ = Gvanderveen
__version__ = 0.1
"""

is_typing = True
tab = []

while(is_typing):
    usr_in = input("Entrez un nombre ou q pour arrêter : ")
    if usr_in == "q":
        is_typing = False
    else:
        tab.append(int(usr_in))

print(tab)
is_cons =True
direction = 0
if tab[1]>tab[0]:
    direction = 1
else:
    direction = -1
for i in range(1,len(tab)):
    if direction == 1:
        if tab[i]<tab[i-1] or tab[i]-tab[i-1] != 1:
            is_cons = False
    elif direction == -1:
        if tab[i]>tab[i-1] or tab[i]-tab[i-1] != -1:
            is_cons = False
if is_cons:
    print("consécutif")
else:
    print("non-consécutif")