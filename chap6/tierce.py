"""
Écrivez un algorithme qui permette de connaître les chances de gagner au Tiercé, Quarté
et Quinté. On demande à l'utilisateur le nombre de chevaux partants et le nombre de
chevaux joués. Les deux messages affichés devront être:
Dans l'ordre: une chance sur X de gagner
Dans le désordre: une chance sur Y de gagner
X et Y nous sont donnés par les formules suivantes, si n est le nombre de chevaux partants
et 𝑝 le nombre de chevaux joués. Pour rappel, le signe ! signifie factorielle en mathématique.
𝑋 = 𝑛! / (𝑛−𝑝)!
𝑌 = 𝑛! / (𝑝!∗(𝑛−𝑝)!)
__author__ = Gvanderveen
__version__ = 0.1
"""

horses_nbr = int(input("Combien de chevaux vont participer ? ")) 
horses_bet = int(input("Sur combien de chevaux vous jouez ? "))

horses_nbr_fact = 1
for i in range(horses_nbr):
    horses_nbr_fact *= i+1

horses_bet_fact = 1
for i in range(horses_nbr):
    horses_bet_fact *= i+1

horses_nbr_bet_fact = 1
for i in range(horses_nbr):
    horses_nbr_bet_fact *= i+1

print(f"Dans l'odre : une chance sur {horses_nbr_fact / horses_nbr_bet_fact} de gagner")
print(f"Dans le désordre : une chance sur {horses_nbr / (horses_bet_fact * horses_nbr_bet_fact)} de gagner")
