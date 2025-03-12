"""
Les exos du chap 10
__author__ = Gvanderveen
__version__ = 0.1
"""

import math


def max1(a: int, b: int) -> int:
    """
    Écrivez une fonction qui demande deux paramètres entiers, puis qui renvoie le nombre
    maximum
    """
    if a > b:
        return a
    return b


def max2_1(*nbr: int) -> int:
    """
    version avec args
    Écrivez  une  fonction  qui  demande  plusieurs  paramètres  entiers,  puis  qui  renvoie le
    nombre maximum
    """
    maxi = -math.inf
    for n in nbr:
        if n > maxi:
            maxi = n
    return maxi


def max2_2(number_list: list) -> int:
    """
    version avec list
    Écrivez  une  fonction  qui  demande  plusieurs  paramètres  entiers,  puis  qui  renvoie le
    nombre maximum
    """
    maxi = -math.inf
    for n in number_list:
        if n > maxi:
            maxi = n
    return maxi


def fizzbuzz(nbr: int) -> str | int:
    """
    Écrivez une fonction nommée fizzbuzz prenant un nombre en paramètre. Cette fonction
    renverra :
    • FIZZ si le nombre est divisible par 3 ;
    • BUZZ si le nombre est divisible par 5 ;
    • FIZZBUZZ si le nombre est divisible par 3 et par 5 ;
    • Dans les autres cas, la fonction renverra le nombre passé en paramètre
    """
    if nbr % 3 == 0:
        if nbr % 5 == 0:
            return "FIZZBUZZ"
        return "FIZZ"
    if nbr % 5 == 0:
        return "BUZZ"
    return nbr


def permis(spd: int) -> str:
    """
    Écrivez une fonction qui vérifie une vitesse.
    1. Si la vitesse est inférieure à 70km/h, elle renverra OK ;
    2. Sinon, pour chaque tranche de 5km/h au-dessus de la limite, le conducteur perd 1 point
    sur son permis. La fonction renverra le nombre de points perdus ;
    3. Au-delà de 12 points perdus, la fonction renverra Permis suspendu.
    """
    if spd < 70:
        return "OK"
    pts = (spd - 70) // 5
    return f" vous avez perdu {pts} points {', permis suspendu' if pts > 12 else ''}"
