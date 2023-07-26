from operator import itemgetter
from random import randint

jogadores = dict()
jogadores['Jogador1'] = randint(1, 6)
jogadores['Jogador2'] = randint(1, 6)
jogadores['Jogador3'] = randint(1, 6)
jogadores['Jogador4'] = randint(1, 6)

for i, j in jogadores.items():
    print(f'{i} tirou {j} no dado.')

print('-='*15)
print(f'{"== RANKING DO JOGO ==":^30}')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for pos, tup in enumerate(ranking):
    print(f'  {pos+1}° lugar: {tup[0]} com {tup[1]}.')


