"""
Modifiez l’algorithme précédent, mais cette fois-ci on ne connaît pas à l’avance combien
l’utilisateur souhaite entrer de nombres. La saisie des nombres s’arrête lorsque l’utilisateur
entre un 0.
__author__ = Gvanderveen
__version__ = 0.1
"""

maxi = -100000000000
pos = 0
counter = 0
is_zero = False
while not is_zero:
    counter += 1
    in_usr = int(input("Entrez un nombre ou 0 pour arrêter : "))
    if in_usr == 0:
        is_zero = True
    elif in_usr > maxi:
        pos = counter
        maxi = in_usr
        
print(f"Le {pos} ème nombre est le plus grand et il vaut : {maxi}")
