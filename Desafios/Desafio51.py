t1 = int(input("Escreva o primeiro termo de uma progessao aritmetica: "))
r = int(input("Qual e a razao dessa progressao aritmetica? "))
for c in range(2, 11):
    tc = t1+(c-1)*r
    print("a{} = {}".format(c, tc), end=', ')
