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

from keyboard import read_key
from random import randrange
from time import sleep
from colorama import init, Fore, Back, Style
from tabulate import tabulate

COLORS = {
    0: Fore.WHITE,
    2: Fore.CYAN,
    4: Fore.GREEN,
    8: Fore.YELLOW,
    16: Fore.MAGENTA,
    32: Fore.RED,
    64: Back.WHITE,
    128: Back.BLUE,
    256: Back.GREEN,
    512: Back.YELLOW,
    1024: Back.MAGENTA,
    2048: Back.RED,
}


def show_game(board):
    """
    print the board
    """
    board = tabulate(
        [[f"{COLORS[cell]}{cell}{Style.RESET_ALL}" for cell in row] for row in board],
        tablefmt="simple_grid",
    )
    print(board)


def generate_2_4(board: list) -> list:
    """
    generate 2 int values between 2 and 4 in the board
    """
    index_zeros = [
        (j, i) for j, row in enumerate(board) for i in range(len(row)) if row[i] == 0
    ]
    for _ in range(2):
        if not index_zeros:
            return board
        random_zero = index_zeros.pop(randrange(0, len(index_zeros)))
        board[random_zero[0]][random_zero[1]] = randrange(2, 5, 2)
    return board


def create_board() -> list:
    """
    create a list with random entries of 2 or 4
    """
    return generate_2_4([[0 for _ in range(4)] for _ in range(4)])


def check_input() -> int:
    """
    wait for input then return the direction as int starting frome up
    1 -> up
    2 -> right
    3 -> down
    4 -> left
    """
    print("Choisisez une direction ou x pour arrêter")
    usr_choice = read_key()
    print(usr_choice)
    if usr_choice in ("up", "z", "Z"):
        return 1
    if usr_choice in ("right", "d", "D"):
        return 2
    if usr_choice in ("down", "s", "S"):
        return 3
    if usr_choice in ("left", "q", "Q"):
        return 4
    if usr_choice == "x":
        exit()


def do_merge(board: list, direction: int, vertical=0) -> list:
    """
    merge all the adjacent number in the desired direction
    """
    if direction in (2, 4):
        board = [list(filter(lambda x: x != 0, row)) for row in board]
        board = [i[::-1] for i in board] if direction == 2 else board
        for row in board:
            for j in range(len(row) - 1):
                if row[j + 1] == row[j]:
                    row[j] *= 2
                    row[j + 1] = 0
        board = [i[::-1] for i in board] if direction == 2 else board
        return (
            rotate_board(add_zeros(board, direction))
            if vertical
            else add_zeros(board, direction)
        )
    if direction == 1:
        return do_merge(rotate_board(board), 4, 1)
    return do_merge(rotate_board(board), 2, 1)


def rotate_board(board: list) -> list:
    """
    invert vertical and horizontal lines
    """
    return [list(row) for row in zip(*board)]


def add_zeros(board: list, direction: int, vertical=0) -> list:
    """
    complete a row with zeros needed in the right direction
    """
    clrd_board = []
    board = [list(filter(lambda x: x != 0, row)) for row in board]
    for row in board:
        zero_list = [0] * (4 - len(row))
        clrd_board.append(zero_list + row if direction == 2 else row + zero_list)
    return clrd_board


def is_lost(board: list) -> bool:
    """
    Return True if the game is lost (no available move) else False
    """
    board_cp = [i for i in board]
    for i in range(1, 5):
        board = do_merge(board, i)
        if board != board_cp:
            return False
    return True


def main() -> None:
    """
    main function of the game
    """
    init()
    board = create_board()
    show_game(board)
    while 2048 not in board:
        if is_lost(board):
            print("Partie Perdu, aucun mouvement possible")
            break
        usr_in = check_input()
        board = generate_2_4(do_merge(board, usr_in))
        show_game(board)
        sleep(0.4)
    if 2048 in board:
        print("VOUS AVEZ GAGNE")


if __name__ == "__main__":
    main()
