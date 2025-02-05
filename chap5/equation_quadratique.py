"""
Écrivez un algorithme qui permet de trouver toutes les racines d’une équation quadratique.
En algèbre, une équation quadratique est une équation sous la forme 𝑎𝑥2 + 𝑏𝑥 + 𝑐 = 0.
Une équation quadratique peut avoir une ou deux racines réelles ou complexes distinctes
selon la nature du discriminant de l’équation. Le discriminant de l’équation quadratique
est donné par Δ = 𝑏2 − 4𝑎𝑐.
Selon la nature de discriminant, la formule de recherche des racines est donnée par:
• cas 1:√Si le discriminant
Δ est positif, il y a deux racines réelles distinctes données par
√
Δ
Δ
−𝑏 + 2𝑎 et −𝑏 − 2𝑎 .
𝑏
• cas 2: Si le discriminant Δ est nul, il y a exactement une racine réelle donnée par − 2𝑎
• cas 3: Si le discriminant
Δ est négatif,
alors il y a deux racines complexes distinctes
√
√
𝑏
−Δ
𝑏
−Δ
données par: − 2𝑎 + 𝑖 2𝑎 et − 2𝑎 − 𝑖 2𝑎
L’algorithme va demander les paramètres a,b et c avant d’afficher les racines quadr
__author__ = Gvanderveen
__version__ = 0.1
"""

a = int(input("Entrez le a : "))
b = int(input("Entrez le b : "))
c = int(input("Entrez le c : "))
roots = 0
delta = b**2 - 4 * a * c

if delta < 0:
    print("no roots")
elif delta == 0:
    print(f"root is {-b / (2*a)}")
else:
    print(f"roots are {(-b - delta**(1/2)) / (2*a)} and {(-b + delta**(1/2)) / (2*a)}")