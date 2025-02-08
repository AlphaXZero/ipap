"""
Écrivez un algorithme qui permette de connaître les chances de gagner au Tiercé, Quarté
et Quinté. On demande à l’utilisateur le nombre de chevaux partants et le nombre de
chevaux joués. Les deux messages affichés devront être:
Dans l’ordre: une chance sur X de gagner
Dans le désordre: une chance sur Y de gagner
X et Y nous sont donnés par les formules suivantes, si 𝑛 est le nombre de chevaux partants
et 𝑝 le nombre de chevaux joués. Pour rappel, le signe ! signifie factorielle en mathématique.
𝑋 =
𝑛!
(𝑛−𝑝)!
𝑌 =
𝑛!
𝑝!∗(𝑛−𝑝)!
__author__ = Gvanderveen
__version__ = 0.1
"""

horses_nbr = int(input("Combien de chevaux vont participer ? ")) 
horses_bet = int(input("Combien de chevaux vont participer ? "))

