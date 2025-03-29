"""
Modifiez  l’intelligence  artificielle  de  telle  sorte  qu’elle  ne  tire  plus  des  allumettes  au
hasard, mais tente d’empêcher le joueur de gagner. On pourra aussi jouer avec un nombre
quelconque d’allumettes (entre 20 et 100)
__author__ = Gvanderveen
__version__ = 0.1
"""

from random import randint

last_choice = 0


def print_game(nbr: int) -> str:
    """
    print the game
    """
    print(f"{'I ' * nbr} ({nbr})")


def ask_name(p_setting: int) -> list:
    """
    ask players name for the game and return a list of the them
    """
    if p_setting == 0:
        return [input("Joueur1, entre ton nom : "), input("Joueur2, entre ton nom : ")]
    else:
        return [input("Entre ton nom : "), "Ordinateur"]


def ask_game_type() -> int:
    """
    ask the player if he wants to play against an ia (func return 0) or a human (func return 1)
    """
    while True:
        p_choice = input("Souhaite tu jouer contre un robot (1) ou un humain (2) ? ")
        if p_choice in ("1", "robot", "ia"):
            return ask_difficulty()
        elif p_choice in ("2", "humain", "joueur"):
            return 0
        else:
            print("Entrée incorrecte, réssaye")


def ask_difficulty() -> int:
    """
    ask the player if he want easy mode (1), medium (2) or hard(3)
    """
    while True:
        p_choice = input(
            "Quelle niveau de difficulté ? facile (1), moyen (2) ou difficile (3) ? "
        )
        if p_choice in ("1", "facile"):
            return 1
        elif p_choice in ("2", "moyen"):
            return 2
        elif p_choice in ("3", "difficile"):
            return 3
        else:
            print("Entrée incorrecte, réssaye")


def ask_fc_amount() -> int:
    """
    ask the player the amont of firecrackers he wants to play with
    """
    while True:
        p_choice = input("Avec Combien d'allumettes allez vous jouer ? (de 20 à 100)")
        if p_choice.isdigit() and 20 <= int(p_choice) <= 100:
            return int(p_choice)
        else:
            print("Entrée incorrecte, réssaye")


def game_settings() -> tuple:
    """
    ask the player for the differents settings he wants to play
    """
    return ask_fc_amount(), ask_game_type()


def check_best_move(fc_amount: int) -> int:
    """
    compute the best move
    """
    # d'après mes recherches si un joueur tombe sur un multiple de 4 + 1 il a perdu car
    # l'autre n'a qu'a faire en sorte de toujours compléter pour que ça fasse 4
    # exemple
    # s'il reste 21 à l'ennemi et qu'il en retire 2, j'en retire 2, il en reste 16
    # il en retire 3, j'en retire 1, ect

    if last_choice == 0:
        if fc_amount % 4 == 1:
            return randint(1, 3)
        return (fc_amount % 4) - 1
    if (last_choice + fc_amount) % 4 == 1:
        return 4 - last_choice
    if fc_amount % 4 == 1:
        return randint(1, 3)
    return (fc_amount % 4) - 1


def game_turn(fc_amount: int, p_name: list, p_turn: int, p_setting: int) -> int:
    """
    ask the player the amount of firecrackers he wants to take then returns it
    """
    global last_choice
    while True:
        if p_setting >= 1 and p_turn == 1:
            if p_setting == 1:
                player_choice = randint(1, 3)
            elif p_setting == 2 and fc_amount > 4:
                player_choice = (
                    check_best_move(fc_amount),
                    randint(1, 3),
                    randint(1, 3),
                )[randint(0, 2)]
            else:
                player_choice = check_best_move(fc_amount)
            print(f"Tour de l'ordinateur : {player_choice}")
            break
        else:
            player_choice = input(
                f"Tour de {p_name[p_turn]}, combien d'allumettes tu retires ? 1, 2 ou 3 ? "
            )
            if player_choice.isdigit() and int(player_choice) in (1, 2, 3):
                last_choice = int(player_choice)
                break
            else:
                print("Entrée incorrecte, réessaye")
    print("-------------------------------")
    return int(player_choice)


def main():
    """
    main function for firecrackers game
    """
    fc_amount, p_setting = game_settings()
    p_name = ask_name(p_setting)
    p_turn = randint(0, 1)
    while fc_amount > 0:
        print_game(fc_amount)
        fc_amount -= game_turn(fc_amount, p_name, p_turn, p_setting)
        p_turn = (p_turn + 1) % 2
    print(f"<><> Partie finie, {p_name[p_turn]} a gagné <><>")


if __name__ == "__main__":
    main()
