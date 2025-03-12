"""
Les exos du chap 10
__author__ = Gvanderveen
__version__ = 0.1
"""
import math


def max1(a, b):
    """
    Écrivez une fonction qui demande deux paramètres entiers, puis qui renvoie le nombre
    maximum
    """
    if a > b:
        return a
    return b


def max2(*nbr):
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

def max2(number_list):
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