# Créé par moutarde, le 11/10/2022 en Python 3.7
def reaction(vitesse):
    """reaction(vitesse) renvoie la distance de réaction
    Par exemple reaction(50.0) doit renvoyer 13.88888....
    ENTREE: type float
    SORTIE: type float"""
    return vitesse/3.6

def freinage(vitesse):
    """freinage(vitesse) renvoie la distance de freinage
    Par exemple freinage(50.0) doit renvoyer 12.5
    ENTREE: type float
    SORTIE: type float"""
    return vitesse**2/200

def arret(vitesse):
    """arret(vitesse) renvoie la distance totale d'arrêt
    Par exemple arret(50.0) doit renvoyer 26.388888....
    ENTREE: type float
    SORTIE: type float"""
    r=reaction(V)
    f=freinage(V)
    return r+f

#Programme principal
V=float(input("Quelle est votre vitesse en km/h ?"))
reac=reaction(V)
frein=freinage(V)
arr=arret(V)
print("Vitesse=",V,"km/h")
print("distance de réaction=",reac,"m")
print("distance de freinage=",frein,"m")
print("distance d'arrêt=", arr,"m")
