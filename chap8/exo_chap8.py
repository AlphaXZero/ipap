"""
exercises from chapter 8
__author__ = Gvanderveen
__version__ = 0.1
"""

import random
import math


def twoD_init() -> list:
    """
    Écrivez un algorithme remplissant un tableau de 6x13 cases, avec des 0
    """
    return [[0 for i in range(6)] for y in range(13)]


def twoD_max(inp: list) -> int:
    """
    Iterate through a 2D list and return its maximum value
    """
    maxi = -math.inf
    for line in inp:
        if max(line) > maxi:
            maxi = max(line)
    return maxi


def print_board(board : list) -> None:
    """
    prints the board
    """
    for i in board:
        print(" ".join(i))


def one_move_checkers():
    """
    Écrivez un algorithme de jeu de dames très simplifié.
    L’ordinateur demande à l’utilisateur dans quelle case se trouve son pion (ligne, colonne).
    On met en place un contrôle de saisie afin de vérifier la validité des valeurs entrées.
    Ensuite, on demande à l’utilisateur quel mouvement il veut effectuer: 7 (en haut à gauche),
    9 (en haut à droite), 1 (en bas à gauche), 3 (en bas à droite).
    Si le mouvement est impossible (on sort du damier), on le signale à l’utilisateur et on
    s’arrête là. Sinon, on déplace le pion et on affiche le damier résultant, en affichant un O
    pour une case vide et un X pour la case où se trouve le pion
    """
    board = [["O" for i in range(10)] for j in range(10)]
    board_y = int(input("Entrez la colonne de votre pion")) - 1
    board_x = int(input("Entrez la ligne de votre pion")) - 1

    board[board_y][board_x] = "X"
    print_board(board)

    move_choice = int(
        input(
            "Comment souhaitez vous vous déplacer ? 7 (en haut à gauche), 9 (en haut à droite), 1 (en bas à gauche), 3 (en bas à droite) : "
        )
    )


    flag = False
    match move_choice:
        case 7:
            if 0 <=board_y - 1 < 10 and 0 <= board_x - 1 < 10:
                board[board_y - 1][board_x - 1] = "X"
            else:
                flag = True

        case 9:
            if board_y - 1 < 10 and board_x + 1 < 10:
                board[board_y - 1][board_x + 1] = "X"
            else:
                flag = True
        case 1:
            if board_y + 1 < 10 and board_x - 1 < 10:
                board[board_y + 1][board_x - 1] = "X"
            else:
                flag = True
        case 3:
            if board_y + 1 < 10 and board_x + 1 < 10:
                board[board_y + 1][board_x + 1] = "X"
            else:
                flag = True

    if flag:
        print("impossible")
    else:
        board[board_y][board_x] = "O"
        print_board(board)

if __name__ == "__main__":
    """main func"""
    # tab = [[random.randint(0,400) for i in range(12)] for j in range(8)]
    # print(twoD_max(tab))
    one_move_checkers()
