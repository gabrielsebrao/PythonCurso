f = True
while f:
    sex = input("Qual é o seu sexo? M/F ").upper().strip()
    if sex == 'M' or sex == 'F':
        print("Ok, voce selecionou {}.".format(sex))
        f = False
    else:
        print("Digite novamente!\n")
