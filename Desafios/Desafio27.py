nome=input('Digite seu nome completo: ')
nome_s=nome.split()
print('''Primeiro nome: {} 
Último nome: {}'''.format(nome_s[0],nome_s[len(nome_s)-1]))