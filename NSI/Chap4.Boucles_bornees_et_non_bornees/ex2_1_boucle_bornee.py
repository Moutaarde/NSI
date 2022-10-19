# Créé par moutarde, le 02/10/2022 en Python 3.7
nbjourstotal=int(input("Entrez le nombre total de jours de la randonnée"))
distanceparjour=30
print("Il parcours",round(distanceparjour,2),"km au jour 1.")
for jours in range(nbjourstotal-1):
    distanceparjour=(distanceparjour/100)*95
    print("Il parcours",round(distanceparjour,1),"km au jour",(jours+2),".")