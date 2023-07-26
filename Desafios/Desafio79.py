lista = []
while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Valor duplicado! Nao vou adicionar...')
    else:
        print('Valor adicionador com sucesso...')
        lista.append(n)
    opt = input("Voce quer continuar? [S/N] ").lower().strip()[0]
    if opt == 'n':
        break
print('-'*40)
print(f'Voce digitou os valores: {sorted(lista)}')