"""
exercises from chapter 8
__author__ = Gvanderveen
__version__ = 0.1
"""


def twoD_init() -> list:
    """
    Écrivez un algorithme qui recherche la plus grande valeur au sein d’un tableau à deux
    dimensions (12x8) préalablement rempli de valeurs numériques
    """
    return [[0 for i in range(6)] for y in range(13)]


def twoD_max(list_input: list) -> int:
    """
    Iterate through a 2D list and return its maximum value
    """
    return max([max(line) for line in list_input])


def print_board_checkers(board: list) -> None:
    """
    prints the board
    """
    for i in board:
        print(" ".join(i))


def is_in_grid(x: int, y: int) -> bool:
    """
    return True if the two entry are between 0 and 9
    """
    return 0 <= x < 10 and 0 <= y < 10


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

    # je fais -1 pour que ce soit + userfriendly colonne 0 -> 1
    board_y = int(input("Entrez la colonne de votre pion: ")) - 1
    board_x = int(input("Entrez la ligne de votre pion: ")) - 1
    if not is_in_grid(board_x, board_y):
        return "Cette case n'existe pas"

    board[board_y][board_x] = "X"
    print_board_checkers(board)
    move_choice = int(
        input(
            "Comment souhaitez vous vous déplacer ? 1 (en bas à gauche), 3 (en bas à droite), 7 (en haut à gauche), 9 (en haut à droite): "
        )
    )
    board[board_y][board_x] = "O"
    flag = False
    match move_choice:
        case 7:
            if 0 <= board_y - 1 < 10 and 0 <= board_x - 1 < 10:
                board_y, board_x = board_y - 1, board_x - 1
            else:
                flag = True
        case 9:
            if 0 <= board_y - 1 < 10 and 0 <= board_x + 1 < 10:
                board_y, board_x = board_y - 1, board_x + 1
            else:
                flag = True
        case 1:
            if 0 <= board_y + 1 < 10 and 0 <= board_x - 1 < 10:
                board_y, board_x = board_y + 1, board_x - 1
            else:
                flag = True
        case 3:
            if 0 <= board_y + 1 < 10 and 0 <= board_x + 1 < 10:
                board_y, board_x = board_y + 1, board_x + 1
            else:
                flag = True
        case _:
            print("Entrez un déplacement valide 1/3/7/9")

    if flag:
        print("impossible, bord du terrain: ")
    board[board_y][board_x] = "X"
    print_board_checkers(board)


if __name__ == "__main__":
    """main func"""
    tab = twoD_init()
    print(tab)
    for i in tab:
        print(i)
    # one_move_checkers()
