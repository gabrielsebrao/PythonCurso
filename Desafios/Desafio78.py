numeros = []
posm = posn = 0

for n in range(0, 5):
    numeros.append(int(input(f"Digite um valor para a Posicao {n}: ")))
print(f'Voce digitou os valores: {numeros}')

print(f'O maior valor digitado foi {max(numeros)} nas posicoes ', end='')
for p, num in enumerate(numeros):
    if max(numeros) == num:
        print(p, end='... ')

print('')

print(f'O menor valor digitado foi {min(numeros)} nas posicoes ', end='')
for p, num in enumerate(numeros):
    if min(numeros) == num:
        print(p, end='... ')