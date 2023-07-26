peso = float(input("Qual é o seu peso? "))
altura = float(input("Qual é a sua altura? "))
imc = peso/(altura*altura)
print("Seu IMC e {:.1f}".format(imc))
if imc < 18.5:
    print('Status IMC: Abaixo do Peso.')
elif 18.5 <= imc < 25:
    print('Status IMC: Peso Ideal.')
elif 25 <= imc < 30:
    print('Status IMC: Sobrepeso.')
elif 30 <= imc <= 40:
    print('Status IMC: Obesidade.')
else:
    print('Status IMC: Obesidade Mórbida.')