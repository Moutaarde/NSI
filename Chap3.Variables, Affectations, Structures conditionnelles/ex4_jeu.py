# Créé par moutarde, le 16/09/2022 en Python 3.7
pv=float(input("Combien de points de vie as-tu ?"))
pe=float(input("Combien de points d'energie as-tu ?"))
niv=pe+pv**2
if niv>=110 :
    print("Tu as gagne !")
else :
    print("Tu as perdu...")