n1=int(input("Digite sua primeira nota: "))
n2=int(input("Digite sua segunda nota: "))
m=(n1+n2)/2
print("Sua média foi {:.1f}".format(m))
print("Parabéns!!! Você passou!" if m >=6 else "Que pena, você não passou...")
#if m >= 6:
#    print("Parabéns!!! Você passou!")
#else:
#    print("Que pena, você não passou...")