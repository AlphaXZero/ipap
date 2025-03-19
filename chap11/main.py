"""
Les exos du chap 11
__author__ = Gvanderveen
__version__ = 0.1
"""


def somme(nbr: int) -> int:
    """
    Écrivez  une  fonction  récursive  qui  renvoie  la  somme  des  nombres  entiers  jusqu’à  un
    nombre préalablement entré. Exemple avec le nombre 5 : 1 + 2 + 3 + 4 + 5 = 15
    """
    if nbr == 0:
        return 0
    return nbr + somme(nbr - 1)


def syracuse(nbr: int) -> int:
    """
    Écrivez une fonction récursive qui affiche les éléments de la conjecture de Syracuse. Pour
    rappel, la conjecture de Syracuse est une suite d’entiers naturels définie de la manière
    suivante :
    • on part d’un nombre entier plus grand que 0 ;
    • si ce nombre est pair, on le divise par deux ;
    • si ce nombre est impair, on le multiplie par 3 et on ajoute 1 ;
    • on répète l’opération jusqu’à ce que l’on obtienne la valeur 1
    """
    print(nbr)
    if nbr == 1:
        return 1
    elif nbr % 2 == 0:
        return syracuse(nbr // 2)
    else:
        return syracuse((nbr * 3) + 1)


def fibonnaci(n: int, nbr=0, nbr_av=1) -> None:
    """
    Écrivez une fonction récursive qui calcule le nème élément de la suite de Fibonacci. En
    mathématiques, la suite de Fibonacci est une suite de nombres entiers dont chaque terme
    successif est la somme des deux termes précédents, et qui commence par 0 et 1.
    Par exemple, les dix premiers nombres de la suite sont : 0,1,1,2,3,5,8,13,21,34
    """
    print(nbr)
    if n > 1:
        return fibonnaci(n - 1, nbr=(nbr + nbr_av), nbr_av=nbr)


def somme_digits(nbr: int, sumi=0) -> int:
    """
    Écrivez une fonction récursive qui additionne chaque chiffre d’un nombre donné. Ex :
    func(354) = 12
    """
    if nbr == 0:
        return sumi
    return somme_digits(nbr // 10, sumi + nbr % 10)


def somme_harmonique(occu: int, sumi=0) -> int:
    """
    Écrivez une fonction récursive qui affiche le nème élément de la suite harmonique. Une
    suite harmonique est la somme des éléments inverses : 1/1 + 1/2 + 1/3 + 1/4
    """
    if occu == 0:
        return sumi
    return somme_harmonique(occu - 1, sumi + 1 / occu)


def convert_b2d(nbr: int, result="b") -> int:
    """
    Écrivez une fonction récursive qui convertisse un nombre décimal en un nombre binaire.
    Ex : func(12) = b1100.
    """
    if nbr == 0:
        return result
    return convert_b2d(nbr // 2, result + ("1" if nbr % 2 == 0 else "0"))


def gcd_calculator(nbr1: int, nbr2: int, gcd=1, actu=1) -> int:
    """
    Écrivez une fonction récursive qui calcule le GCD (Grand Commun Diviseur) entre deux
    nombres.
    """
    if actu > nbr1 or actu > nbr2:
        return gcd
    return (
        gcd_calculator(nbr1, nbr2, actu, actu + 1)
        if nbr1 % actu == 0 and nbr2 % actu == 0
        else gcd_calculator(nbr1, nbr2, gcd, actu + 1)
    )


def recurse_hanoi_resolver():
    """
    Écrivez une fonction récursive qui affiche les étapes de résolution des Tours de Hanoï.
    """


def hanoi_print(repr: list) -> None:
    """
    Show hannoi
    """
    maxi = max(repr, key=len)
    for i in range(len(maxi)):
        maxi = len(max(repr, key=len))
        for y in range(3):
            if len(repr[y]) == maxi:
                print(repr[y].pop(),end="  ")
            else:
                print("   ",end="")
        print("")



def is_even(nbr):
    """
    crivez deux fonctions récursives mutuelles permettant de tester si un nombre est pair
    ou impair. Ex:
    is_even(5) >>> False 
    is_odd(7) >>> True
    """
    if nbr%2==0:
        return True
    return is_odd(nbr)

def is_odd(nbr):
    """
    crivez deux fonctions récursives mutuelles permettant de tester si un nombre est pair
    ou impair. Ex:
    is_even(5) >>> False 
    is_odd(7) >>> True
    """
    if nbr%2!=0:
        return False
    return is_even(nbr)


if __name__ == "__main__":
    jeu=[[2,4],[3],[1,5]]
    hanoi_print(jeu)
