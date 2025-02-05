"""
Une  compagnie  d’assurance  automobile  propose  à  ses  clients  quatre  sortes  de  tarifs
identifiables par une couleur, du moins au plus onéreux: le tarif bleu, le tarif vert, le tarif
orange et le tarif rouge. Le tarif dépend de la situation du conducteur:
1. Un conducteur de moins de 25 ans et titulaire du permis depuis moins de deux ans, se
voit attribuer le tarif rouge, si toutefois il n’a jamais été responsable d’accident. Sinon,
la compagnie refuse de l’assurer.
2. Un conducteur de moins de 25 ans et titulaire du permis depuis plus de deux ans, ou
de plus de 25 ans, mais titulaire du permis depuis moins de deux ans a droit au tarif
orange s’il n’a jamais provoqué d’accident, au tarif rouge s’il a eu un accident, sinon il
est refusé.
5
3. Un conducteur de plus de 25 ans titulaire du permis depuis plus de deux ans bénéficie
du tarif vert s’il n’est à l’origine d’aucun accident, du tarif orange s’il a eu un accident,
du rouge s’il en a eu deux, et sera refusé au-delà.
4. De  plus,  pour  encourager  la  fidélité  des  clients  acceptés,  la  compagnie  propose  un
contrat de la couleur immédiatement la plus avantageuse s’il est client de la compagnie
depuis plus de 5 ans. Ainsi, s’il satisfait cette exigence, un client normalement vert
deviendra bleu, un client normalement orange devient vert et le rouge devient orange.
Écrivez un algorithme permettant de saisir les données nécessaires (sans contrôle de saisie)
et de traiter le problème
__author__ = Gvanderveen
__version__ = 0.1
"""

drv_age = int(input("Entrez votre âge : "))
has_two_year_exp = (
    True if input("Avez-vous le permis depuis + de 2 ans ? (y/n)") == "y" else False
)
has_five_year_sub = (
    True
    if input("Etes vous assurez chez nous depuis + de 5 ans ? (y/n)") == "y"
    else False
)
nbr_accident = int(input("Combien d'accidents avez vous eu ? : "))
color = ""
if not has_two_year_exp and drv_age < 25:
    if nbr_accident == 0:
        color = "rouge"
elif has_two_year_exp and drv_age < 25:
    if nbr_accident == 0:
        color = "orange"
    elif nbr_accident == 1:
        color = "rouge"
elif has_two_year_exp and drv_age >= 25:
    if nbr_accident == 0:
        color = "vert"
    elif nbr_accident == 1:
        color = "orange"
    elif nbr_accident == 2:
        color = "rouge"
if has_five_year_sub:
    match color:
        case "vert":
            color = "bleu"
        case "orange":
            color = "vert"
        case "rouge":
            color = "orange"
color = color if color else "refusé"
print(f"Vous avez le tarif : {color}")