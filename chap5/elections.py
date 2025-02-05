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

result1 = int(input("Entrez le résultat du premier : "))
result2 = int(input("Entrez le résultat du deuxième : "))
result3 = int(input("Entrez le résultat du troisième : "))
result4 = int(input("Entrez le résultat du quatrième : "))

first_cand_percent = result1 / (result1 + result2 + result3 + result3)

if first_cand_percent > 0.5:
    print(f"élu avec {first_cand_percent * 100:.2f}% des voix")
elif first_cand_percent > 0.125:
    if result1 == max(result1, result2, result3, result4):
        print(f"Ballotage favorable avec {first_cand_percent * 100:.2f}% des voix")
    else:
        print(f"Ballotage défavorable avec {first_cand_percent * 100:.2f}% des voix")
else:
    print(f"perdu avec {first_cand_percent * 100:.2f}% des voix")