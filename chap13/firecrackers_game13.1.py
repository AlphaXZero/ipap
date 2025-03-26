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
