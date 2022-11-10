from typing import List


alphbt = ""
Alphbt = ""
for i in range(26):
    alphbt += chr(i+97)
    Alphbt += chr(i+65)

chif = "0123456789"
speciale = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"+'"'



def isSecured(pwd):
    return len(set(alphbt).intersection(pwd)) != 0 and len(set(Alphbt).intersection(pwd)) != 0 and len(set(speciale).intersection(pwd)) !=0 and len(set(chif).intersection(pwd)) !=0



def fuite_de_clavier(n: int, k: int, chaine: List[str]) -> None:
    """
    :param n: taille de la chaîne
    :param k: taille du mot de passe
    :param chaine: la chaîne contenant le mot de passe
    """
    # TODO afficher le nombre de mots de passes possibles parmi la chaîne
    sections = [chaine[i:i+k] for i in range(len(chaine)-k+1)]
    print(sections)
    pwds = [word for word in sections if isSecured(word)]
    print(len(pwds))


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    chaine = list(input())
    fuite_de_clavier(n, k, chaine)