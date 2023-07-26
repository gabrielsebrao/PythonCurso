mens = "CADASTRE UMA PESSOA"
total_maior = 0
homens = 0
mulheres_menor_20 = 0
while True:
    print('')
    print('-' * 20)
    print(f'{mens:^20}')
    print('-' * 20)
    age = int(input("Idade: "))
    if age > 17:
        total_maior += 1
    while True:
        sex = input("Sexo [M/F]: ").upper().strip()[0]
        if sex == 'M':
            homens += 1
        if sex in 'FM' and len(sex) == 1:
            break
    if sex == 'F' and age < 20:
        mulheres_menor_20 += 1
    while True:
        opt = input("\nVocê quer continuar? [S/N]: ").upper().strip()
        if opt == 'S':
            break
        if opt == 'N':
            break
        elif 'S' != opt != 'N':
            print("Por favor, insira [S/N].")
    if opt == 'N':
        break
print(f"Total de pessoas com mais de 18 anos: {total_maior}")
print(f"Ao todo temos {homens} homens cadastrados.")
print(f"E temos {mulheres_menor_20} mulheres com menos de 20 anos.")
