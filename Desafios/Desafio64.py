running = True
r = 0
cont = 0
r1 = 0
while running:
    c = int(input("Digite um número: "))
    if c != 999:
        r = c
        r += r1
        r1 = r
        cont += 1
    else:
        running = False
print("Você pôs {} números no sistema.".format(cont))
print("A soma dos números colocados foi {}".format(r))