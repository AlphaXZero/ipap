"""
 Les habitants de Lenclume paient l’impôt selon les règles suivantes:
 • Les hommes de plus de 20 ans paient l’impôt;
 • Les femmes paient l’impôt si elles ont entre 18 et 35 ans;
 • Les autres ne paient pas d’impôts.
 Écrivez un algorithme qui demande l’âge et le sexe de l’Argonien, puis qui indiquera s’il
 doit payer un impôt ou non.
__author__ = Gvanderveen
__version__ = 0.1
"""

age = int(input("Quelle est votre âge"))
gender = input("Entrez h si vous êtes un homme ou f si vous êtes une femme")
impot = False

if gender not in "hf" or len(gender) != 1:
    raise Exception("Mauvaise saisie sur le sexe") # print :)
if age < 0:
    raise Exception("Mauvaise saisie sur l'âge")

if gender == "h" and age > 20:
    impot = True
if gender == "f" and 18 >= age >= 35:
    impot = True

print("il faut payer") if impot else print("il ne faut pas payer")  
