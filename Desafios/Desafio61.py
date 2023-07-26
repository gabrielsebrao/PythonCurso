t1 = int(input("Escreva o primeiro termo de uma progessao aritmetica: "))
r = int(input("Qual e a razao dessa progressao aritmetica? "))
c = 2
q = 11
running = True
while running:
    while c < q:
        tc = t1+(c-1)*r
        print("a{} = {}".format(c, tc))
        c += 1
    if c == q:
        m = int(input("Você quer que apareça mais quantos termos? "))
        if m == 0:
            running = False
        q += m
