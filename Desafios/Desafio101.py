from datetime import date

def voto(anonasc):
    ano = date.today().year
    idade = ano - anonasc
    if 18 > idade >= 16 or idade >= 65:
        condicao = 'VOTO OPCIONAL'
    elif idade < 18:
        condicao = 'NEGADO'
    else:
        condicao = 'VOTO OBRIGATORIO'
    return condicao, idade

ano = int(input("Em que ano voce nasceu? "))
voto = voto(ano)
print(f'Com {voto[1]} anos: {voto[0]}.')