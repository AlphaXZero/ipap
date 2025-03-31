"""
Concevez le jeu du démineur en version console. Le but du jeu est de détecter des mines
placées aléatoirement dans un champ de mines en y posant un drapeau. Concevez ce
projet en TDD avec Pytest. Vous pouvez utiliser des bibliothèques tierce (comme tabulate
et colorama) pour l’interface graphique.
Faites en sorte de ne pas tomber sur une mine dès la première case
__author__ = Gvanderveen
__version__ = 0.1
"""

from tabulate import tabulate


def init_board(size: int) -> list:
    """
    Take a size argument and create a sizeXsize matrix
    """
    return [[0 for _ in range(size)] for _ in range(size)]


def show_board(board: list) -> None:
    """
    Print the board
    """
    print(tabulate(board, tablefmt="grid"))


show_board(init_board(5))
