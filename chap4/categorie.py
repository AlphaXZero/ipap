"""
Écrivez un algorithme qui demande l’âge d’un enfant à l’utilisateur, puis qui l’informe de
sa catégorie:
Poussin de 6 à 7 ans;
Pupille de 8 à 9 ans;
Minime de 10 à 11 ans;
Cadet de 12 à 15 ans;
Espoir après 15 ans.
__author__ = Gvanderveen
__version__ = 0.1
"""

age = int(input("Quelle est ton âge ?"))
if age >15:
    print("Espoir")
elif age >= 12:
    print("Cadet")
elif age >= 10:
    print("Minime")
elif age >= 8:
    print("Pupille")
elif age >= 6:
    print("Poussin") 