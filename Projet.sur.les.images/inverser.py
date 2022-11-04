from PIL import Image
img = Image.open("C:\\Users\\gouba\\Documents\\NSI\\Projet.sur.les.images\\flower.jpg")
largeur,hauteur=img.size
image_retourner = Image.new("RGB",(largeur, hauteur))
for y in range(hauteur):
    for x in range(largeur):
        r,v,b=img.getpixel((x,y))
        image_retourner.putpixel( (largeur-1-x,hauteur-1-y) , (r, v, b) )
image_retourner.show()