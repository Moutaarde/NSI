# Créé par moutarde, le 11/10/2022 en Python 3.7
def maxi3nombres(n1,n2,n3):
    """maxi3nombres(n1,n2,n3) renvoie la valeur du plus grand des 3 nombres
    ENTREE: 3 nombres (type float)
    SORTIE: un nombre (type float)"""
    maximum=maxi(n1,n2)
    maximum=maxi(n3,maximum)
    return maximum

def maxi(nb1,nb2):
    """maxi(nb1,nb2) renvoie la valeur du plus grand des 2 nombres
    ENTREE: 2 nombres (type float)
    SORTIE: un nombre (type float)"""
    if nb1>nb2:
        return nb1
    else:
        return nb2

a=float(input("Entrer le premier nombre"))
b=float(input("Entrer le deuxieme nombre"))
c=float(input("Entrer le troisieme nombre"))
maxab=maxi(a,b)
if maxab==a:
    maxac=maxi(a,c)
    if maxac==a:
        pg=a
    else:
        pg=c
else:
    maxbc=maxi(b,c)
    if maxbc==b:
        pg=b
    else:
        pg=c
print("Le plus grand nombre est",pg)