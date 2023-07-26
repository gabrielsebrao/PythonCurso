mens = "BANCO CEV"
print('='*20)
print(f'{mens:^20}')
print('='*20)
valor = int(input("Que valor você quer retirar? R$"))
notas_50 = valor//50
notas_20 = valor//20
notas_10 = valor//10
notas_1 = valor//1
count = 1
n = 50
while True:
    notas_50 = valor // 50
    notas_20 = valor // 20
    notas_10 = valor // 10
    notas_1 = valor // 1
    if valor >= 50:
        print(f"Total de {notas_50} notas de R$50,00")
        valor -= notas_50*50
    elif valor >= 20:
        print(f"Total de {notas_20} notas de R$20,00")
        valor -= notas_20*20
    elif valor >= 10:
        print(f"Total de {notas_10} notas de R$10,00")
        valor -= notas_10*10
    elif valor >= 1:
        print(f"Total de {notas_1} notas de R$1,00")
        valor -= notas_1*1
    else:
        break
print('='*20)
print("Volte sempre ao BANCO CEV! Tenha um bom dia!")