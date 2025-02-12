"""
Écrivez un algorithme qui lit une suite de prix en euros entiers, terminée par un 0,
correspondant aux achats d’un client. Calculer la somme que le client doit payer, lire la
somme qu’il paie et simuler la remise de la monnaie en affichant les textes billets de
10€: …, … autant de fois qu’il y a de coupures à rendre.
__author__ = Gvanderveen
__version__ = 0.1
"""

total = 0
usr_in = -1
while usr_in != 0:
    usr_in = int(input("Entrez un prix ou 0 pour arrêter : "))
    if usr_in >= 0:
        total += usr_in
    else:
        print("nombre invalide")

print(f"Total : {total}€")
while True:
    usr_pay = int(input("Combien allez vous payer ? "))
    if usr_pay >= total:
        usr_pay -= total
        break
    else:
        print("Erreur : entrez une somme supérieure ou égale au prix total")

# j'ai déduis qu'on avait le droit car on avait utilisé les tuples pour l'exo sur le jour en plus
# mais sinon j'aurai fais une grosse formule à base de tot//500, (tot%500)//200, ect
print(f"{usr_pay}€ à rendre soit : ")
for i in (500, 200, 100, 50, 20, 10, 5, 2, 1):
    print(f"-{'billets' if i > 2 else 'pièces'} de {i}€ remis : {usr_pay // i}")
    usr_pay %= i
