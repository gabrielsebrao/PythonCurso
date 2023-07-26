print('-'*15+'CALCULADORA DE FATORIAL'+'-'*15)
n = int(input("Digite um valor: "))
no = n
n1 = 1
for i in range(n, 1, -1):
    n1 = n1 * i

'''while n > 1:
    n1 = n1 * n
    n -= 1'''

print("{}! = {}".format(no, n1))
