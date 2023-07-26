from random import randint
n=int(input("Adivinhe um número entre 0 e 5: "))
n1=randint(0,5)
print("Parabéns, você adivinhou o número correto!" if n == n1 else "Você errou! Era {}".format(n1))