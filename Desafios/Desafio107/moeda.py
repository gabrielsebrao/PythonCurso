def metade(numero, format):
    met = numero/2
    if format:
        corrigido = "R${:.2f}".format(met)
        return corrigido
    else:
        return met

def dobro(numero, format):
    dob = numero*2
    if format:
        corrigido = "R${:.2f}".format(dob)
        return corrigido
    else:
        return dob

def aumentar(numero, porcentagem, format):
    resultado = numero * (1+porcentagem/100)
    if format:
        corrigido = "R${:.2f}".format(resultado)
        return corrigido
    else:
        return resultado

def diminuir(numero, porcentagem, format):
    resultado = numero * (1-porcentagem/100)
    if format:
        corrigido = "R${:.2f}".format(resultado)
        return corrigido
    else:
        return resultado

def moeda (valor):
    corrigido = "R${:.2f}".format(valor)
    return corrigido

def resumo(numero, porcent1, porcent2):
    print("-"*35)
    print(f"{'RESUMO DO VALOR':^35}")
    print("-" * 35)
    print(f"  Preco analisado: {numero:>13}")
    print(f"  Dobro do preco: {metade(numero, True):>14}")
    print(f"  Metade do preco: {dobro(numero, True):>13}")
    print(f"  {porcent1}% de aumento: {aumentar(numero, porcent1, True):>14}")
    print(f"  {porcent2}% de reducao: {aumentar(numero, porcent2, True):>14}")
    print("-" * 35)
