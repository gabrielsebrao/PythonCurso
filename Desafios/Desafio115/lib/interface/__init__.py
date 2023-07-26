from Desafios.Desafio115.lib.arquivo import *
from Desafios.validacao import *
def linha(tam=42):
    return '—' * tam

def cabecalho(texto, tam=42):
    print(linha(tam))
    print(texto.center(tam))
    print(linha(tam))

def menu(*opt, tam=42):
    cabecalho("MENU PRINCIPAL", tam)
    for i in range(1, len(opt)+1):
        print(f"[  \033[33m{i}\033[m  ] - \033[34m{opt[i-1]}\033[m")
    print(linha(tam))
    while True:
        try:
            resp = int(input("\033[32mSua opcao:\033[m "))
        except ValueError:
            print('ERRO! Por favor, digite um valor inteiro valido.')
        else:
            break
    return resp

def pessoasCadast(arquivo):
    cabecalho("PESSOAS CADASTRADAS")
    lerArq(arquivo)

def novoCadast(arq):
    cabecalho("NOVO CADASTRO")
    nome = input("\033[32mNome:\033[m ")
    idade = leiaInt("\033[32mIdade:\033[m ")
    cadastrarArq(arq, nome, idade)
