from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    sleep(1)
    for i in range(0, 5):
        lista.append(randint(1, 10))
        print(lista[i], end=' ')
        sleep(0.3)
    print('PRONTO!')
    sleep(1)

def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores de {lista}, temos {soma}.')

numeros = list()
sorteia(numeros)
somaPar(numeros)
