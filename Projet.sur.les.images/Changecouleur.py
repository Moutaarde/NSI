# Créé par moutarde, le 21/10/2022 en Python 3.7
from PIL import Image
from random import randrange
img = Image.open("Z:/home/moutarde/NSI/Projet.sur.les.images/flower.jpg")
largeur,hauteur=img.size
for y in range(hauteur):
    for x in range(largeur):
        r,v,b=img.getpixel((x,y))
        u=randrange(0,100)
        r=randrange(0,100)
        l=randrange(0,100)
        img.putpixel((x,y),(r+u,v+r,b+l))
img.save("Z:/home/moutarde/NSI/Projet.sur.les.images/flower2.jpg")

