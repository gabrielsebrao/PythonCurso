n1 = int(input("Digite sua primeira nota: "))
n2 = int(input("Digite sua segunda nota: "))
media = (n1+n2)/2
print("Sua média foi {:.1f}".format(media))
if media < 5:
    print("REPROVADO")
elif media >= 7:
    print("APROVADO")
else:
    print("RECUPERAÇÃO")