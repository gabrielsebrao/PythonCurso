from validacao import yesnt

lista = list()
fichario = list()
ficha = dict()

while True:

    ficha['Nome'] = input('Nome do jogador: ')
    partidas = int(input(f"Quantas partidas {ficha['Nome']} jogou? "))

    for i in range(0, partidas):
        lista.append(int((input(f"Quantos gols na partida {i+1}? "))))

    ficha['Gols'] = lista[:]
    ficha['Total'] = sum(lista)
    lista.clear()
    fichacopy = ficha.copy()
    fichario.append(ficha.copy())

    for key, value in fichacopy.items():
        del ficha[key]

    condicao = yesnt()
    if not condicao:
        break

print('-='*40)
print(f'{"Cod":>4} ', end='')
for k in fichacopy.keys():
    print(f'{str(k):<15}', end='')
print()
print('-' * 40)
for pos, dictn in enumerate(fichario):
    print(f'{pos:>4} ', end='')
    for v in dictn.values():
        print(f'{str(v):<15}', end='')
    print()
print('-' * 40)
print()
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if busca == 999:
        break
    if busca >= len(fichario):
        print(f"Nao existe jogador com codigo {busca}.")
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR {fichario[busca]['Nome']}")
        for part, gols in enumerate(fichario[busca]['Gols']):
            print(f'   No jogo {part+1} fez {gols} gols.')
    print('-'*40)
print('<< Volte sempre! >>')
