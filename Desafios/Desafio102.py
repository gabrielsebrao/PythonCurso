from math import factorial
def fatorial(numero, show=False):
    """
    -> Calcula o Fatorial de um numero.
    :param numero: O numero a ser calculado
    :param show: (opicional) Mostrar ou nao a conta
    :return: retorna o valor 'resultado' do fatorial do valor 'n'
    """
    resultado = factorial(numero)
    if show:
        for i in range (1, numero+1):
            print(f"{i} x " if i < numero else f"{i} = ", end='')
    return resultado

print(fatorial(5, show=True))