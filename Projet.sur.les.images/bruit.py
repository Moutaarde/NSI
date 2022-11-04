# Créé par moutarde, le 21/10/2022 en Python 3.7
from PIL import Image
from random import randrange
img = Image.open("C:\\Users\\gouba\\Documents\\NSI\\Projet.sur.les.images\\flower.jpg")
largeur,hauteur=img.size
for y in range(hauteur):
    for x in range(largeur):
        u=randrange(-100,100)
        z=randrange(-100,100)
        l=randrange(-100,100)
        r,v,b=img.getpixel((x,y))
        img.putpixel((x,y),(r+u,v+z,b+l))
img.show()

