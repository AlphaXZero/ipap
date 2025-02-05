"""
Écrivez un algorithme qui demande un nombre compris entre 10 et 20, jusqu’à ce que la
réponse convienne. En cas de réponse supérieure à 20, on fera apparaître un message:
Plus petit!, et inversement Plus grand! si le nombre est inférieur à 10.
__author__ = Gvanderveen
__version__ = 0.1
"""


number = -1

while not (10 <= number <= 20):
    number = int(input("Entrez un nombre entre 10 et 20 : "))
    if number < 10:
        print("plus grand")
    else:
        print("plus petit")