from typing import List

all_chiffres = "0123456789"

def extract(mot):
    chiffres = ""
    minuscule = ""
    majuscule = ""

    for charactere in mot:
        if charactere in all_chiffres:
            chiffres += charactere
        
        if charactere.islower():
            minuscule += charactere
        
        if charactere.isupper():
            majuscule+=charactere

    return chiffres, minuscule, majuscule


def nb_pas_malin_drome(n: int, mots: List[str]) -> None:
    """
    :param n: Le nombre de mots de passe contenus dans le fichier de mots de passe de Raphaël
    :param mots: La liste des mots de passe à décoder
    """

    nb = 0
    for mot in mots:
        extraction = extract(mot)
        if extraction[1] == extraction[1][::-1] and extraction[2] == extraction[2][::-1] and extraction[0] == extraction[0][::-1]:
            nb+=1
    print(nb)




if __name__ == "__main__":
    n = int(input())
    mots = [input() for _ in range(n)]
    nb_pas_malin_drome(n, mots)
