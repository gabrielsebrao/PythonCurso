import math
co = float(input("Digite o comprimento do Cateto Oposto: "))
ca = float(input("Digite o comprimento do Cateto Adjacente: "))
hip = math.hypot(co, ca)
print("O comprimento da hipotenusa é {}.".format(hip))
