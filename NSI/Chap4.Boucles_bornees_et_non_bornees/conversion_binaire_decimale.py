# Créé par moutarde, le 30/09/2022 en Python 3.7
nb=int(input("nb"))
binaire="" #str vide
while nb!=0:
    reste=nb%2 #int
    c=str(reste) #converti reste en str
    nb=nb//2
    binaire=c+binaire
print(binaire)




