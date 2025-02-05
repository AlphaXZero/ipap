"""
Écrivez un algorithme qui demande successivement 20 nombres à l’utilisateur, puis qui lui
indique ensuite quel est le plus grand parmi ces 20 nombres.
__author__ = Gvanderveen
__version__ = 0.1
"""
maxi = -100000000000
for i in range(20):
    in_usr = int(input(f"Entrez un {i+1}/20 nombre : "))
    if in_usr > maxi:
        maxi = in_usr
print(maxi)