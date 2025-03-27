"""
Le jeu des allumettes se joue à deux joueurs. Le principe est simple : 20 allumettes sont
alignées. Chaque joueur a le droit de tirer 1, 2 ou 3 allumettes à la fois. Celui qui tire la
dernière allumette a perdu.
Programmez le jeu des allumettes. Le jeu doit répondre aux critères suivants :
• Le jeu doit être jouable à deux joueurs humains. Il demandera le nom des deux joueurs.
• Le jeu choisira au hasard un des deux joueurs.
• Le jeu doit afficher le nombre d’allumettes restantes (au début, 20) :
ΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙΙ• Le jeu doit vérifier que le joueur ne tire qu’une à trois allumettes.
• Le jeu s’arrête quand un joueur a tiré la dernière allumette. Il affichera un message
indiquant quel joueur a perdu.
__author__ = Gvanderveen
__version__ = 0.1
"""

from random import randint


def print_game(nbr: int) -> str:
    """
    print the game
    """
    print("I " * nbr)


def ask_name() -> list:
    """
    ask players name for the game and return a list of the them
    """
    return [input("Joueur1, entre ton nom : "), input("Joueur2, entre ton nom : ")]


def check_answer(answer: str) -> bool:
    """
    return True if the answer given by the player is a correct int value else false
    """
    return answer.isdigit() and int(answer) in (1, 2, 3)


def game_turn(fc_amount: int, p_name: list, p_turn: int) -> int:
    """
    ask the player the amount of firecrackers he wants to take then returns it
    """
    while True:
        player_choice = input(
            f"Tour de {p_name[p_turn]}, combien d'allumettes tu retires ? de 1, 2 ou 3 ? :"
        )
        if check_answer(player_choice):
            break
        else:
            print("Entrée incorrecte, réessaye")
    print("-------------------------------")
    return int(player_choice)


def main():
    """
    main function for firecrackers game
    """
    fc_amount = 20
    p_name = ask_name()
    p_turn = randint(0, 1)
    while fc_amount > 0:
        print_game(fc_amount)
        fc_amount -= game_turn(fc_amount, p_name, p_turn)
        p_turn = (p_turn + 1) % 2
    print(f"<><> Partie finie, {p_name[p_turn]} a gagné <><>")


if __name__ == "__main__":
    main()
