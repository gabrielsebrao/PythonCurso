nome=input('Qual é o seu nome? ')
nome=nome.strip()
nome_dividido=nome.split()
print('''{}
{}
{} letras ao todo
{} letras no primeiro nome'''.format(nome.upper(),nome.lower(),len(''.join(nome_dividido)),len(nome_dividido[0])))