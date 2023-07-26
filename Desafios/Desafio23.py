numero=int(input('Digite um número entre 0 a 9999: '))
print('''Milhar: {}
Centena: {}
Dezena: {}
Unidade: {}'''.format(numero//1000,numero//100-((numero//1000)*10),numero//10-((numero//100)*10),numero//1-((numero//10)*10)))
