n = int(input("Digite um numero para saber sua tabuada: "))
print("TABUADE DE {}".format(n))
for a in range(0, 11):
    print("{} x {} = {}".format(n, a, n*a))
