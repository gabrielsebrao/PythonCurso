n = int(input("Digite um numero: "))
i = 0
for c in range(1, n+1):
    if n % c == 0:
        i += 1
if i == 2:
    print("O numero {} e primo!".format(n))
else:
    print("O numero {} nao e primo!".format(n))
