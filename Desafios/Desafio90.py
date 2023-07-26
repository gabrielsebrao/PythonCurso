ficha = dict()

ficha['nome'] = input("Nome: ")
ficha['media'] = int(input(f"Media de {ficha['nome']}: "))
if ficha['media'] > 6:
    ficha['situacao'] = "Aprovado"
else:
    ficha['situacao'] = "Repovrado"
print(f'Nome e igual a {ficha["nome"]}')
print(f'Media e igual a {ficha["media"]}')
print(f'Situacao e igual a {ficha["situacao"]}')
