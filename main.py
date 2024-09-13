"""
importe la fonction racine carrée
"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    Cherche si le nombre donné est un entier
    args: 
        p: entier supposé premier
    returns:
        True ou False
    """
    if p in (0,1):  #cas isolés de 0 et 1
        return False
    r=int(sqrt(p))
    for i in range(2,r+1):  # on va jusqu'a la racine plutot que le nb, c'est plus rapide
    #for i in range(2,p):
        if p%i==0:
            return False
    return True
#### Fonction principale


def main():
    """
    s execute lors de l'execution de ce fichier

    args: None

    reuturns: rien, affiche les nb premiers trouvés

    """
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
