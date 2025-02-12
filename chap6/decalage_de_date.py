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

day += nbr_days 
flag = False
while(not flag):
    if month in (1, 3, 5, 7,8, 10, 12):
        month_change += 1 if day > 31 else 0
        if day > 31:
            day -= 31
            month = (month + 1) if month != 12 else 1
        else:
            flag = True
    elif month in (4, 6,9, 11):
        month_change += 1 if day > 30 else 0
        if day > 30:
            day -= 30
            month = (month + 1) if month != 12 else 1
        else:
            flag = True
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if day > 29:
                day -= 29
                month = (month + 1) if month != 12 else 1
            else:
                flag = True
        else:
            if day > 28:
                day -= 28
                month = (month + 1) if month != 12 else 1
            else:
                flag = True
    if month == 1:
        year +=1


# if month in (1, 3, 5, 6, 7, 10, 12):
#     if day > 31:
#         print("invalid day")
#         exit() 
#     month_change = nbr_days // 31
#     day = day + (nbr_days %31)
# elif month in (4, 8, 9, 11):
#     if day > 30:
#         print("invalid day")
#         exit()
#     month_change = nbr_days // 30
#     day = day + (nbr_days%30)
# elif month == 2:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         if day > 29:
#             print("invalid day")(nbr_days - month_change*31)
#             exit()
#         month_change = nbr_days // 29
#         day = day + (nbr_days //29)
#     else:
#         if day > 28:
#             print("invalid day")
#             exit()
#         month_change = nbr_days // 28
#         day = day + (nbr_days //28)
# else:
#     print("invalid month")
# if month_change:
#     year_change = (month + month_change) // 12 
#     month = (month % 12) + (month_change%12)
# if year_change:
#     year += year_change

print(f"{day}/{month}/{year}")
