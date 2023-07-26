from Desafios.validacao import yesnt

ficha = dict()
lista = list()
opt = ' '
while True:

    sexo = ' '
    ficha['Nome'] = input("Nome: ")
    ficha['Idade'] = int(input("Idade: "))

    while sexo not in 'mf':
        sexo = input("Sexo: [M/F] ").lower().strip()[0]
        if sexo not in 'mf':
            print("ERRO! Responda apenas com M ou F.")
        else:
            ficha['Sexo'] = sexo

    lista.append(ficha.copy())
    del ficha['Nome']
    del ficha['Idade']
    del ficha['Sexo']

    condicao = yesnt()
    if not condicao:
        break

print('-='*30)
print(f'A) Ao todo temos {len(lista)} cadastradas.')

soma = 0
for dictn in lista:
    soma += dictn['Idade']
media = soma/len(lista)
print(f'B) A media de idade e de {media}')

print('C) As mulheres cadastradas foram: ', end='')
for dictn in lista:
    if dictn['Sexo'] == 'f':
        if dictn == lista[len(lista)-1]:
            print(dictn['Nome'],'.')
        else:
            print(dictn['Nome'], end=', ')\

print()
print('D) Lista das pessoas que estao acima da media: ')
for dictn in lista:
    if dictn['Idade'] > media:
        print(f'nome = {dictn["Nome"]}; idade = {dictn["Idade"]}; sexo = {dictn["Sexo"]}')
