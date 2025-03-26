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


def max1_2(a: int, b: int) -> int:
    """
    version opti
    Écrivez une fonction qui demande deux paramètres entiers, puis qui renvoie le nombre
    maximum
    """
    return max(a, b)


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


def max2_3(*nbr: int) -> int:
    """
    version avec args et opti
    Écrivez  une  fonction  qui  demande  plusieurs  paramètres  entiers,  puis  qui  renvoie le
    nombre maximum
    """
    return max(nbr)


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


def separate(nbr_list: list) -> list:
    """
    Écrivez une fonction qui sépare les 0 et les 1 d’une liste, en mettant les 0 en début et les
    1 en fin de liste. Ex: separate([0,1,0,1,1,1,0]) >>> [0,0,0,1,1,1,1]
    """
    nbr0 = 0
    nbr1 = 0
    for i in range(len(nbr_list)):
        if nbr_list[i] == 0:
            nbr0 += 1
        elif nbr_list[i] == 1:
            nbr1 += 1
    return [0] * nbr0 + [1] * nbr1


def separate_opti(nbr_list: list) -> list:
    """
    version + compacte
    Écrivez une fonction qui sépare les 0 et les 1 d’une liste, en mettant les 0 en début et les
    1 en fin de liste. Ex: separate([0,1,0,1,1,1,0]) >>> [0,0,0,1,1,1,1]
    """
    return [0] * nbr_list.count(0) + [1] * nbr_list.count(1)


def sumcode(nbr: int) -> int:
    """
    Écrivez une fonction qui prend en paramètre un nombre strictement supérieur à 100
    et qui permet ensuite de déterminer un code à partir de ce nombre, selon les étapes
    suivantes :
    • Faire la somme des chiffres du nombre passé en paramètre.
    • Recommencer l’opération tant que le code est supérieur à 9.
    Ex : sumcode(69810) >>> 669810
    """
    if nbr <= 100:
        print("Réessayez avec un nombre strictement supérieur à 100")
    code = nbr
    while code > 9:
        code = sum([int(i) for i in str(code)])
    return int(str(code) + str(nbr))


def dist_nbr(nbr: int) -> bool:
    """
    Écrivez une fonction qui prend en paramètre un nombre entier et qui indique par True ou
    False si tous les chiffres sont différents
    """
    nbr_to_list = sorted([i for i in str(nbr)])
    for i in range(0, len(nbr_to_list) - 1):
        if nbr_to_list[i] == nbr_to_list[i + 1]:
            return False
    return True


def is_palindrome(nbr: int) -> bool:
    """
    Écrivez une fonction qui prend un nombre en paramètre et qui indique par True ou False
    si le nombre est palindrome ou non.
    Un nombre est un nombre palindrome s’il donne la même valeur en étant lu de gauche à
    droite et de droite à gauche.
    """
    return str(nbr) == str(nbr)[::-1]


def nombres_palindromes_2() -> str:
    """
    Le plus grand nombre palindrome obtenu comme produit de deux entiers à deux chiffres
    est 9009 = 91 × 99.
    Écrivez un programme qui permet de trouver le plus grand nombre palindrome obtenu
    comme produit de deux entiers à trois chiffres.
    """
    maxi = -math.inf
    for i in range(100, 1000):
        for j in range(100, 1000):
            if is_palindrome(i * j) and i * j > maxi:
                maxi = i * j
                ind = i, j
    print(
        f"Le plus grand nombre palindrome obtenable avec 2 entiers à 3 chiffres est {maxi} obtenu à partir de {ind[0]} et {ind[1]}"
    )


def is_prime(nbr: int) -> bool:
    """
    return True if the int input is prime else False
    """
    if (nbr % 2 == 0 or nbr % 3 == 0 or nbr % 5 == 0 or nbr % 7 == 0) and nbr not in [
        1,
        2,
        3,
        5,
        7,
    ]:
        return False
    return True


def nombres_circulaires_premiers(nbr: int) -> bool:
    """
    Écrivez une fonction qui prend en paramètre un nombre entier et qui teste si le nombre
    est circulaire premier. Un nombre est circulaire premier si la rotation de ses chiffres
    sont également des nombres premiers. Ex : 71 est circulaire premier, car 17 est premier et
    71 l’est aussi.
    """
    if is_prime(nbr) and is_prime(int(str(nbr)[-1::-1])):
        return True
    return False


if __name__ == "__main__":
    print(is_palindrome(30103))
