cidade=input('Digite o nome da sua cidade: ')
cidade_split=cidade.lower().split()
#print(cidade.split())
print('Tem Santo no primeiro nome:','santo' in cidade_split[0])