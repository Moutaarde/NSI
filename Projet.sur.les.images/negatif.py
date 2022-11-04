from PIL import Image
img = Image.open("C:\\Users\\gouba\\Documents\\NSI\\Projet.sur.les.images\\flower.jpg")
largeur,hauteur=img.size
for y in range(hauteur):
    for x in range(largeur):
        r,v,b=img.getpixel((x,y))
        img.putpixel((x,y),(255-r,255-v,255-b))
img.show()