lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f"Digite um valor para [{l}, {c}]? "))
        lista[l][c] = n
for l in range(0, 3):
    print()
    for c in range(0, 3):
        print(f'[ {lista[l][c]} ]', end='')

soma_pares = 0
soma_3coluna = 0
for l in lista:
    for p in l:
        if p % 2 == 0:
            soma_pares += p
for c in range(0,3):
    soma_3coluna += lista[c][2]
print()
print(f'\nA soma dos valores pares e {soma_pares}')
print(f'A soma dos valores da terceira coluna e {soma_3coluna}')
print(f'A soma dos valores pares e {max(lista[1])}')
