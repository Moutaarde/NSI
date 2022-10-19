# Créé par moutarde, le 07/10/2022 en Python 3.7
def prix(nb_adultes,nb_enfants):
    resultat=37*nb_adultes+28*nb_enfants
    return resultat
adultes=int(input("Entrer le nb d'adultes"))
enfants=int(input("Entrer le nb d'enfants"))
a_payer=prix(adultes,enfants)
print("Le prix a payer est :",a_payer)
