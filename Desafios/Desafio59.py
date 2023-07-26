running = True
opt = 4
while opt != 5:
    if opt == 4:
        n1 = int(input("Digite um valor: "))
        n2 = int(input("Digite outro: "))
    opt = int(input('''O que você quer fazer com esses valores? 
[ 1 ] - Somar
[ 2 ] - Multiplicar
[ 3 ] - Maior
[ 4 ] - Novos Números
[ 5 ] - Sair do Programa
Opção: '''))
    if opt == 1:
        sum = n1 + n2
        print("A soma desses dois valores é: {}".format(sum))
    elif opt == 2:
        mult = n1 * n2
        print("O produto desses dois valores é: {}".format(mult))
    elif opt == 3:
        if n1 > n2:
            print("O maior desses dois valores é: {}".format(n1))
        elif n2 > n1:
            print("O maior desses dois valores é: {}".format(n2))
        else:
            print("Os dois valores são iguais!")
    elif opt == 4:
        print("Os novos valores são {} e {}".format(n1, n2))
    elif opt == 5:
        print("Programa Encerrado!")
        running = False
    else:
        print("Por favor, digite um número correspondente às opções acima!")
    print("")
