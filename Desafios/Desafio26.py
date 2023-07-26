frase=input('Escreva qualquer coisa: ').lower().split()
frase=' '.join(frase)
print('''{}
{}
{}'''.format(frase.count('a'),frase.find('a'),frase.rfind('a')))