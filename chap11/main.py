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


def syracuse(nbr):
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


def fibonnaci(n, nbr=0, nbr_av=1):
    """
    Écrivez une fonction récursive qui calcule le nème élément de la suite de Fibonacci. En
    mathématiques, la suite de Fibonacci est une suite de nombres entiers dont chaque terme
    successif est la somme des deux termes précédents, et qui commence par 0 et 1.
    Par exemple, les dix premiers nombres de la suite sont : 0,1,1,2,3,5,8,13,21,34
    """
    print(nbr)
    if n > 1:
        return fibonnaci(n - 1, nbr=(nbr + nbr_av), nbr_av=nbr)


if __name__ == "__main__":
    print(fibonnaci(10))
