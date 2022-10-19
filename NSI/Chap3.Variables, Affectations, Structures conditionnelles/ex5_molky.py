# Créé par moutarde, le 16/09/2022 en Python 3.7
pts=int(input("Combien de points avez vous ?"))
ptsenplus=int(input("Combien de points avez vous gagné ?"))
ptsfinal=pts+ptsenplus
if ptsfinal==51 :
    print("Vous avez gagné !")
else :
    if ptsfinal<51 :
        print("Votre sccore est de : ",ptsfinal)
    else :
        ptsfinal=25
        print("Vous avez depassé 51, votre score est de : ",ptsfinal)
