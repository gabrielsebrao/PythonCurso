lista = []
condicao = True
for c in range(0, 5):
    n = int(input("Digite um valor: "))
    for i, j in enumerate(lista):
        jJ = j
        iI = i
        if c == 0:
            break
        elif n > j:
            condicao = True
        elif n < j or n == j:
            condicao = False
            lista.insert(iI, n)
            print(f'Adicionado na posicao {iI} da lista...')
            break
    if condicao:
        lista.append(n)
        print(f'Adicionado ao final da lista...')
print('-'*50)
print(f'Os valores digitados em ordem foram {lista}')
