"""
Les exos du chap 12
__author__ = Gvanderveen
__version__ = 0.1
"""

ALPHAB = "abcdefghijklmnopqrstuvwxyza  "
ALPHAB2 = "abcdefghijklmnopqrstuvwxyz"


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
    print(f"il y a {len(input('Entrez une phrase : ').split())} mots dans la phrase")


def vowels_count():
    """
    Écrivez un algorithme qui demande une phrase à l’utilisateur et qui affiche le nombre de
    voyelles contenues dans cette phrase.
    """
    print(
        f"il y a {len([i for i in input('Entrez une phrase : ') if i in 'aeiouy'])} voyelles dans la phrase"
    )


def letter_suppr():
    """
    Écrivez un algorithme qui demande une phrase à l’utilisateur. Celui-ci entrera ensuite la
    position d’un caractère à supprimer et la nouvelle phrase doit être affichée.
    """
    str_in = input("Entrez une phrase : ")
    index_in = int(input("Entrez l'indice que vous voulez supprimer : "))
    print(str_in[:index_in] + str_in[index_in + 1 :])


def str_inverter():
    """
    Écrivez un algorithme qui demande une phrase à l’utilisateur, puis qui inverse l’ordre des
    mots de la phrase.
    """
    print(
        f"Voici votre phrase retournée : {' '.join(reversed(input('Entrez une phrase : ').split()))}"
    )


def coding():
    """
    Un des plus anciens systèmes de cryptographie consiste à décaler les lettres d’un message
    pour le rendre illisible. Ainsi, les a deviennent des b, etc.
    Écrivez  un  algorithme  qui  demande  une  phrase  à  l’utilisateur  et  qui  la  code  selon  ce
    principe.
    """
    usr_in = input("Entrez votre phrase : ").lower()
    print(
        f"voici votre phrase codé : {''.join([ALPHAB[ALPHAB.index(i) + 1] for i in usr_in])}"
    )


def caesar_coding():
    """
    Une amélioration du principe précédent consiste à opérer un décalage d’un nombre quel-
    conque de lettres
    """
    usr_in = list(input("Entrez votre phrase : ").lower())
    padding_in = int(input("Entrez le décalage souhaité : "))
    for i in range(len(usr_in)):
        if usr_in[i] in ALPHAB2:
            usr_in[i] = ALPHAB2[(ALPHAB2.index(usr_in[i]) + padding_in) % len(ALPHAB2)]
    print("".join(usr_in))


if __name__ == "__main__":
    caesar_coding()
