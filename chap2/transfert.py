"""
Écrivez un algorithme permettant de transférer les valeurs de trois variables a, b et c. Il
 faut transférer a dans b, b dans c et c dans a, quels que soient les contenus préalables
 de ces variables.
__author__ = Gvanderveen
__version__ = 0.1
"""

a = input("a ->")
b = input("b ->")
c = input("c ->")
a, b, c = c, a, b

print("a ->", a, "b ->", b, "c ->", c)
