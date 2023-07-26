ficha = dict()
ficha['Nome'] = input("Nome: ")
ficha['Ano'] = int(input("Ano de Nascimento: "))
ficha['Carteira'] = int(input("Carteira de Trabalho: "))
if ficha['Carteira'] != 0:
    ficha['Contratacao'] = int(input("Ano de Contratacao: "))
    ficha['Salario'] = int(input("Salario: "))
print(ficha)
print('-='*30)
for i, j in ficha.items():
    print(f'{i} tem o valor {j}')
