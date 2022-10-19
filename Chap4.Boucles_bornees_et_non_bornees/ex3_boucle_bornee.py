# Créé par moutarde, le 04/10/2022 en Python 3.7
solutions=0
for nbfemmes in range(26):
    for nbhommes in range(11):
        if(10*nbhommes+4*nbfemmes)==100:
            print("Nombre de femmes :",nbfemmes,"Nombre d'hommes :",nbhommes)
            solutions=solutions+1
print("Il y a",solutions,"solutions.")