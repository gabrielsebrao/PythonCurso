ficha = dict()
pessoas = list()
opt = ' '

while True:
    ficha['Nome'] = input("Nome: ")
    ficha['Idade'] = int(input("Idade: "))
    ficha['Sexo'] = input("Sexo: [M/F] ")
    pessoas.append(ficha.copy())
    while opt not in 'sn':
        opt = input('Quer continuar? [S/N] ').lower().strip()[0]
    if opt == 'n':
        break
    else:
        opt = ' '

print(ficha)