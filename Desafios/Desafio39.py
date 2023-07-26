from datetime import date

ano = int(input("Em que ano você nasceu? "))
ano_atual = date.today().year
if ano_atual - ano < 18:
    print("Você ainda vai se alistar no exército!")
    print("Falta {} ano(s) para você se alistar.".format(18 - (ano_atual - ano)))
elif ano_atual - ano > 18:
    print("Já passou do teu tempo de alistamento!")
    print("Já passou {} ano(s) do prazo.".format(ano_atual - ano - 18))
else:
    print("É hora de se alistar!")
