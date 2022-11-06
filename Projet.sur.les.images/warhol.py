from PIL import Image
img = Image.open("C:\\Users\\gouba\\Documents\\NSI\\Projet.sur.les.images\\flower.jpg")
largeur,hauteur=img.size
for y in range(hauteur):
    for x in range(largeur):
        r,v,b=img.getpixel((x,y))
        #img.putpixel((x,y),(v,b,r))
        #img.putpixel((x,y),(b,r,v))
        #if r>v and r>b:
            #img.putpixel((x,y),(0,v,b))
        #if v>r and v>b:
            #img.putpixel((x,y),(r,0,b))
        #if b>v and b>r:
            #img.putpixel((x,y),(r,v,0))
img.show()