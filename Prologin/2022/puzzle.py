from dataclasses import dataclass
from typing import List


@dataclass
class Structpiece:
    """Structure pour designer une piece"""

    ncotespiece: int  # le nombre de cotes de la pièce
    couleurpiece: str  # la couleur de la pièce


def resoudre(
    ncouleurs: int,
    couleurs: List[str],
    ncotes: int,
    couleurscotes: List[str],
    npieces: int,
    pieces: List[Structpiece],
) -> None:
    """
    :param ncouleurs: le nombre de couleurs
    :param couleurs: les différentes couleurs possibles
    :param ncotes: le nombre de côtés de la pièce manquante
    :param couleurscotes: les couleurs des pièces adjacentes à la pièce manquante
    :param npieces: le nombre de pièces à trier
    :param pieces: les pièces à trier
    """
    # TODO Affiche sur la première ligne, pour chaque pièce un caractère 'O' si
    # la pièce peut correspondre à celle recherchée, 'X' sinon. Affiche sur la
    # ligne suivante le nombre de pièces qui peuvent correspondre.
    load = ""
    count = 0
    for struct in pieces:
        if (struct.ncotespiece == ncotes and struct.couleurpiece in couleurs and struct.couleurpiece not in couleurscotes) :
            load+='O'
            count+=1

        else : 
            load+='X'
    print(load); print(count)
    


if __name__ == "__main__":
    ncouleurs = int(input())
    couleurs = [input() for _ in range(ncouleurs)]
    ncotes = int(input())
    couleurscotes = [input() for _ in range(ncotes)]
    npieces = int(input())
    pieces = [
        Structpiece(
            int(input()),
            input(),
        )
        for _ in range(npieces)
    ]
    resoudre(ncouleurs, couleurs, ncotes, couleurscotes, npieces, pieces)
