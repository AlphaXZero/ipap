"""
Les exos du chap 12
__author__ = Gvanderveen
__version__ = 0.1
"""

from random import randrange, uniform

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


def advanced_coding():
    """
    Une technique ultérieure de cryptographie consiste à opérer non avec un décalage systé-
    matique, mais par une substitution aléatoire. Pour cela, on utilise un alphabet-clé dans
    lequel les lettres se succèdent de façon désordonnée. Par exemple:
    C’est cette clé qui va servir ensuite à coder le message.
    Écrivez un algorithme qui effectue ce cryptage. L’utilisateur entrera son alphabet-clé (on
    suppose qu’il le fera sans erreurs), puis une phrase à coder. L’algorithme affichera la phrase
    codée.
    """
    usr_in = list(input("Entrez la phrase à coder : ").lower())
    ALPHAC = input("Entrez la phrase-clé : ")
    for i in range(len(usr_in)):
        if usr_in[i] in ALPHAC:
            usr_in[i] = ALPHAC[(ALPHAC.index(usr_in[i]) + 1) % len(ALPHAC)]
    print("".join(usr_in))


def vigner_coding():
    """
    Le chiffre de Vigenère est beaucoup plus difficile à briser que les précédents. Il consiste
    en une combinaison de différents chiffres de César.
    On peut en effet écrire 25 alphabets décalés par rapport à l’alphabet normal:
    • l’alphabet qui commence par b et finit par yza;
    • l’alphabet qui commence par c et finit par zab;
    • etc.
    Le codage va s’effectuer sur le principe du code de César: on remplace la lettre d’origine
    par la lettre occupant la même place dans l’alphabet décalé. Mais à la différence du chiffre
    de César, un même message va utiliser non un, mais plusieurs alphabets décalés. Pour
    savoir quels alphabets seront utilisés, et dans quel ordre, on utilise une clé.
    Par exemple, si on prend la clé VIGENERE, et la phrase à coder Il faut coder cette phrase,
    nous procéderons comme suit:
    • La première lettre (I) sera codée en utilisant l’alphabet commençant par V. La neuvième
    lettre de cet alphabet est le D.
    • La seconde lettre (l) sera codée avec l’alphabet commençant par I. «L» étant la 12eme
    lettre de l’alphabet normal, elle deviendra un t dans l’alphabet décalé.
    • etc.
    Écrivez l’algorithme qui effectue un cryptage de Vigenère, en demandant bien sûr au départ
    la clé à l’utilisateur
    """
    usr_in = list(input("Entrez la phrase à coder : ").lower())
    KEY = input("Entrez la phrase-clé : ")
    for i in range(len(usr_in)):
        if usr_in[i] in ALPHAB2:
            usr_in[i] = ALPHAB2[
                (ALPHAB2.index(KEY[i]) + ALPHAB2.index(usr_in[i])) % len(ALPHAB2)
            ]
    print("".join(usr_in))


def odd_or_even():
    """
    Écrivez un algorithme qui demande un nombre à l’utilisateur. L’ordinateur affiche ensuite
    si ce nombre est pair ou impair
    """
    usr_in = int(input("Entrez un nombre : "))
    print(f"Le nombre est {'pair' if usr_in % 2 == 0 else 'impair'}")


def schpountz_number(type: int) -> int:
    """
    Écrivez différents algorithmes qui génèrent un nombre Schpountz aléatoire tel que:
    • 0 =< 𝑆𝑐ℎ𝑝𝑜𝑢𝑛𝑡𝑧 < 2
    • −1 =< 𝑆𝑐ℎ𝑝𝑜𝑢𝑛𝑡𝑧 < 1
    • 1,35 ≤ 𝑆𝑐ℎ𝑝𝑜𝑢𝑛𝑡𝑧 < 1,65
    • Schpountz simule un dé à six faces.
    • −10,5 ≤ 𝑆𝑐ℎ𝑝𝑜𝑢𝑛𝑡𝑧 < +6,5
    • Schpountz simule la somme d’un jet de deux dés à 6 faces.
    """
    match type:
        case 1:
            return randrange(0, 2)
        case 2:
            return randrange(-1, 1)
        case 3:
            return uniform(1.35, 1.65)
        case 4:
            return randrange(1, 7)
        case 5:
            return uniform(-10.5, 6.55)
        case 6:
            return (randrange(1, 7), randrange(1, 7))


if __name__ == "__main__":
    print(schpountz_number(6))
