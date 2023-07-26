lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        n = input(f"Digite um valor para [{l}, {c}]? ")
        lista[l][c] = n
for l in range(0, 3):
    print()
    for c in range(0, 3):
        print(f'[ {lista[l][c]} ]', end='')
