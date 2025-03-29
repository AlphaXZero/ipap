"""
Écrivez le jeu du 2048 en version console. Le but du jeu est d’afficher un tableau de
4x4 cases avec des tuiles de couleur. Chaque tuile possède une valeur numérique entre
2 et 2048 (toujours une puissance de deux). En appuyant sur une des flèches du clavier,
on va pousser toutes les tuiles dans la direction indiquée. Si deux tuiles identiques se
collisionnent  lors  de  la  compression,  elles  fusionnent  en  une  tuile  de  rang  supérieur.
Après la compression, deux nouvelles tuiles apparaissent. Ces tuiles portent aléatoirement
les numéros 2 ou 4.
Le but est d’atteindre la tuile 2048.
Analysez le problème pour en déduire les fonctions à écrire
__author__ = Gvanderveen
__version__ = 0.1
"""

from keyboard import is_pressed
from random import randrange


def show_game(board: list) -> None:
    """ """
    print("\n---------------")
    for i in board:
        for j in range(len(i)):
            print(f"|{i[j]}| ", end="")
        print("\n---------------")


def create_game() -> list:
    """
    create a list with random entries of 2 or 4
    """
    return [[randrange(2, 5, 2) for _ in range(4)] for _ in range(4)]


def check_input() -> int:
    """
    wait for input then return the direction as int starting frome up
    1 -> up
    2 -> right
    3 -> down
    4 -> left
    """
    print("Choisisez une direction")
    while True:
        if is_pressed("up") or is_pressed("z"):
            return 1
        if is_pressed("right") or is_pressed("d"):
            return 2
        if is_pressed("left") or is_pressed("q"):
            return 4
        if is_pressed("down") or is_pressed("s"):
            return 3


def do_merge(board: list, direction: int) -> list:
    """
    merge all the adjacent number in the desired direction
    """
    # TODO : une fonction de plus pour enlever répétion ?
    board = [i[::-1] for i in board] if direction == 2 else board
    if direction in (2, 4):
        for i in range(len(board)):
            for j in range(len(board) - 1):
                if board[i][j + 1] == board[i][j]:
                    board[i][j] *= 2
                    board[i][j + 1] = 0
        return board if direction == 4 else [i[::-1] for i in board]
    print(board)
    show_game(cleanse_zero(board, direction))


def rotate_board(board: list) -> list:
    """
    invert vertical and horizontal lines
    """
    return [list(row) for row in zip(*board)]


def cleanse_zero(board: list, direction: int, vertical=0) -> list:
    """
    remove the 0 if they are betwen two int
    then isolate them in the desired direction
    []
    """
    clrd_board = []
    if direction in (2, 4):
        for row in board:
            zero_list, int_list = [0] * row.count(0), [j for j in row if j != 0]
            clrd_board.append(
                zero_list + int_list if direction == 2 else int_list + zero_list
            )
    else:
        if direction == 1:
            return cleanse_zero(rotate_board(board), 4, 1)
        return cleanse_zero(rotate_board(board), 2, 1)

    return clrd_board if vertical == 0 else rotate_board(clrd_board)


def main() -> None:
    """
    main function of the game
    """


if __name__ == "__main__":
    oui = create_game()
    show_game(oui)
    show_game(cleanse_zero(do_merge(oui, 4), 4))
    show_game(cleanse_zero(do_merge(oui, 2), 2))
