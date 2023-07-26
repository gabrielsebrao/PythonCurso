mens = "LOJA SUPER BARATÃO"
print('')
print('-' * 20)
print(f'{mens:^20}')
print('-' * 20)
total = mais_mil = preco = preco_barato = 0
produto_barato = ''
count = 0
while True:
    count += 1
    produto = input("Nome do produto: ")
    preco = int(input("Preço: R$"))
    total += preco
    if preco > 1000:
        mais_mil += 1
    if count == 1 or preco < preco_barato:
        preco_barato = preco
        produto_barato = produto
    while True:
        opt = input("Deseja continuar? [S/N]: ").lower().strip()
        if opt in 'sn' and len(opt) == 1:
            break
        else:
            print("Por favor, insira entre [S/N].")
    if opt == 'n':
        break
print(f"O total da compra foi {total}")
print(f"Temos {mais_mil} produtos custando mais do que R$1000,00")
print(f"O produto mais barato foi {produto_barato} que custa R${preco_barato},00")