"""
Écrivez un algorithme qui demande une date valide à l’utilisateur, puis qui demande un
nombre de jours. L’algorithme affichera alors la nouvelle date décalée. Ex : En entrant la
première date 01/03/2025 suivi du décalage 45, l’algorithme affichera 15/04/2025.
__author__ = Gvanderveen
__version__ = 0.1
"""

day = int(input("Enter the day : "))
month = int(input("Enter the month (number) : "))
year = int(input("Enter the year : "))
nbr_days = int(input("combien de jours voulez vous en plus ? : "))
month_change = 0
year_change = 0

if day < 0 or year < 0 or nbr_days < 0 or day <1:
    print("erreur : nombre négatif")
    quit()

while nbr_days > 0:
    if month in (1, 3, 5, 7, 8, 10, 12):
        if day > 31:
            print("erreur : mois de + de 31 jours")
            quit()
        if day + nbr_days > 31:
            nbr_days -= (31 - day + 1)
            day,month_change = 1,1
        else:
            day += nbr_days
            nbr_days = 0
    elif month in (4, 6, 9, 11):
        if day > 30:
            print("erreur : mois 4, 6, 9 ou 11 de + de 30 jours")
            quit()
        if day + nbr_days > 30:
            nbr_days -= (30 - day + 1)
            day,month_change = 1,1
        else:
            day += nbr_days
            nbr_days = 0
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if day > 29:
                print("erreur : février de + de 29 jours")
                quit()
            if day + nbr_days > 29:
                nbr_days -= (29 - day + 1)
                day,month_change = 1,1
            else:
                day += nbr_days
                nbr_days = 0
        else:
            if day > 28:
                print("erreur : février non-bisextile de + de 28 jours")
                quit()
            if day + nbr_days > 28:
                nbr_days -= (28 - day + 1)
                day,month_change = 1,1
            else:
                day += nbr_days
                nbr_days = 0
    if month_change:
        month, year_change = (month + 1, 0) if month !=12 else (1,1)
        month_change = 0
    if year_change:
        year += 1
        year_change = 0
print(f"{day}/{month}/{year}")
