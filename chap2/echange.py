"""
Écrivez un algorithme permettant d’échanger les valeurs de deux variables a et b, et ce
 quel que soit le contenu préalable.
__author__ = Gvanderveen
__version__ = 0.1
"""

a = input("a ->")
b = input("b ->")
a, b = b, a
print("a ->", a, "b ->", b)
