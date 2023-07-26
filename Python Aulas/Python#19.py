galera = list()
dado = list()
for c in range(0,3):
    dado.append(input("Nome:"))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()

for pessoa in galera:
    if pessoa[1] >= 18:
        print(f'{pessoa[0]} e maior de idade')
    else:
        print(f'{pessoa[0]} e menor de idade')
