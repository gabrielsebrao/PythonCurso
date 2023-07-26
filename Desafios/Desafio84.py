lista = list()
dado = list()
lista_maiores = list()
lista_menores = list()
opt = ' '
maior_peso = menor_peso = 0

while True:
    dado.append((input('Nome: ')))
    dado.append(int(input('Peso: ')))
    lista.append(dado[:])
    dado.clear()
    while opt not in 'sn':
        opt = input('Quer continuar? [S/N] ').lower().strip()[0]
    if opt == 'n':
        break
    else:
        opt = ' '

for pessoa, peso in lista:
    if pessoa == lista[0][0]:
        maior_peso = peso
        menor_peso = peso
    elif peso > maior_peso:
        maior_peso = peso
    else:
        menor_peso = peso

for cadastro in lista:
    if cadastro[1] == maior_peso:
        lista_maiores.append(cadastro[0])
    elif cadastro[1] == menor_peso:
        lista_menores.append(cadastro[0])

print(f'Ao todo, voce cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {maior_peso}. Peso de {lista_maiores}')
print(f'O menor peso foi de {menor_peso}. Peso de {lista_menores}')