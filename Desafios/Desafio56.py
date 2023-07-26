sm = 0
med = 0
im = 0
hm = ''
mqi = 0
for c in range(0,4):
    n = input("Qual e o seu nome? ")
    i = int(input("Qual e a sua idade? "))
    s = int(input('''Qual e o seu sexo? 
[ 1 ] - Masculino
[ 2 ] - Feminino 
Opcao: '''))
    if i > im and s == 1:
        im = i
        hm = n
    if s == 2 and i < 20:
        mqi += 1
    sm += i
    med = sm/4
print("A media de idade entre as 4 pessoas e {:.1f}".format(med))
print("O homem mais velho e o {} e tem {}.".format(hm, im))
print("A quantidade de mulheres com menos de 20 anos e {}".format(mqi))
