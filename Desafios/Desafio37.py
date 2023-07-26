num = int(input("Digite um número: "))
cod = int(input('''Escolha um número abaixo de conversão:
1 - Binário
2 - Octal
3 - Hexadecimal
Opção: '''))
if cod == 1:
    print("O número {} em binário é {}.".format(num, bin(num)[2:]))
elif cod == 2:
    print("O número {} e octal é {}.".format(num, oct(num)[2:]))
elif cod == 3:
    print("O número {} em hexadecimal é {}.".format(num, hex(num)[2:]))
else:
    print("Por favor, escolha um número dentro das opções pré-determinadas!")
