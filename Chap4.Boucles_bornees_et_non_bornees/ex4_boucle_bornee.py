# Créé par moutarde, le 06/10/2022 en Python 3.7
for a in range(1,10):
    for b in range(10):
        nb=10*a+b
        if a+b==13 and (b*10+a)*nb==4930:
                print(a,b)
