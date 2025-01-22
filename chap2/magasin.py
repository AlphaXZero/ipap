"""
 Écrivez un algorithme qui lit le nom d’un article, son prix hors taxe, le nombre d’articles
 et le taux de TVA, puis qui fournit le prix total TTC correspondant. Faites en sorte que
 l’algorithme pose des questions claire et affiche un résultat complet.
__author__ = Gvanderveen
__version__ = 0.1
"""

article = input("Entrez le nom de l'article : ")
prix_htv = int(input("Entrez le prix hors TVA : "))
nbr = int(input("Entrez le nombre d'articles : "))
taux_tva = int(input("Entrez le taux tva (en %) : "))
print(
    "les",
    nbr,
    article,
    "coûtent",
    nbr * ((prix_htv * taux_tva) / 100 + prix_htv),
    "TTC",
)
