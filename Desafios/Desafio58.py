from random import randint

n = -1
r = randint(0, 100)
cont = 0
while n != r:
    n = int(input("Digite um valor: "))
    cont += 1
    if n > r:
        print("Menos... Tente novamente!")
    if n < r:
        print("Mais... Tente novamente!")
print("Parabéns, você acertou depois de {} tentativas!".format(cont))
