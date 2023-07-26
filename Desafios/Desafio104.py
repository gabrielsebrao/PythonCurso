def leiaInt(string):
    while True:
        numero = input(string)
        if numero.isnumeric():
            break
        else:
            print("ERRO! Digite um numero inteiro valido.")
    return numero

n = leiaInt("Digite um numero: ")
print(f"Voce acabou de digitar o numero {n}.")
