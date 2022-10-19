from PIL import Image
img = Image.open("/home/moutarde/NSI/Projet.sur.les.images/flower.jpg")
R,V,B=img.getpixel((0,0))
print("R=",R, "V=",V, "B=", B)



