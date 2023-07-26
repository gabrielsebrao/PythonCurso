from random import choice
a = input("Digite o nome de um aluno: ")
b = input("Digite o nome de um aluno: ")
c = input("Digite o nome de um aluno: ")
d = input("Digite o nome de um aluno: ")
lista = [a, b, c, d]
ran = choice(lista)
print("O aluno escolhido foi {}.".format(ran))
