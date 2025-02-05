"""
 Un magasin de photocopies facture 0,05€ les 10 premières photocopies, 0,04€ les 20
 suivantes et 0,03€ au-delà. Écrivez un algorithme qui demande à l’utilisateur le nombre
 de photocopies effectuées et qui affiche la facture correspondante.
__author__ = Gvanderveen
__version__ = 0.1
"""

nbr = int(input("Entrez le nombre de photocopies : "))
total = 0  # base rate

if nbr < 0:
    print("impossible d'imprimer un nombre négatif de feuilles")
elif nbr <= 10:
    total = 0.05 * nbr
elif 10 < nbr <= 30:
    total = 0.04 * (nbr - 10) + (10 * 0.05)
else:
    total = 0.03 * (nbr - 30) + (10 * 0.05) + (20 * 0.04) 

print(f"Ces {nbr} photocopies coûtenront {total} €")
