while True:
    num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'cartoze', 'quinze', 'dezesseis', 'dezessete','dezoito', 'dezenove', 'vinte')
    n = int(input("Digite um número entre 0 a 20: "))
    if n > 20 or n < 0:
        print("Tente novamente!")
    else:
        print(f'Você digitou o número {num[n]}.')
        break
