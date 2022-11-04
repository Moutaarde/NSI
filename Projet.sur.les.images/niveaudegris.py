from site import getuserbase
from PIL import Image
img = Image.open("C:\\Users\\gouba\\Documents\\NSI\\Projet.sur.les.images\\flower.jpg")
largeur,hauteur=img.size
for y in range(hauteur):
    for x in range(largeur):
        r,v,b=img.getpixel((x,y))
        img.putpixel((x,y),(int(r+v+b/3),int(r+v+b/3),int(r+v+b/3)))
for y in range(hauteur):
    for x in range(largeur):
        a1,a2,a3=img.getpixel((x,y))
        gbase = a1  # On calcule le gris 
        r1, v1, b1 = img.getpixel((x-1, y))  # On récupère la couleur du pixel de gauche
        gg = int(r1+v1+b1/3)  #   pour en calculer le gris
        r2, v2, b2 = img.getpixel((x, y-1))  # On récupère la couleur du pixel du haut
        gh = int(r2+v2+b2/3)  #   pour en calculer le gris
        # Si la différence entre les gris dépasse la valeur de seuil, on le signale
        if abs(gbase - gg) > 10 or abs(gbase - gh) > 10:
            img.putpixel((x, y), (r,v,b))
        else:
            img.putpixel((x, y), (255,255,255))  
img.show()