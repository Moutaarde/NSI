# Créé par moutarde, le 07/10/2022 en Python 3.7
def prix(nb_adultes,nb_enfants,nb_etudiants):
    """prix renvoie le prix selon le nb d'adultes, d'enfants et d'etudiants
    ENTREE: nb_adultes,nb_enfants,nb_etudiants sont des nombres (type int)
    SORTIE: un nombre positif (type int)"""
    resultat=37*nb_adultes+28*nb_enfants+30*nb_etudiants
    return resultat
adultes=int(input("Entrer le nb d'adultes"))
enfants=int(input("Entrer le nb d'enfants"))
etudiants=int(input("Entrer le nb d'etudiants"))
a_payer=prix(adultes,enfants,etudiants)
print("Le prix a payer est :",a_payer)