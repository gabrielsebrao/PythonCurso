listagem = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-'*50)
print('{:^50}'.format('LISTAGEM DE PRECOS'))
print('-'*50)
for it_pc in range(0, len(listagem)):
    if it_pc % 2 == 0:
        print(f'{listagem[it_pc]:.<41}', end='')
    else:
        print(f'R${listagem[it_pc]:>7.2f}')