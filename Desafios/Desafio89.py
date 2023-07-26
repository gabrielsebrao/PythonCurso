lista = []
opt = ' '
while True:
    nome = (input('Nome: '))
    nota1 = (int(input('Nota 1: ')))
    nota2 = (int(input('Nota 2: ')))
    media = (nota1 + nota2)/2
    lista.append([nome, [nota1, nota2], media])
    while opt not in 'sn':
        opt = input('Quer continuar? [S/N] ').lower().strip()[0]
    if opt == 'n':
        break
    else:
        opt = ' '
print('='*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>16}')
print('='*30)
for i, j in enumerate(lista):
    print(f'{i:<4}{j[0]:<10}{j[2]:>16}')
print('='*30)
op = 0
while op != 999:
    op = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if op == 999:
        print('Finalizando...')
        print('<<<VOLTE SEMPRE>>>')
    else:
        print(f'Notas de aluno {lista[op][0]} sao {lista[op][1]}')
