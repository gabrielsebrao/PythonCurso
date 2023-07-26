running = True
num = num2 = cont = mm = mn = num3 = num4 = 0
while running:
    resp = input("Você quer por algum valor: ").lower().split()
    resp = ''.join(resp)
    if resp == 'sim':
        num4 = num3
        num2 = num
        num = int(input("Digite um valor: "))
        num3 = num
        if cont == 0:
            mm = mn = num
        else:
            if num3 < num4:
                mn = num
            else:
                mm = num
        num += num2
        cont += 1
    elif resp == 'nao':
        running = False
    else:
        print("Digite 'sim' ou 'não', por favor!")
med = num / cont
print("A média dos números que você digitou é: {}".format(med))
print("O maior número é {} e o menor é {}".format(mm, mn))