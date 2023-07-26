def notas(*num, sit=False):
    """
    -> Funcao para analisar notas e situacoes de varios alunos
    :param num: (aceita 1 ou mais) notas dos alunos
    :param sit: (opcional) situacao da media dos alunos, True para mostrar e False para nao mostrar
    :return: dicionario com dados da turma
    """
    soma = 0
    nota = dict()
    media = soma / len(num)
    nota['Maior'] = max(num)
    nota['Menor'] = min(num)
    nota['Media'] = media
    nota['Total'] = len(num)
    if sit:
        if media >= 7:
            nota['Situacao'] = 'BOA'
        elif 6 <= media < 7:
            nota['Situacao'] = 'RAZOAVEL'
        else:
            nota['Situacao'] = 'RUIM'
    return nota

resp = notas(10, 2, sit=True)
print(resp)

