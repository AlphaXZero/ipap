"""
Modifiez l’algorithme Notes afin d’effectuer et d’afficher le calcul de la moyenne des notes.
__author__ = Gvanderveen
__version__ = 0.1
"""

tab = [0 for i in range(9)]

# for i in range(len(tab)):
#     tab[i] = int(input(f"Entrez votre {i+1} ème résultat : "))

# print(f"les notes sont {tab}, votre moyenne est {sum(tab)/len(tab):.2f}")


#sans sum :

tot = 0
for i in range(len(tab)):
    tab[i] = int(input(f"Entrez votre {i+1} ème résultat : "))
    tot += tab[i]

print(f"les notes sont {tab}, votre moyenne est {tot/len(tab):.2f}")
