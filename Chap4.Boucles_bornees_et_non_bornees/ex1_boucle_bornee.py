# Créé par moutarde, le 02/10/2022 en Python 3.7
somme=0
for i in range(4):
    nb=float(input("Entrez le nombre"))
    somme=somme+nb
moyenne=somme/(i+1)
print(moyenne)