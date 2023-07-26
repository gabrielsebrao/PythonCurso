from datetime import date
ano = int(input("Qual é o seu ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano
if idade <= 9:
    modalidade = 'mirim'
elif 9 < idade <= 14:
    modalidade = 'infantil'
elif 14 < idade <= 19:
    modalidade = 'junior'
elif idade == 20:
    modalidade = 'sênior'
else:
    modalidade = 'master'
print("Sua modalidade de atleta é {}.".format(modalidade))