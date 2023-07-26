preco=int(input("Qual é o valor da casa? "))
salario=int(input("Qual é o teu salário? "))
anos=int(input("Por quantos anos você pagará essa prestação? "))
parcela_mensal = (preco/anos)/12
print("Sua parcela mensal será de {:.2f}".format(parcela_mensal))
if parcela_mensal > 1.3*parcela_mensal:
    print("Como excede 30% do teu salário atual, seu empréstimo será negado!".format(parcela_mensal))
else:
    print("Parabéns! Seu empréstimo foi aprovado.".format(parcela_mensal))