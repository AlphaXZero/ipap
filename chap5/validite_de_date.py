"""
Écrivez un algorithme qui demande à l’utilisateur un numéro de jour, de mois et d’année,
puis qui renvoie s’il s’agit ou non d’une date valide. Pour rappel, une année est bissextile
si elle est divisible par 4. Les années divisibles par 100 ne sont pas bissextiles, mais les
années divisibles par 400 le sont.
__author__ = Gvanderveen
__version__ = 0.1
"""

day = int(input("Enter the day : "))
month = int(input("Enter the month (number) : "))
year = int(input("Enter the year : "))

if month in (1, 3, 5, 6, 7, 10, 12):
    if day > 31:
        print("invalid day")  # or print()
elif month in (4, 8, 9, 11):
    if day > 30:
        print("invalid day")
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        if day > 29:
            print("invalid day")
    else:
        if day > 28:
            print("invalid day")
else:
    print("invalid month")

print(f"{day}/{month}/{year}")
