from time import sleep
from lib.arquivo import *
from lib.interface import *

arq = 'listadepessoas.txt'
if not arqExiste(arq):
    criarArq(arq)
    print(f"Arquivo \033[34m{arq}\033[m criado com sucesso!")

while True:
    resposta = menu("Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema")
    if resposta == 1:
        pessoasCadast(arq)
        sleep(2)
    elif resposta == 2:
        novoCadast(arq)
        sleep(2)
    elif resposta == 3:
        cabecalho("Saindo do sistema... Ate logo!")
        break
    else:
        print("ERRO! Por favor, digite uma opcao valida.")
        sleep(2)
