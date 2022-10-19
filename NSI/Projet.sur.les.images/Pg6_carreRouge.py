from PIL import Image
largeur=600
hauteur=600
img =Image.new('RGB', (largeur,hauteur))
for y in range(hauteur):
    for x in range(largeur):
        img.putpixel((x,y),(255,0,0))

img.show()
img.save("CarreRouge.png", "PNG")


