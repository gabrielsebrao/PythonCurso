lista = []
opt = ' '
while True:
    lista.append(int(input('Digite um valor: ')))
    while opt not in 'sn':
        opt = input('Quer continuar? [S/N] ').lower().strip()[0]
    if opt == 'n':
        break
    else:
        opt = '  '

lista.sort(reverse=True)
print('-'*50)
print(f'Voce digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente e {lista}')
print(f'O valor 5 faz parte da lista!' if 5 in lista else 'O valor 5 nao foi encontrado na lista!')
