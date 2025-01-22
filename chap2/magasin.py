"""__author__ = Gvanderveen
__version__ = 0.1
exercice 2.5 Magasin
"""

article = input("Entrez le nom de l'article")
prix_htv = int(input("Entrez le prix hors TVA"))
nbr = int(input("Entrez le nombre d'articles"))
taux_tva = int(input("Entrez le taux tva"))
print("les", nbr, article, "coûtent", (prix_htv * taux_tva) / 100 + prix_htv, "TTC")
