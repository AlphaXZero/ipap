"""
 Un magasin de photocopies facture 0,05€ les 10 premières photocopies, 0,04€ les 20
 suivantes et 0,03€ au-delà. Écrivez un algorithme qui demande à l’utilisateur le nombre
 de photocopies effectuées et qui affiche la facture correspondante.
__author__ = Gvanderveen
__version__ = 0.1
"""

nbr = int(input("Entrez le nombre de photocopies : "))
rate = 0.03  # base rate


if nbr <= 10:
    rate = 0.05
elif 10 < nbr <= 20:
    rate = 0.04


print(f"Ces {nbr} photocopies coûtenront {rate * nbr} €")
