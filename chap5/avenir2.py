"""
Écrivez un algorithme similaire au précédent, mais en gérant les secondes. L’algorithme
affichera l’heure qu’il sera une seconde plus tard.
__author__ = Gvanderveen
__version__ = 0.1
"""

hour = int(input("Entrez l'heure"))
minute = int(input("Entrez les minutes"))
second = int(input("Entrez les secondes"))

time = 3600 * hour + minute * 60 + second
time = (time + 1) % (86400)
print(f"il sera {time // 3600} heures, {(time % 3600) // 60} minutes et {time % 60} secondes")
