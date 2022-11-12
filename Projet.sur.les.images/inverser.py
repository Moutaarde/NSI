from PIL import Image
img = Image.open("C:\\Users\\gouba\\Documents\\NSI\\Projet.sur.les.images\\flower.jpg")
largeur,hauteur=img.size
image_retourner = Image.new("RGB",img.size)
for x in range(largeur):
    flipped_x = largeur - x - 1
    for y in range(hauteur):
        pixel=img.getpixel((x,y))
        ##image_retourner.putpixel( (largeur-1-x,hauteur-1-y) , (r, v, b) )
        image_retourner.putpixel((flipped_x ,y),pixel)
image_retourner.show()
#