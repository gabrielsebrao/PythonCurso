from random import choice
from time import sleep

j1 = int(input("""Escolha Pedra, Papel ou Tesoura!
1 - Pedra
2 - Papel 
3 - Tesoura
Opção: """))
jo = ["Pedra", "Papel", "Tesoura"]
j1 = jo[j1-1]
j2 = choice(jo)
print("JO...")
sleep(1)
print("KEN...")
sleep(1)
print("PO!")
sleep(1)
if j1 == j2:
    print("""Jogador: {}
Computador: {}
EMPATE!""".format(j1,j2))
elif j1 == "Tesoura" and j2 == "Pedra" or j1 == "Pedra" and j2 == "Papel" or j1 == "Papel" and j2 == "Tesoura":
    print("""Jogador: {}
Computador: {}
VITÓRIA DO COMPUTADOR!""".format(j1,j2))
else:
    print("""Jogador: {}
Computador: {}
VITÓRIA DO JOGADOR!""".format(j1, j2))
