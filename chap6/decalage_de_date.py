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

for i in range(nbr_days):
    if month in (1, 3, 5, 6, 7, 10, 12):
        if day > 31:
            raise ValueError("invalid day")  # or print()
        day = (day % 31) + 1
    elif month in (4, 8, 9, 11):
        if day > 30:
            raise ValueError("invalid day")
        day = (day % 30) + 1
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if day > 29:
                raise ValueError("invalid day")
            day = (day % 29) + 1
        else:
            if day > 28:
                raise ValueError("invalid day")
            day = (day % 28) + 1
    else:
        raise ValueError("invalid month")
    if day == 1:
        month = (month % 12) + 1
    if month == 1 and day == 1:
        year += 1

print(f"{day}/{month}/{year}")
