def yesnt():
    """
    -> Faz uma pergunta de validacao de sim ou nao em looping ate o usuario acertar 's' ou 'n'.
    :return: retorna a condicao de validacao
    """
    condicao = True
    while True:
        opt = input("Voce quer continuar? [S/N] ").lower().strip()
        if opt in 'sn' and len(opt) == 1:
            break
        else:
            print('ERRO! Digite S ou N.')
    if opt == 'n':
        condicao = False
    return condicao

def leiaInt(string):
    while True:
        try:
            numero = int(input(string))
        except ValueError:
            print("ERRO! Por favor, digite um numero inteiro valido.")
        else:
            break
    return numero