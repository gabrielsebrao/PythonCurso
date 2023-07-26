c = int(input("Digite quantos elementos da Sequência de Fibonacci você quer que apareça: "))
n = 0
n2 = 1
n3 = 0
q = 0
while q < c:
    if q == 0:
        print(n3)
    elif q == 1:
        print(n2)
    else:
        n = n3 + n2
        n3 = n2
        n2 = n
        print('{}'.format(n))
    q += 1
