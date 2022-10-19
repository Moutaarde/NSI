# Créé par moutarde, le 13/09/2022 en Python 3.7
a=int(input("Entrez le bit de poids faible"))
b=int(input("Entrez le bit suivant"))
c=int(input("Entrez le bit suivant"))
d=int(input("Entrez le bit de poids fort"))
if a==1:
    e=1
else:
    e=0
if b==1:
    e=e+2
if c==1:
    e=e+4
if d==1:
    e=e+8
print("Ce nombre en base 10 est :",e)