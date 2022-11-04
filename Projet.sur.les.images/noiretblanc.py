from PIL import Image
img = Image.open("C:\\Users\\gouba\\Documents\\NSI\\Projet.sur.les.images\\flower.jpg")
largeur,hauteur=img.size
for y in range(hauteur):
    for x in range(largeur):
        r,v,b=img.getpixel((x,y))
        m=int(r+v+b/3)
        if m>170:
            m=(255,255,255)
        else:
            m=(0,0,0)
        img.putpixel((x,y),(m)) 
img.show()