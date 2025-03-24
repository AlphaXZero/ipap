"""
__author__ = Gvanderveen
__version__ = 0.1
"""


def print_board(board: list) -> None:
    """
    prints the board
    """
    for i in board:
        print(" ".join(i))


def one_move_checkers():
    """
    BOUCLE
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
    board_y = int(input("Entrez la colonne de votre pion : ")) - 1
    board_x = int(input("Entrez la ligne de votre pion : ")) - 1

    board[board_y][board_x] = "X"
    print_board(board)
    while True:
        move_choice = int(
            input(
                "Comment souhaitez vous vous déplacer ? 1 (en bas à gauche), 3 (en bas à droite), 7 (en haut à gauche), 9 (en haut à droite), -1 pour arrêter: "
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
            case -1:
                break
            case _:
                print("Entrez un déplacement valide 1/3/7/9/-1")

        if flag:
            print("impossible, bord du terrain, choisir une autre destination : ")
        board[board_y][board_x] = "X"
        print_board(board)


one_move_checkers()
