# Créé par moutarde, le 11/10/2022 en Python 3.7
def calcul(x):
    """calcul(x) renvoie la valeur de la fonction 2x²+x+3 selon x
    ENTREE: x est un nombre (type float)
    SORTIE: un nombre (type float)"""
    resultat=2*x**2+x+3
    return resultat
assert calcul(0)==3
assert calcul(1)==6
print("fini")