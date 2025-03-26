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


def ask_name() -> list:
    """
    ask name for the game
    """
    return [input("Joueur1, entre ton nom : "), input("Joueur2, entre ton nom : ")]


def check_answer(answer: str) -> bool:
    """
    check if the answer given by the player is a correct int value
    """
    return answer.isdigit() and int(answer) in (1, 2, 3)


def main():
    """
    main function for firecrackers game
    """
    fc_amount = 20
    p_name = ask_name()
    i = randint(0, 1)
    while fc_amount > 0:
        print_game(fc_amount)
        is_typing = True
        while is_typing:
            player_choice = input(
                f"Tour de {p_name[i % 2]} choisis le nombre d'allumettes (1,2 ou 3) à retirer :"
            )
            if check_answer(player_choice):
                fc_amount -= int(player_choice)
                is_typing = False
            else:
                print("Entrée incorrecte, réessaye")
        print("-------------------------------")
        i += 1
    print(f"<><> Partie finie, {p_name[i % 2]} a gagné <><>")


if __name__ == "__main__":
    main()
