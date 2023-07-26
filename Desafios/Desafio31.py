km=int(input("Quanto quilômetros dessa viagem? "))
if km > 200:
    print("A sua passagem custará R${:.2f}".format(km*0.45))
else:
    print("A sua passagem custará R${:.2f}".format(km*0.5))