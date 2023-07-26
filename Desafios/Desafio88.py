from random import randint
from time import sleep


print('='*40)
print('{:^40}'.format('JOGO DA MEGA SENA'))
print('='*40)
n = int(input("Quantos jogos voce quer que eu sorteie? "))
lista = []
for c in range(1, n+1):
    for d in range(0, 6):
        lista.append(randint(1,60))
    print(f'Jogo {c}: {lista}')
    lista.clear()
    sleep(0.5)