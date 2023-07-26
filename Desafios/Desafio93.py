lista = list()
ficha = dict()

ficha['nome'] = input('Nome do jogador: ')
partidas = int(input(f"Quantas partidas {ficha['nome']} jogou? "))
for i in range(0, partidas):
    lista.append(int((input(f"Quantos gols na partida {i}? "))))
ficha['gols'] = lista[:]
ficha['total'] = sum(lista)

print('-='*30)
print(ficha)
print('-='*30)
for i, j in ficha.items():
    print(f'O campo {i} tem o valor {j}')
print('-='*30)
print(f'O jogador {ficha["nome"]} jogou {len(lista)} partidas.')
for pos, num in enumerate(lista):
    print(f'  => Na partida {pos}, fez {num} gols.')
print(f'Foi um total de {ficha["total"]} gols.')

