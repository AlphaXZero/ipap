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
    



if __name__ == "__main__":
    syracuse(14)    
