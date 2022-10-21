# Créé par moutarde, le 21/10/2022 en Python 3.7
from PIL import Image
largeur=600
hauteur=300
img =Image.new('RGB', (largeur,hauteur))
for y in range(hauteur):
    for x in range(400,600):
        img.putpixel((x,y),(255,0,0))
    for x in range(200,400):
        img.putpixel((x,y),(255,255,255))
    for x in range(0,200):
        img.putpixel((x,y),(0,0,255))

img.save("Z:/home/moutarde/NSI/Projet.sur.les.images/test.png", "PNG")
