r1 = float(input("Diga o comprimento de uma reta: "))
r2 = float(input("Diga o comprimento de uma reta: "))
r3 = float(input("Diga o comprimento de uma reta: "))
if  r1 < r2 + r3:
    if  r2 < r1 + r3:
        if r3 < r1 + r2:
            print("As três retas podem formar um triângulo!")
        else:
            print("As três retas não podem formar um triângulo!")
    else:
        print("As três retas não podem formar um triângulo!")
else:
    print("As três retas não podem formar um triângulo!")
