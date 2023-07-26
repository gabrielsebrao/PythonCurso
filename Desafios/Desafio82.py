lista = []
lista_i = []
lista_p = []
opt = ' '
while True:
    lista.append(int(input('Digite um valor: ')))
    while opt not in 'sn':
        opt = input('Quer continuar? [S/N] ').lower().strip()[0]
    if opt == 'n':
        break
    else:
        opt = ' '

for num in lista:
    if num % 2 == 0:
        lista_p.append(num)
    else:
        lista_i.append(num)
    lista_p.sort()
    lista_i.sort()
lista.sort()
print(f'A lista completa e {lista}')
print(f'A lista de pares e {lista_p}')
print(f'A lista de impares e {lista_i}')
