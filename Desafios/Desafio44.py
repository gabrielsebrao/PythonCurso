preco = int(input("Digite o valor do produto: R$"))
escolha = int(input("""Escolha a opção de pagamento desejada: 
1 - Dinheiro/Cheque
2 - À Vista no Cartão
3 - 2x no Cartão
4 - 3x no Cartão 
Opção: """))
if escolha == 1:
    print("Desconto de 10% aplicado! O seu produto custa agora R${:.2f}".format(preco*0.9))
elif escolha == 2:
    print("Desconto de 5% aplicado! O seu produto custa agora R${:.2f}".format(preco * 0.95))
elif escolha == 3:
    print("Sem descontos aplicados! O seu produto custará R${:.2f}".format(preco))
elif escolha == 4:
    print("Juros de 20% aplicado! O seu produto custa agora R${:.2f}".format(preco * 1.2))
else:
    print("Por favor, escolha dentro das opções pré-deterinadas!")