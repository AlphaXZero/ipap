"""
Écrivez un algorithme capable de prédire l’avenir. Demandez à l’utilisateur de rentrer
l’heure puis les minutes. L’algorithme indiquera l’heure qu’il sera une minute plus tard.
On suppose que l’utilisateur entre une heure valide.
__author__ = Gvanderveen
__version__ = 0.1
"""

hour = int(input("Entrez l'heure"))
minute = int(input("Entrez les minutes"))

time = 60 * hour + minute
time = (time + 1) % (1440)

print(f"il sera {time // 60} heures et {time % 60} minutes")