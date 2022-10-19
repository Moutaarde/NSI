from PIL import Image
img = Image.open("/home/moutarde/NSI/Projet.sur.les.images/flower.jpg")

img.putpixel((0,0),(255,0,0))
img.show()




