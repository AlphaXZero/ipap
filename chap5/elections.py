"""
 Les élections législatives en Bordeciel obéissent à la règle suivante:
 • Lorsqu’un des candidats obtient plus de 50% des suffrages, il est élu dès le premier tour.
 • En cas de second tour, seuls les candidats ayant obtenu au moins 12,5% des voix au
 premier tour peuvent participer.
 Écrivez un algorithme qui permette la saisie des scores de quatre candidats au premier
 tour. Cet algorithme traitera ensuite uniquement le premier candidat. Il dira s’il est élu,
 battu, en ballottage favorable (il participe au second tour en étant arrivé en tête à l’issue
 du premier tour), ou en ballottage défavorable (il participe au second tour sans avoir été
 en tête au premier tour).
__author__ = Gvanderveen
__version__ = 0.1
"""

result1 = int(input("Entrez le résultat du premier"))
result2 = int(input("Entrez le résultat du deuxième"))
result3 = int(input("Entrez le résultat du troisième"))
result4 = int(input("Entrez le résultat du quatrième"))

