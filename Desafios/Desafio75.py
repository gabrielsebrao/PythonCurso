n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
n3 = int(input("Digite mais um valor: "))
n4 = int(input("Digite o ultimo valor: "))
num = (n1, n2, n3, n4)

print('Voce digitou os valores',num)

print(f'O valor 9 apareceu {num.count(9)} vezes')

if 3 not in num:
    print("O numero 3 nao foi digitado em nenhuma posicao.")
else:
    print(f'O valor 3 foi digitado na posicao {num.index(3)}')

count = 0
for n in num:
    if n % 2 == 0:
        print(f'{n}', end=' ')
        count += 1
if count == 0:
    print("Nao ha numeros pares!")
