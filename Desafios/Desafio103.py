def ficha(jogador='', gols=''):
    if jogador == '':
        jogador = '<desconhecido>'
    if gols == '':
        gols = 0
    print(f"O jogador {jogador} fez {gols} gol(s) no campeonato.")

nome = input("Nome do Jogador: ")
gols = input("Numero de Gols: ")

ficha(nome,gols)