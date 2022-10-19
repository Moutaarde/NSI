score=0
while score!=51:
    pts=int(input("pts marqués?"))
    while pts>12 or pts<0:
        pts=int(input("entrer un nb de points valide!!!"))
    score=score+pts
    if score>51:
        score=25
        print("votre score est maintenant égal à ", score)
    else:
        if score==51:
            print("bien joué vous avez gagné")
        print("vous y êtes presque! Votre score est:", score)



