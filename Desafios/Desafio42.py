r1 = float(input("Diga o comprimento de uma reta: "))
r2 = float(input("Diga o comprimento de uma reta: "))
r3 = float(input("Diga o comprimento de uma reta: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("As três retas podem formar um triângulo!")
    if r1 == r2 == r3:
        print("Esse triângulo é equilátero.")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("Esse triângulo é isóceles.")
    else:
        print("Esse triângulo é escaleno.")
else:
    print("As três retas não podem formar um triângulo!")
