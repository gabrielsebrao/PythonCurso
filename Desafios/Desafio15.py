d = int(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))
dp = d*60
kmp = km*0.15
print("O total a pagar é R${:.2f}".format(dp+kmp))
