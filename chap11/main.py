
def somme(nbr: int) -> int:
    """
    Écrivez  une  fonction  récursive  qui  renvoie  la  somme  des  nombres  entiers  jusqu’à  un
    nombre préalablement entré. Exemple avec le nombre 5 : 1 + 2 + 3 + 4 + 5 = 15
    """
    if nbr==0:
        return 0
    return nbr + somme(nbr-1)





if __name__ == "__main__":
    print(somme(5))
