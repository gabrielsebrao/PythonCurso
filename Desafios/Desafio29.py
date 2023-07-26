velocidade=int(input("Qual é a velocidade atual do carro? "))
if velocidade > 80:
    print("Você foi multado! Terá que pagar R${},00".format((velocidade-80)*7))
else:
    print("Parabéns! Você está dentro dos limites de velocidade no trânsito.")