from tkinter import *
from tkinter import filedialog
from PIL import Image
from random import randrange

def ouvrir_fichier():
    """donne le chemin d'acces de l'image qui a pour extension .png ou .jpg
    ENTREE: rien
    SORTIE: chemin acces d'une seule image qui a pour extension .png ou .jpg"""
    global nomfichier
    nomfichier=filedialog.askopenfilename(parent=fenetre,title="Choisissez un fichier.",filetypes=[(".png",".jpg")],multiple=NO)

def imagefinale():
    """return image finale
    ENTREE: rien
    SORTIE: une image composee des images choisies par l'utilisateur"""
    global new_im
    img=Image.open(nomfichier)
    largeur,hauteur=img.size
    new_im=Image.new('RGB',(largeur*nb_colonnes,hauteur*nb_lignes))
    bruit()
    niveaudegris()
    negatif()

    #img00
    if img00.get()=="Image de base":
        if img00r.get()==0:
            new_im.paste(img,(0*largeur,0*hauteur))
        else:
            retourner(img)
            new_im.paste(imgretourner,(0*largeur,0*hauteur))
    if img00.get()=="Bruit":
        if img00r.get()==0:
            new_im.paste(imgbruit,(0*largeur,0*hauteur))
        else:
            retourner(imgbruit)
            new_im.paste(imgretourner,(0*largeur,0*hauteur))
    if img00.get()=="Niveau de gris":
        if img00r.get()==0:
            new_im.paste(imggris,(0*largeur,0*hauteur))
        else:
            retourner(imggris)
            new_im.paste(imgretourner,(0*largeur,0*hauteur))
    if img00.get()=="Negatif":
        if img00r.get()==0:
            new_im.paste(imgnegatif,(0*largeur,0*hauteur))
        else:
            retourner(imgnegatif)
            new_im.paste(imgretourner,(0*largeur,0*hauteur))

    #img01
    if img01.get()=="Image de base":
        if img01r.get()==0:
            new_im.paste(img,(0*largeur,1*hauteur))
        else:
            retourner(img)
            new_im.paste(imgretourner,(0*largeur,1*hauteur))
    if img01.get()=="Bruit":
        if img01r.get()==0:
            new_im.paste(imgbruit,(0*largeur,1*hauteur))
        else:
            retourner(imgbruit)
            new_im.paste(imgretourner,(0*largeur,1*hauteur))
    if img01.get()=="Niveau de gris":
        if img01r.get()==0:
            new_im.paste(imggris,(0*largeur,1*hauteur))
        else:
            retourner(imggris)
            new_im.paste(imgretourner,(0*largeur,1*hauteur))
    if img01.get()=="Negatif":
        if img01r.get()==0:
            new_im.paste(imgnegatif,(0*largeur,1*hauteur))
        else:
            retourner(imgnegatif)
            new_im.paste(imgretourner,(0*largeur,1*hauteur))

    #img02
    if img02.get()=="Image de base":
        if img02r.get()==0:
            new_im.paste(img,(0*largeur,2*hauteur))
        else:
            retourner(img)
            new_im.paste(imgretourner,(0*largeur,2*hauteur))
    if img02.get()=="Bruit":
        if img02r.get()==0:
            new_im.paste(imgbruit,(0*largeur,2*hauteur))
        else:
            retourner(imgbruit)
            new_im.paste(imgretourner,(0*largeur,2*hauteur))
    if img02.get()=="Niveau de gris":
        if img02r.get()==0:
            new_im.paste(imggris,(0*largeur,2*hauteur))
        else:
            retourner(imggris)
            new_im.paste(imgretourner,(0*largeur,2*hauteur))
    if img02.get()=="Negatif":
        if img02r.get()==0:
            new_im.paste(imgnegatif,(0*largeur,2*hauteur))
        else:
            retourner(imgnegatif)
            new_im.paste(imgretourner,(0*largeur,2*hauteur))

    #img10
    if img10.get()=="Image de base":
        if img10r.get()==0:
            new_im.paste(img,(1*largeur,0*hauteur))
        else:
            retourner(img)
            new_im.paste(imgretourner,(1*largeur,0*hauteur))
    if img10.get()=="Bruit":
        if img10r.get()==0:
            new_im.paste(imgbruit,(1*largeur,0*hauteur))
        else:
            retourner(imgbruit)
            new_im.paste(imgretourner,(1*largeur,0*hauteur))
    if img10.get()=="Niveau de gris":
        if img10r.get()==0:
            new_im.paste(imggris,(1*largeur,0*hauteur))
        else:
            retourner(imggris)
            new_im.paste(imgretourner,(1*largeur,0*hauteur))
    if img10.get()=="Negatif":
        if img10r.get()==0:
            new_im.paste(imgnegatif,(1*largeur,0*hauteur))
        else:
            retourner(imgnegatif)
            new_im.paste(imgretourner,(1*largeur,0*hauteur))

    #img11
    if img11.get()=="Image de base":
        if img11r.get()==0:
            new_im.paste(img,(1*largeur,1*hauteur))
        else:
            retourner(img)
            new_im.paste(imgretourner,(1*largeur,1*hauteur))
    if img11.get()=="Bruit":
        if img11r.get()==0:
            new_im.paste(imgbruit,(1*largeur,1*hauteur))
        else:
            retourner(imgbruit)
            new_im.paste(imgretourner,(1*largeur,1*hauteur))
    if img11.get()=="Niveau de gris":
        if img11r.get()==0:
            new_im.paste(imggris,(1*largeur,1*hauteur))
        else:
            retourner(imggris)
            new_im.paste(imgretourner,(1*largeur,1*hauteur))
    if img11.get()=="Negatif":
        if img11r.get()==0:
            new_im.paste(imgnegatif,(1*largeur,1*hauteur))
        else:
            retourner(imgnegatif)
            new_im.paste(imgretourner,(1*largeur,1*hauteur))

    #img12
    if img12.get()=="Image de base":
        if img12r.get()==0:
            new_im.paste(img,(1*largeur,2*hauteur))
        else:
            retourner(img)
            new_im.paste(imgretourner,(1*largeur,2*hauteur))
    if img12.get()=="Bruit":
        if img12r.get()==0:
            new_im.paste(imgbruit,(1*largeur,2*hauteur))
        else:
            retourner(imgbruit)
            new_im.paste(imgretourner,(1*largeur,2*hauteur))
    if img12.get()=="Niveau de gris":
        if img12r.get()==0:
            new_im.paste(imggris,(1*largeur,2*hauteur))
        else:
            retourner(imggris)
            new_im.paste(imgretourner,(1*largeur,2*hauteur))
    if img12.get()=="Negatif":
        if img12r.get()==0:
            new_im.paste(imgnegatif,(1*largeur,2*hauteur))
        else:
            retourner(imgnegatif)
            new_im.paste(imgretourner,(1*largeur,2*hauteur))

    #img20
    if img20.get()=="Image de base":
        if img20r.get()==0:
            new_im.paste(img,(2*largeur,0*hauteur))
        else:
            retourner(img)
            new_im.paste(imgretourner,(2*largeur,0*hauteur))
    if img20.get()=="Bruit":
        if img20r.get()==0:
            new_im.paste(imgbruit,(2*largeur,0*hauteur))
        else:
            retourner(imgbruit)
            new_im.paste(imgretourner,(2*largeur,0*hauteur))
    if img20.get()=="Niveau de gris":
        if img20r.get()==0:
            new_im.paste(imggris,(2*largeur,0*hauteur))
        else:
            retourner(imggris)
            new_im.paste(imgretourner,(2*largeur,0*hauteur))
    if img20.get()=="Negatif":
        if img20r.get()==0:
            new_im.paste(imgnegatif,(2*largeur,0*hauteur))
        else:
            retourner(imgnegatif)
            new_im.paste(imgretourner,(2*largeur,0*hauteur))

    #img21
    if img21.get()=="Image de base":
        if img21r.get()==0:
            new_im.paste(img,(2*largeur,1*hauteur))
        else:
            retourner(img)
            new_im.paste(imgretourner,(2*largeur,1*hauteur))
    if img21.get()=="Bruit":
        if img21r.get()==0:
            new_im.paste(imgbruit,(2*largeur,1*hauteur))
        else:
            retourner(imgbruit)
            new_im.paste(imgretourner,(2*largeur,1*hauteur))
    if img21.get()=="Niveau de gris":
        if img21r.get()==0:
            new_im.paste(imggris,(2*largeur,1*hauteur))
        else:
            retourner(imggris)
            new_im.paste(imgretourner,(2*largeur,1*hauteur))
    if img21.get()=="Negatif":
        if img21r.get()==0:
            new_im.paste(imgnegatif,(2*largeur,1*hauteur))
        else:
            retourner(imgnegatif)
            new_im.paste(imgretourner,(2*largeur,1*hauteur))

    #img22
    if img22.get()=="Image de base":
        if img22r.get()==0:
            new_im.paste(img,(2*largeur,2*hauteur))
        else:
            retourner(img)
            new_im.paste(imgretourner,(2*largeur,2*hauteur))
    if img22.get()=="Bruit":
        if img22r.get()==0:
            new_im.paste(imgbruit,(2*largeur,2*hauteur))
        else:
            retourner(imgbruit)
            new_im.paste(imgretourner,(2*largeur,2*hauteur))
    if img22.get()=="Niveau de gris":
        if img22r.get()==0:
            new_im.paste(imggris,(2*largeur,2*hauteur))
        else:
            retourner(imggris)
            new_im.paste(imgretourner,(2*largeur,2*hauteur))
    if img22.get()=="Negatif":
        if img22r.get()==0:
            new_im.paste(imgnegatif,(2*largeur,2*hauteur))
        else:
            retourner(imgnegatif)
            new_im.paste(imgretourner,(2*largeur,2*hauteur))

    return new_im

def afficherapercu():
    """ouvre un apercu temporaire de l'image finale
    ENTREE: rien
    SORTIE: une fenetre avec l'image finale"""
    imagefinale()
    new_im.show()

def enregistrer():
    """ouvre un popup pour demander le chemin ou enregistrer l'image finale puis l'enregistre a cet endroit
    ENTREE: rien
    SORTIE: l'image finale au chemin indique par l'utilisateur"""
    global savechemin
    imagefinale()
    savechemin=filedialog.asksaveasfilename(parent=fenetre,title="Enregistrer un fichier",filetypes=[("Image","*.png")],defaultextension=".png")
    new_im.save(savechemin)

def retourner(img_a_retourner):
    """prend l'image et la renvoie retourner
    ENTREE: une image
    SORTIE: l'image retourne"""
    global imgretourner
    largeur,hauteur=img_a_retourner.size
    imgretourner=Image.new("RGB",(largeur, hauteur))
    for y in range(hauteur):
        for x in range(largeur):
            r,v,b=img_a_retourner.getpixel((x,y))
            imgretourner.putpixel((largeur-1-x,hauteur-1-y),(r,v,b))
    return imgretourner

def bruit():
    """prend l'image et la renvoie avec du bruit
    ENTREE: une image
    SORTIE: l'image avec du bruit aleatoire"""
    global imgbruit
    imgbruit=Image.open(nomfichier)
    largeur,hauteur=imgbruit.size
    for y in range(hauteur):
        for x in range(largeur):
            u=randrange(-100,100)
            z=randrange(-100,100)
            l=randrange(-100,100)
            r,v,b=imgbruit.getpixel((x,y))
            imgbruit.putpixel((x,y),(r+u,v+z,b+l))
    return imgbruit

def niveaudegris():
    """prend l'image et la renvoie en niveau de gris
    ENTREE: une image
    SORTIE: l'image en niveau de gris"""
    global imggris
    imggris=Image.open(nomfichier)
    largeur,hauteur=imggris.size
    for y in range(hauteur):
        for x in range(largeur):
            r,v,b=imggris.getpixel((x,y))
            imggris.putpixel((x,y),(int(r+v+b/3),int(r+v+b/3),int(r+v+b/3)))
    return imggris

def negatif():
    """prend l'image et la renvoie en negatif
    ENTREE: une image
    SORTIE: l'image en negatif"""
    global imgnegatif
    imgnegatif=Image.open(nomfichier)
    largeur,hauteur=imgnegatif.size
    for y in range(hauteur):
        for x in range(largeur):
            r,v,b=imgnegatif.getpixel((x,y))
            imgnegatif.putpixel((x,y),(255-r,255-v,255-b))
    return imgnegatif

def fram1versfram2() :
    """permet d'appeler la fonction pour fermer la frame1ere et la fontion pour ouvrir/creer la f2 en verifiant si on a selectionner une image et si on a un nb de colonnes et de lignes valides
    ENTREE: rien
    SORTIE: appele la fonction pour fermer la frame1ere et la fonction pour ouvrir/creer la f2"""
    if 'nomfichier' in globals():
        if nomfichier=="":
            #affiche une popup qui nous dis qu'il faut selectionner une image
            popuppasdenom=Toplevel()
            popuppasdenom.title("Erreur")
            popuppasdenom.geometry("250x50")
            popuppasdenom.minsize(250,50)
            popuppasdenom.iconphoto(False,iconeerreur)
            textepasdenom=Label(popuppasdenom,text="Veuillez selectionner une image !",font=("Helvetica", 13),fg='black')
            textepasdenom.pack(expand=YES)
        else:
            if 'nb_lignes' in globals() or 'nb_colonnes' in globals():
                if nb_lignes not in (1,2,3) or nb_colonnes not in (1,2,3):
                    #affiche une popup qui nous dis qu'il faut renseigner des nombres de lignes et de colonnes compris entre 1 et 3
                    popupmauvaisnbs=Toplevel()
                    popupmauvaisnbs.title("Erreur")
                    popupmauvaisnbs.geometry("600x50")
                    popupmauvaisnbs.minsize(600,50)
                    popupmauvaisnbs.iconphoto(False,iconeerreur)
                    textemauvaisnbs=Label(popupmauvaisnbs,text="Veuillez renseigner des nombres de lignes et de colonnes compris entre 1 et 3 !",font=("Helvetica", 13),fg='black')
                    textemauvaisnbs.pack(expand=YES)
                else:
                    #tout est correct, on passe a la suite
                    close_frame1ere()
                    create_f2()
            else:
                #affiche une popup qui nous dis qu'il faut cliquer sur le bouton valider des lignes et des colonnes
                popupvalider=Toplevel()
                popupvalider.title("Erreur")
                popupvalider.geometry("670x50")
                popupvalider.minsize(670,50)
                popupvalider.iconphoto(False,iconeerreur)
                textevalider=Label(popupvalider,text="Veuillez cliquer sur les boutons Valider pour valider le nombres de lignes et de colonnes !",font=("Helvetica", 13),fg='black')
                textevalider.pack(expand=YES)
    else:
        #affiche une popup qui nous dis qu'il faut selectionner une image
        popuppasdenom2=Toplevel()
        popuppasdenom2.title("Erreur")
        popuppasdenom2.geometry("250x50")
        popuppasdenom2.minsize(250,50)
        popuppasdenom2.iconphoto(False,iconeerreur)
        textepasdenom2=Label(popuppasdenom2,text="Veuillez selectionner une image !",font=("Helvetica", 13),fg='black')
        textepasdenom2.pack(expand=YES)

def fonc_nb_colonnes():
    """utiliser afin de prendre la valeur du champs colonnes et le stocker dans la variable nb_colonnes
    ENTREE: rien
    SORTIE: varible nb_colonnes"""
    global nb_colonnes
    nb_colonnes=IntVar()
    nb_colonnes=int(user_nb_colonnes.get())

def fonc_nb_lignes():
    """utiliser afin de prendre la valeur du champs lignes et le stocker dans la variable nb_lignes
    ENTREE: rien
    SORTIE: varible nb_lignes"""
    global nb_lignes
    nb_lignes=IntVar()
    nb_lignes=int(user_nb_lignes.get())

def fram2versfram1() :
    """permet d'appeler la fonction pour fermer la f2 et la fontion pour ouvrir/creer la frame1ere
    ENTREE: rien
    SORTIE: appele la fonction pour fermer la f2 et la fonction pour ouvrir/creer la frame1ere"""
    close_f2()
    create_frame1ere()

def close_frame1ere():
    """permet de fermer la frame1ere
    ENTREE: rien
    SORTIE: ferme la frame1ere"""
    global frame1ere
    frame1ere.destroy()

def close_f2():
    """permet de fermer la f2
    ENTREE: rien
    SORTIE: ferme la f2"""
    global f2
    f2.destroy()

def create_frame1ere():
    """permet de ouvrir/creer la frame1ere
    ENTREE: rien
    SORTIE: ouvre/cree la frame1ere"""
    global frame1ere, textebienvenue, texteexplicationapp, boutonchoosefile, boutonbruit, colonnes, lignes, user_nb_colonnes, boutonvalidercolonnes, user_nb_lignes, boutonvaliderlignes, texteexplicationlignes, texteexplicationcolonnes

    #parametres frame
    frame1ere=Frame(fenetre)

    #texte bienvenue (titre)
    textebienvenue=Label(frame1ere,text="Bienvenue sur le createur d'oeuvre d'art !",font=("Helvetica", 30),fg='black')
    textebienvenue.pack()

    #texte explicatif
    texteexplicationapp=Label(frame1ere,text="Dans ce programme, vous pouvez a partir d'une image en creer une multitude avec differents effets, puis les rassembler dans une image.",font=("Helvetica", 15),fg='black',wraplengt=650)
    texteexplicationapp.pack()

    #bouton choisir fichier
    boutonchoosefile=Button(frame1ere,text="Choisir une image",font=("Helvetica", 20),bg='#ca4d31',fg='white',command=ouvrir_fichier)
    boutonchoosefile.pack(pady=15)

    #champs pour saisir nb colonnes + textes explicatifs + bouton valider
    texteexplicationcolonnes=Label(frame1ere,text="Rentrez ici le nombre de colonnes souhaité pour l'image finale",font=("Helvetica", 15),fg='black',wraplengt=350)
    texteexplicationcolonnes.pack()
    user_nb_colonnes=IntVar()
    colonnes=Entry(frame1ere,font=("Helvetica", 20),fg='black',textvariable=user_nb_colonnes)
    colonnes.pack()
    boutonvalidercolonnes=Button(frame1ere,text="Valider",font=("Helvetica", 10),bg='#ca4d31',fg='white',command=fonc_nb_colonnes)
    boutonvalidercolonnes.pack(pady=10)

    #champs pour saisir nb lignes + textes explicatifs + bouton valider
    texteexplicationlignes=Label(frame1ere,text="Rentrez ici le nombre de lignes souhaité pour l'image finale",font=("Helvetica", 15),fg='black',wraplengt=350)
    texteexplicationlignes.pack()
    user_nb_lignes=IntVar()
    lignes=Entry(frame1ere,font=("Helvetica", 20),fg='black',textvariable=user_nb_lignes)
    lignes.pack()
    boutonvaliderlignes=Button(frame1ere,text="Valider",font=("Helvetica", 10),bg='#ca4d31',fg='white',command=fonc_nb_lignes)
    boutonvaliderlignes.pack(pady=10)

    #bouton etape suivante
    boutonetapesuivante=Button(frame1ere, text='Etape suivante',font=("Helvetica", 15),bg='#ca4d31',fg='white',command=fram1versfram2)
    boutonetapesuivante.pack(pady=15)

    #creation frame
    frame1ere.pack(expand=YES)

def create_f2():
    """permet de ouvrir/creer la 2
    ENTREE: rien
    SORTIE: ouvre/cree la 2"""
    global f2, listeoptions, img00, img01, img02, img10, img11, img12, img20, img21, img22, img00r, img01r, img02r, img10r, img11r, img12r, img20r, img21r, img22r

    #parametres frame
    f2 = Frame(fenetre)

    #texte explication2 (titre)
    texteexplication2=Label(f2,text="Choississez les effets que vous souhaitez pour chaque image",font=("Helvetica", 20),fg='black')
    texteexplication2.grid(row=0,pady=10,columnspan=3)

    #menus deroulants pour choisir les effets
    listeoptions=["Image de base","Bruit","Niveau de gris","Negatif"]
    img00=StringVar(f2)
    img00r=IntVar(f2)
    img01=StringVar(f2)
    img01r=IntVar(f2)
    img02=StringVar(f2)
    img02r=IntVar(f2)
    img10=StringVar(f2)
    img10r=IntVar(f2)
    img11=StringVar(f2)
    img11r=IntVar(f2)
    img12=StringVar(f2)
    img12r=IntVar(f2)
    img20=StringVar(f2)
    img20r=IntVar(f2)
    img21=StringVar(f2)
    img21r=IntVar(f2)
    img22=StringVar(f2)
    img22r=IntVar(f2)
    if nb_colonnes==1 and nb_lignes==1:
        #img00
        img00.set(listeoptions[0])
        menuderoulant=OptionMenu(f2,img00,*listeoptions)
        menuderoulant.config(width=20, font=('Helvetica', 15))
        menuderoulant.grid(column=1,row=1)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img00r, onvalue=1, offvalue=0)
        checkbox.grid(column=1,row=2)
    if nb_colonnes==1 and nb_lignes==2:
        #img00
        img00.set(listeoptions[0])
        menuderoulant=OptionMenu(f2,img00,*listeoptions)
        menuderoulant.config(width=20, font=('Helvetica', 15))
        menuderoulant.grid(column=1,row=1)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img00r, onvalue=1, offvalue=0)
        checkbox.grid(column=1,row=2)
        
        #img01
        img01.set(listeoptions[0])
        menuderoulant2=OptionMenu(f2,img01,*listeoptions)
        menuderoulant2.config(width=20, font=('Helvetica', 15))
        menuderoulant2.grid(column=1,row=3)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img01r, onvalue=1, offvalue=0)
        checkbox.grid(column=1,row=4)
    if nb_colonnes==1 and nb_lignes==3:
        #img00        
        img00.set(listeoptions[0])
        menuderoulant=OptionMenu(f2,img00,*listeoptions)
        menuderoulant.config(width=20, font=('Helvetica', 15))
        menuderoulant.grid(column=1,row=1)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img00r, onvalue=1, offvalue=0)
        checkbox.grid(column=1,row=2)
        
        #img01
        img01.set(listeoptions[0])
        menuderoulant2=OptionMenu(f2,img01,*listeoptions)
        menuderoulant2.config(width=20, font=('Helvetica', 15))
        menuderoulant2.grid(column=1,row=3)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img01r, onvalue=1, offvalue=0)
        checkbox.grid(column=1,row=4)
        
        #img02
        img02.set(listeoptions[0])
        menuderoulant3=OptionMenu(f2,img02,*listeoptions)
        menuderoulant3.config(width=20, font=('Helvetica', 15))
        menuderoulant3.grid(column=1,row=5)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img02r, onvalue=1, offvalue=0)
        checkbox.grid(column=1,row=6)
    if nb_colonnes==2 and nb_lignes==1:
        #img00
        img00.set(listeoptions[0])
        menuderoulant=OptionMenu(f2,img00,*listeoptions)
        menuderoulant.config(width=20, font=('Helvetica', 15))
        menuderoulant.grid(column=0,row=1)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img00r, onvalue=1, offvalue=0)
        checkbox.grid(column=0,row=2)

        #img10
        img10.set(listeoptions[0])
        menuderoulant5=OptionMenu(f2,img10,*listeoptions)
        menuderoulant5.config(width=20, font=('Helvetica', 15))
        menuderoulant5.grid(column=1,row=1)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img10r, onvalue=1, offvalue=0)
        checkbox.grid(column=1,row=2)
    if nb_colonnes==2 and nb_lignes==2:
        #img00
        img00.set(listeoptions[0])
        menuderoulant=OptionMenu(f2,img00,*listeoptions)
        menuderoulant.config(width=20, font=('Helvetica', 15))
        menuderoulant.grid(column=0,row=1)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img00r, onvalue=1, offvalue=0)
        checkbox.grid(column=0,row=2)
        
        #img01
        img01.set(listeoptions[0])
        menuderoulant2=OptionMenu(f2,img01,*listeoptions)
        menuderoulant2.config(width=20, font=('Helvetica', 15))
        menuderoulant2.grid(column=0,row=3)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img01r, onvalue=1, offvalue=0)
        checkbox.grid(column=0,row=4)

        #img10
        img10.set(listeoptions[0])
        menuderoulant5=OptionMenu(f2,img10,*listeoptions)
        menuderoulant5.config(width=20, font=('Helvetica', 15))
        menuderoulant5.grid(column=1,row=1)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img10r, onvalue=1, offvalue=0)
        checkbox.grid(column=1,row=2)

        #img11
        img11.set(listeoptions[0])
        menuderoulant6=OptionMenu(f2,img11,*listeoptions)
        menuderoulant6.config(width=20, font=('Helvetica', 15))
        menuderoulant6.grid(column=1,row=3)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img11r, onvalue=1, offvalue=0)
        checkbox.grid(column=1,row=4)
    if nb_colonnes==2 and nb_lignes==3:
        #img00
        img00.set(listeoptions[0])
        menuderoulant=OptionMenu(f2,img00,*listeoptions)
        menuderoulant.config(width=20, font=('Helvetica', 15))
        menuderoulant.grid(column=0,row=1)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img00r, onvalue=1, offvalue=0)
        checkbox.grid(column=0,row=2)
        
        #img01
        img01.set(listeoptions[0])
        menuderoulant2=OptionMenu(f2,img01,*listeoptions)
        menuderoulant2.config(width=20, font=('Helvetica', 15))
        menuderoulant2.grid(column=0,row=3)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img01r, onvalue=1, offvalue=0)
        checkbox.grid(column=0,row=4)

        #img02
        img02.set(listeoptions[0])
        menuderoulant3=OptionMenu(f2,img02,*listeoptions)
        menuderoulant3.config(width=20, font=('Helvetica', 15))
        menuderoulant3.grid(column=0,row=5)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img02r, onvalue=1, offvalue=0)
        checkbox.grid(column=0,row=6)

        #img10
        img10.set(listeoptions[0])
        menuderoulant5=OptionMenu(f2,img10,*listeoptions)
        menuderoulant5.config(width=20, font=('Helvetica', 15))
        menuderoulant5.grid(column=1,row=1)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img10r, onvalue=1, offvalue=0)
        checkbox.grid(column=1,row=2)

        #img11
        img11.set(listeoptions[0])
        menuderoulant6=OptionMenu(f2,img11,*listeoptions)
        menuderoulant6.config(width=20, font=('Helvetica', 15))
        menuderoulant6.grid(column=1,row=3)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img11r, onvalue=1, offvalue=0)
        checkbox.grid(column=1,row=4)
        
        #img12
        img12.set(listeoptions[0])
        menuderoulant7=OptionMenu(f2,img12,*listeoptions)
        menuderoulant7.config(width=20, font=('Helvetica', 15))
        menuderoulant7.grid(column=1,row=5)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img12r, onvalue=1, offvalue=0)
        checkbox.grid(column=1,row=6)
    if nb_colonnes==3 and nb_lignes==1:
        #img00
        img00.set(listeoptions[0])
        menuderoulant=OptionMenu(f2,img00,*listeoptions)
        menuderoulant.config(width=20, font=('Helvetica', 15))
        menuderoulant.grid(column=0,row=1)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img00r, onvalue=1, offvalue=0)
        checkbox.grid(column=0,row=2)

        #img10
        img10.set(listeoptions[0])
        menuderoulant5=OptionMenu(f2,img10,*listeoptions)
        menuderoulant5.config(width=20, font=('Helvetica', 15))
        menuderoulant5.grid(column=1,row=1)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img10r, onvalue=1, offvalue=0)
        checkbox.grid(column=1,row=2)

        #img20
        img20.set(listeoptions[0])
        menuderoulant9=OptionMenu(f2,img20,*listeoptions)
        menuderoulant9.config(width=20, font=('Helvetica', 15))
        menuderoulant9.grid(column=2,row=1)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img20r, onvalue=1, offvalue=0)
        checkbox.grid(column=2,row=2)
    if nb_colonnes==3 and nb_lignes==2:
        #img00
        img00.set(listeoptions[0])
        menuderoulant=OptionMenu(f2,img00,*listeoptions)
        menuderoulant.config(width=20, font=('Helvetica', 15))
        menuderoulant.grid(column=0,row=1)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img00r, onvalue=1, offvalue=0)
        checkbox.grid(column=0,row=2)

        #img01
        img01.set(listeoptions[0])
        menuderoulant2=OptionMenu(f2,img01,*listeoptions)
        menuderoulant2.config(width=20, font=('Helvetica', 15))
        menuderoulant2.grid(column=0,row=3)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img01r, onvalue=1, offvalue=0)
        checkbox.grid(column=0,row=4)

        #img10
        img10.set(listeoptions[0])
        menuderoulant5=OptionMenu(f2,img10,*listeoptions)
        menuderoulant5.config(width=20, font=('Helvetica', 15))
        menuderoulant5.grid(column=1,row=1)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img10r, onvalue=1, offvalue=0)
        checkbox.grid(column=1,row=2)

        #img11
        img11.set(listeoptions[0])
        menuderoulant6=OptionMenu(f2,img11,*listeoptions)
        menuderoulant6.config(width=20, font=('Helvetica', 15))
        menuderoulant6.grid(column=1,row=3)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img11r, onvalue=1, offvalue=0)
        checkbox.grid(column=1,row=4)

        #img20
        img20.set(listeoptions[0])
        menuderoulant9=OptionMenu(f2,img20,*listeoptions)
        menuderoulant9.config(width=20, font=('Helvetica', 15))
        menuderoulant9.grid(column=2,row=1)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img20r, onvalue=1, offvalue=0)
        checkbox.grid(column=2,row=2)
        
        #img21
        img21.set(listeoptions[0])
        menuderoulant10=OptionMenu(f2,img21,*listeoptions)
        menuderoulant10.config(width=20, font=('Helvetica', 15))
        menuderoulant10.grid(column=2,row=3)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img21r, onvalue=1, offvalue=0)
        checkbox.grid(column=2,row=4)
    if nb_colonnes==3 and nb_lignes==3:
        #img00
        img00.set(listeoptions[0])
        menuderoulant=OptionMenu(f2,img00,*listeoptions)
        menuderoulant.config(width=20, font=('Helvetica', 15))
        menuderoulant.grid(column=0,row=1)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img00r, onvalue=1, offvalue=0)
        checkbox.grid(column=0,row=2)

        #img01
        img01.set(listeoptions[0])
        menuderoulant2=OptionMenu(f2,img01,*listeoptions)
        menuderoulant2.config(width=20, font=('Helvetica', 15))
        menuderoulant2.grid(column=0,row=3)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img01r, onvalue=1, offvalue=0)
        checkbox.grid(column=0,row=4)

        #img02
        img02.set(listeoptions[0])
        menuderoulant3=OptionMenu(f2,img02,*listeoptions)
        menuderoulant3.config(width=20, font=('Helvetica', 15))
        menuderoulant3.grid(column=0,row=5)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img02r, onvalue=1, offvalue=0)
        checkbox.grid(column=0,row=6)

        #img10
        img10.set(listeoptions[0])
        menuderoulant5=OptionMenu(f2,img10,*listeoptions)
        menuderoulant5.config(width=20, font=('Helvetica', 15))
        menuderoulant5.grid(column=1,row=1)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img10r, onvalue=1, offvalue=0)
        checkbox.grid(column=1,row=2)

        #img11
        img11.set(listeoptions[0])
        menuderoulant6=OptionMenu(f2,img11,*listeoptions)
        menuderoulant6.config(width=20, font=('Helvetica', 15))
        menuderoulant6.grid(column=1,row=3)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img11r, onvalue=1, offvalue=0)
        checkbox.grid(column=1,row=4)

        #img12
        img12.set(listeoptions[0])
        menuderoulant7=OptionMenu(f2,img12,*listeoptions)
        menuderoulant7.config(width=20, font=('Helvetica', 15))
        menuderoulant7.grid(column=1,row=5)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img12r, onvalue=1, offvalue=0)
        checkbox.grid(column=1,row=6)

        #img20
        img20.set(listeoptions[0])
        menuderoulant9=OptionMenu(f2,img20,*listeoptions)
        menuderoulant9.config(width=20, font=('Helvetica', 15))
        menuderoulant9.grid(column=2,row=1)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img20r, onvalue=1, offvalue=0)
        checkbox.grid(column=2,row=2)
        
        #img21
        img21.set(listeoptions[0])
        menuderoulant10=OptionMenu(f2,img21,*listeoptions)
        menuderoulant10.config(width=20, font=('Helvetica', 15))
        menuderoulant10.grid(column=2,row=3)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img21r, onvalue=1, offvalue=0)
        checkbox.grid(column=2,row=4)
        
        #img22
        img22.set(listeoptions[0])
        menuderoulant11=OptionMenu(f2,img22,*listeoptions)
        menuderoulant11.config(width=20, font=('Helvetica', 15))
        menuderoulant11.grid(column=2,row=5)
        checkbox=Checkbutton(f2, text='Retourner ?',variable=img22r, onvalue=1, offvalue=0)
        checkbox.grid(column=2,row=6)

    #bouton annuler
    boutonannuler=Button(f2, text='Annuler',font=("Helvetica", 15),bg='#ca4d31',fg='white', command=fram2versfram1)
    boutonannuler.grid(column=0,row=nb_lignes*2+1,padx=10,pady=10)

    #bouton apercu de l'image
    boutonannuler=Button(f2, text="Apercu de l'image finale",font=("Helvetica", 15),bg='#ca4d31',fg='white', command=afficherapercu)
    boutonannuler.grid(column=1,row=nb_lignes*2+1,padx=10,pady=10)

    #bouton enregistrer l'image
    boutonannuler=Button(f2, text="Enregistrer l'image finale",font=("Helvetica", 15),bg='#ca4d31',fg='white', command=enregistrer)
    boutonannuler.grid(column=2,row=nb_lignes*2+1,padx=10,pady=10)

    #creation frame
    f2.pack(expand=YES)

#parametre fenetre principale
fenetre=Tk()
fenetre.title("Createur d'oeuvres d'art")
fenetre.geometry("800x600")
fenetre.minsize(800,600)
icone_data="""R0lGODlhAAGrAPcAAAAAAGgWBHYZBHEOA3slB10NAIYcDqYcDIcnB5
ojDJUpCZo3B5srE5kqFpw0FYsuEKcnDaU7BrU8CaQrFKwsFasuGaQoFLMrE7MtGrwtGKUzG6wzG6
o8G6Y3F7QzHLs0HbQ6HLs7HbY2FrMoD5s4J5A1Kaw1Iqs7JKw9K6U5JbQ2Ibs2IrQ7JLs8JbQ9Kb
s+Kqw4K8U0Hco1HsM8Hck5HcAuGcM8I8s9I8M+Ksg6JdI9JNs+JqlICbZJB6tSCrtbBb1cCbdWB7
hEG7BMF7xjCbpgE51CLKxDLahHK7RDJLxCJLRDLLxDK7NKLrxKLbpLJbtUKq1FMa1LM6ZKNbRFMb
tFMbRLM7xLM7dLOqlSObRRNbxSNbRTO7xUO7tZPKxQIJtFB8VZCcJDHchHGspVFsxSEcNkBsprBc
RjC8lnCNVqCM1yBMxzCtJ0Bdh3CMlmENZlGth0FOR4FMRDJctDJcxKJMRELMtFLMRKLMxKLcNKJt
NDJdJLJtJFK9NLLdtMLNpGJ8xTLMhUKtRTLNtSLdZaKsRGMctFMcRLM8xLM8VOOs1NOstHONJGMd
NMM9pNM9ROOtpNOsRSNcxSNcRTOsxTO8NbPM1aPcpcMtRSNNtTNNRaM9xbNNRUO9tVO9RaPdxaPO
JMLOFSLeZaL+NOM+JUNOpUNeNbNeJVOuRbO+pcPOlbOPNbO9xiLt1jNN1iPNllPcxgMeNjNeVkO+
tjPORqO+trPednNvJnPet0M7lZQ65SQbxkS8NbQ81bQspWRNNVQtpWQdNcQttcQ9NdStlbStFQRO
RcQ+pdQuNbRvBfQ81lS8pkSdRhRdtiRdRjS9tkS9tpTtNqTMtoVNVrUttsU9dnVNhzWs5xVeRjRO
xkROVqROxrQ+RkSetlS+VqS+xqTPNkRPNsRPJlSfVrSvpsS/lnR+1yQ+1yS/N0RPZ5RvVzTPtyTP
V6Svp7TPlyRehqUvNuUv1uUfRzVPt1Ufx7VPt8WvZ4WO91U9J1Yvt9YOSCB+OCEf2CXPuHWv6HYS
H5BAEAAAAAIf8LSW1hZ2VNYWdpY2sNZ2FtbWE9MC40NTQ1NQAh/wtYTVAgRGF0YVhNUDw/eHBhY2
tldCBiZWdpbj0n77u/JyBpZD0nVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkJz8+Cjx4OnhtcG1ldG
EgeG1sbnM6eD0nYWRvYmU6bnM6bWV0YS8nIHg6eG1wdGs9J0ltYWdlOjpFeGlmVG9vbCAxMi40MC
c+CjxyZGY6UkRGIHhtbG5zOnJkZj0naHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3
ludGF4LW5zIyc+CgogPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9JycKICB4bWxuczp0aWZmPS
dodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyc+CiAgPHRpZmY6T3JpZW50YXRpb24+MTwvdG
lmZjpPcmllbnRhdGlvbj4KIDwvcmRmOkRlc2NyaXB0aW9uPgo8L3JkZjpSREY+CjwveDp4bXBtZX
RhPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIA
ogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAo8P3hwYWNrZXQgZW5kPSd3Jz8+Af/+/f
z7+vn49/b19PPy8fDv7u3s6+rp6Ofm5eTj4uHg397d3Nva2djX1tXU09LR0M/OzczLysnIx8bFxM
PCwcC/vr28u7q5uLe2tbSzsrGwr66trKuqqainpqWko6KhoJ+enZybmpmYl5aVlJOSkZCPjo2Mi4
qJiIeGhYSDgoGAf359fHt6eXh3dnV0c3JxcG9ubWxramloZ2ZlZGNiYWBfXl1cW1pZWFdWVVRTUl
FQT05NTEtKSUhHRkVEQ0JBQD8+PTw7Ojk4NzY1NDMyMTAvLi0sKyopKCcmJSQjIiEgHx4dHBsaGR
gXFhUUExIREA8ODQwLCgkIBwYFBAMCAQAALAAAAAAAAasAAAj+AAEIHEiwoMGDCBMqXMiwocOHEC
NKnEixosWLGDNq3Mixo8ePIEOKHEmypMmTKFOqXMmypcuXMGPKnEmzps2bOHPq3Mmzp8+fQIMKHU
q0qNGjSJMqXcq0qdOnUKNKnUq1qtWrWLNq3cq1q9evYMOKHUu2rNmzaNOqXcu2rdu3cOPKnUt3IL
Zr1p49q4aN2jRidQMjxNbX2rRlz6BVe0assTVrxoxZE1wXmzRq1PL6IvZMWmPH0B4DM0w5rrS+1P
T+Wt1MmC9hjovJXmwtc2m3naVVK/asU6XXwir93py3WLdqiKPBq3Z77TS9eoP5FkZdeCXqz4QB01
uNWLFo1L7+NU/LTBpi19aFXaqEqNKlS8+aXcL+DFgxzt0mjy9bntmyZp9Uoohw7yFCiXC+NPNaJ8
LoBcxr0EADz35kMcNMMxiuh8gk712CSBXpBdcJMMIMA8xvDUZI4VgXKlhgIpV8sp4h7QmnoHAMfi
IMJdoNA0030KwIliWWPAOLfJLYMckkwuHBRHuKPFhJIoswGBwlwAQzTDGhCfnVJc08894keOCRSC
dLMmGHIYlMgiYiiUDSyTDqVcIgl9AU46VQ1lxTzTXX5ANoPoQCaqigCfUCJjHCfEJmm2g68cILOB
jSCZqJJOKInAHGSWJ2yez50zSG+nkNPKfCsxw11bT6J2b+2ExjkBetvcYeIhtWMomkVbxgaSKHGL
Ipg5cogggkJGqpp6g7TXPYMpi1Ck+E0ERjbTXRSCNNM8zkVg01vAzUyy+v6ZgInDB2IgkLLrzQQi
KfLHIIIo5cKpwTwo5IDJ3BMJuTs8s05ku3zzhDLTQGV1vttsI0Iw14hwm0moybVMIIrohkkskTLL
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"""
iconefleur=PhotoImage(data=icone_data)
fenetre.iconphoto(False,iconefleur)
fenetre.config()

#stockage icone erreur en base 64
icone_erreur_data="""R0lGODlhAAHhAPcAAAAAAAEBAQgHAgwLAhAPAxQTAxgXAxwaBCEfBC
UjBSkmBS0rBjEuBjUyBzk2Bz05Bz05CEA8B0M/CEZBCEpFCU5JCVJNClZRClpVCl5ZC2JdC2ZgDG
pkDG5oDXNsDXdwDnt0Dn94D4N7D4d/EIh/EImBD4yEEJCHEJSMEZiPEZyTEqCXEqWbEqieE6yiE7
GnFLWqFLmuFb2yFcK2Fsa6Fsq+F83BF9PGF9HEF9THF9LFF9TIF9HFGNPHGNTHGNPHGNfKGNfLGN
bJGNnMGNrNGNvOGNvPGN3PGdrNGN3QGd7RGd/RGd/SGd7RGeDTGeHTGeHUGeLVGeTWGeXYGebYGe
faGeXYGubYGufZGubZGujaGujbGuvdGuzeGu3fGuvdGu7gGu/gGu/hGu7gGvDhG/DiG/HjG/LjG/
LkG/PkG/PlG/TlG/TmG/bnG/PlG/boG/foG/fpG/foG/jpG/nqG/jqHPnqHPnrHPrrHPrsHPvsHP
ztHP3tHP3uHP7uHP7vHP/vHP3uHP/wHP/xHP/yHP/wHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC
H5BAEAAAAAIf8LSW1hZ2VNYWdpY2sNZ2FtbWE9MC40NTQ1NQAh/wtYTVAgRGF0YVhNUDw/eHBhY2
tldCBiZWdpbj0n77u/JyBpZD0nVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkJz8+Cjx4OnhtcG1ldG
EgeG1sbnM6eD0nYWRvYmU6bnM6bWV0YS8nIHg6eG1wdGs9J0ltYWdlOjpFeGlmVG9vbCAxMi40MC
c+CjxyZGY6UkRGIHhtbG5zOnJkZj0naHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3
ludGF4LW5zIyc+CgogPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9JycKICB4bWxuczp0aWZmPS
dodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyc+CiAgPHRpZmY6T3JpZW50YXRpb24+MTwvdG
lmZjpPcmllbnRhdGlvbj4KIDwvcmRmOkRlc2NyaXB0aW9uPgo8L3JkZjpSREY+CjwveDp4bXBtZX
RhPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIA
ogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC
AgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAo8P3hwYWNrZXQgZW5kPSd3Jz8+Af/+/f
z7+vn49/b19PPy8fDv7u3s6+rp6Ofm5eTj4uHg397d3Nva2djX1tXU09LR0M/OzczLysnIx8bFxM
PCwcC/vr28u7q5uLe2tbSzsrGwr66trKuqqainpqWko6KhoJ+enZybmpmYl5aVlJOSkZCPjo2Mi4
qJiIeGhYSDgoGAf359fHt6eXh3dnV0c3JxcG9ubWxramloZ2ZlZGNiYWBfXl1cW1pZWFdWVVRTUl
FQT05NTEtKSUhHRkVEQ0JBQD8+PTw7Ojk4NzY1NDMyMTAvLi0sKyopKCcmJSQjIiEgHx4dHBsaGR
gXFhUUExIREA8ODQwLCgkIBwYFBAMCAQAALAAAAAAAAeEAAAj+AAEIHEiwoMGDCBMqXMiwocOHCP
tAnEixosWLGDNq3MixYp+PIENK7EiypMmTKFOiFMkypMqXMGPKnHmxpc2PNHPq3MmT5M2fPYMKHU
oUwE08aPTcLMq0qVOfLNnI8FAhAgUQNea0fMq1q1eFLAcZ4VAggFmzBz5YGSTyq9u3XEP++cOkwt
m7AQRowCJo7tyRcAML1inyzxkOePEKEDHnTx7HOAdLnpyysIuyie8eqOH3T2TKoENjZKllQubEGc
7MzQNStOvXDkUOQiHgNN4CLjy7hM2790DZOBjYThwBC9vdvpOHZvnGw/DEAk6wVE6dsmwaBqAPX4
DjeOvq4N/+suSC4flpD2ymh18fN+SgFgTMZzYww/tn9viHymYCQf5pC2eol9+AO7VkQm3+JUYACw
IS6KBMIPllgwLmIXjaA0/YB9iDHK4U4R9sdJDgcCU02OGJHcn1RwzZjXiaAjYI0haKNGpUGBd2uW
gbB2iYWOOPDxW2wgA62mZADBoCqWSQ7g3hQJHDVcCFj0tW+ZtIeohgIZTQqZCklWASxFINB3A5XA
NGfBmmlVFpYOZwi+FB5Zo0yvZCi/IVcMGWz202J50dkmZaghoYQcGIGvQ4I6A1spQCn8MlMIMgly
VogAtqMnoiS0MIlyAIegiCRgYjTmDcopo+yBIeH5wFaWL+CxjRhyCC0FCmfwKg8Geq6113q3y5fv
SHIHN88Oppse7KK3VRlZegqR89JsgQC4z4gVaoLturSC1gliemwvp1wrGZHVBfttpWJ1sUEYyIQR
ogPTaXFu0meIGiyKWrrkgHJngADd455th73ppHQAuZ6pscS0JQmOC1AfvVxxnO+hdBhugq/BpLcz
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"""
iconeerreur=PhotoImage(data=icone_erreur_data)

#mise en place de fenetre et de frame
create_frame1ere()
fenetre.mainloop()