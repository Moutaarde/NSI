# Créé par moutarde, le 02/10/2022 en Python 3.7
nbjourstotal=int(input("Entrez le nombre total de jours de la randonnée"))
distanceparjour=30
for jours in range(nbjourstotal):
    distanceparjour=(distanceparjour/100)*95
    print(distanceparjour)
print(distanceparjour)