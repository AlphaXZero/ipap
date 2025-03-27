"""
Modifiez le jeu des allumettes pour lui ajouter les fonctionnalités suivantes :
• Le jeu peut maintenant être joué seul contre l’ordinateur ou à deux joueurs. Le joueur
indiquera le mode de jeu (seul/ deux joueurs).
• En cas de jeu contre l’ordinateur, programmez une intelligence artificielle qui choisira au
hasard une à trois allumettes lors de son tour de jeu
__author__ = Gvanderveen
__version__ = 0.1
"""

from random import randint


def print_game(nbr: int) -> str:
    """
    print the game
    """
    print("I " * nbr)


def ask_name(p_setting: int) -> list:
    """
    ask players name for the game and return a list of the them
    """
    if p_setting == 0:
        return [input("Joueur1, entre ton nom : "), input("Joueur2, entre ton nom : ")]
    else:
        return [input("Entre ton nom : "), "Ordinateur"]


def game_settings() -> int:
    """
    ask the player if he wants to play againt an ia (func return 0) or a human (func return 1)
    """
    while True:
        p_choice = input("Souhaite tu jouer contre un robot (1) ou un humain (2) ? ")
        if p_choice in ("1", "robot", "ia"):
            return 1
        elif p_choice in ("2", "humain", "joueur"):
            return 0
        else:
            print("Entrée incorrecte, réssaye")


def check_answer(answer: str) -> bool:
    """
    return True if the answer given by the player is a correct int value else false
    """
    return answer.isdigit() and int(answer) in (1, 2, 3)


def game_turn_human(fc_amount: int, p_name: list, p_turn: int, p_setting: int) -> int:
    """
    ask the player the amount of firecrackers he wants to take then returns it
    """
    while True:
        if p_setting == 1 and p_turn == 1:
            player_choice = randint(1, 3)
            print(f"Tour de l'ordinateur : {player_choice}")
            break
        else:
            player_choice = input(
                f"Tour de {p_name[p_turn]}, combien d'allumettes tu retires ? 1, 2 ou 3 ? "
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
    p_setting = game_settings()
    p_name = ask_name(p_setting)
    p_turn = randint(0, 1)
    while fc_amount > 0:
        print_game(fc_amount)
        fc_amount -= game_turn_human(fc_amount, p_name, p_turn, p_setting)
        p_turn = (p_turn + 1) % 2
    print(f"<><> Partie finie, {p_name[p_turn]} a gagné <><>")


if __name__ == "__main__":
    main()
