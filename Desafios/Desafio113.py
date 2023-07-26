def leiaInt(string):
    while True:
        try:
            numero = int(input(string))
        except ValueError:
            print("ERRO! Por favor, digite um numero inteiro valido.")
        else:
            break
    return numero

def leiaFloat(string):
    while True:
        try:
            numero = float(input(string))
        except ValueError:
            print("ERRO! Por favor, digite um numero inteiro valido.")
        else:
            break
    return numero

i = leiaInt("Digite um numero: ")
f = leiaFloat("Digite um numero: ")
print(f"O valor inteiro digitado foi {i} e o valor real foi {f}")
