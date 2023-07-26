
def arqExiste(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArq(arquivo):
    a = open(arquivo, 'wt+')
    a.close()

def lerArq(arquivo):
    a = open(arquivo, 'rt')
    for linha in a:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        print(f'{dado[0]:<30}{dado[1]:>3} anos')

def cadastrarArq(arquivo, nome='<desconhecido>', idade=0):
    a = open(arquivo, 'at')
    a.write(f'{nome};{idade}\n')
    print(f"Novo registro de {nome} adicionado")
    a.close()


