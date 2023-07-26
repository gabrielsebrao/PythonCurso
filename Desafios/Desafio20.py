import random
a = input("Digite o nome de um aluno: ")
b = input("Digite o nome de um aluno: ")
c = input("Digite o nome de um aluno: ")
d = input("Digite o nome de um aluno: ")
lista = [a, b, c, d]
random.shuffle(lista)
print("A lista de alunos será: ")
print(lista)
