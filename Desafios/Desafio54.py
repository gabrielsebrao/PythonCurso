from datetime import date

mn = 0
mm = 0
for c in range(1,8):
    nasc = int(input("Em que ano voce nasceu? "))
    if date.today().year - nasc < 18:
        mn += 1
    else:
        mm += 1
print("Dentre as sete pessoas, temos {} que atinjiram a maioridade, e {} que ainda sao menores.".format(mm, mn))

