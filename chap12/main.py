"""
Les exos du chap 12
__author__ = Gvanderveen
__version__ = 0.1
"""


def letter_count():
    """
    Écrivez un algorithme qui demande un mot à l’utilisateur et qui affiche à l’écran le nombre
    de lettres de ce mot
    """
    print(f"il y a {len(input('Entrez un mot : '))} lettres dans votre mot")


def word_count():
    """
    Écrivez un algorithme qui demande une phrase à l’utilisateur et qui affiche à l’écran le
    nombre de mots de cette phrase. On suppose que les mots ne sont séparés que par des
    espaces
    """
    usr_in = input("Entrez une phrases : ")
    print(f"il y a {len(usr_in.split())} mots dans votre phrase")


if __name__ == "__main__":
    word_count()
