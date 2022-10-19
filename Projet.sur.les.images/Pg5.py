from PIL import Image
img = Image.open("/home/moutarde/NSI/Projet.sur.les.images/flower.jpg")
largeur,hauteur = img.size
for y in range(hauteur):
    for x in range(largeur):
        r,v,b=img.getpixel((x,y))
        print(r,v,b)







