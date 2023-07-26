n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))
if n1 > n2 > n3:
    print("O número {} é o maior, e o menor é o {}".format(n1, n3))
elif n1 > n3 > n2:
    print("O número {} é o maior, e o menor é o {}".format(n1, n2))
elif n2 > n1 > n3:
    print("O número {} é o maior, e o menor é o {}".format(n2, n3))
elif n2 > n3 > n1:
    print("O número {} é o maior, e o menor é o {}".format(n2, n1))
elif n3 > n2 > n1:
    print("O número {} é o maior, e o menor é o {}".format(n3, n1))
elif n3 > n1 > n2:
    print("O número {} é o maior, e o menor é o {}".format(n3, n2))
