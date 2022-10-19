# Créé par moutarde, le 23/09/2022 en Python 3.7
from random import*
mystere=randint(1,200)
coup=1
guess=int(input("Deviner le nombre !"))
while mystere!=guess:
    if mystere<guess:
        print("C'est moins")
    if mystere>guess:
        print("C'est plus")
    guess=int(input("Deviner le nombre !"))
    coup=coup+1
print("Le nombre mystere était",mystere,"et vous avez mis",coup,"de coups pour le trouver")
