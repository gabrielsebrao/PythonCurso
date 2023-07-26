n2 = 0
for c in range(0, 6):
    n = int(input("Digite um numero: "))
    if n % 2 == 0:
        n2 += n
print("A soma dos numeros pares apresentados foi {}".format(n2))
