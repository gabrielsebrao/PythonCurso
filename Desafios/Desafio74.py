from random import randint
# n1 = randint(0, 9)
# n2 = randint(0, 9)
# n3 = randint(0, 9)
# n4 = randint(0, 9)
# n5 = randint(0, 9)
numeros = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))
maior = menor = 0
print(f'Os valores sorteados foram: ', end='')
for c in range(0,5):
    print(numeros[c], end=' ')
    # if c == 0:
    #     maior = c
    #     menor = c
    # if numeros[c] > numeros[maior]:
    #     maior = c
    # if numeros[c] < numeros[menor]:
    #     menor = c
print("")
print(f'''O maior valor sorteado foi: {max(numeros)}
O menor valor sorteado foi {min(numeros)}''')
