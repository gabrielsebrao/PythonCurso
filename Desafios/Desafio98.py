from time import sleep

def contagem(inicio, fim, passo):
    print('-=' * 20)
    print(f'De {inicio} ate {fim}, de {passo} em {passo}:')
    sleep(1)
    if inicio > fim:
        if passo > 0:
            while inicio > fim-passo:
                if inicio > fim-1:
                    print(inicio, end=' ')
                    sleep(0.3)
                    inicio -= passo
                else:
                    break
        elif passo < 0:
            while inicio > fim+passo:
                if inicio > fim+1:
                    print(inicio, end=' ')
                    sleep(0.3)
                    inicio += passo
                else:
                    break
        else:
            passo = 1
            while inicio > fim-passo:
                if inicio > fim-1:
                    print(inicio, end=' ')
                    sleep(0.3)
                    inicio -= passo
                else:
                    break
    else:
        if passo == 0:
            passo = 1
            while inicio < fim + passo:
                if inicio < fim+1:
                    print(inicio, end=' ')
                    sleep(0.3)
                    inicio += passo
                else:
                    break
        else:
            while inicio < fim+passo:
                if inicio < fim+1:
                    print(inicio, end=' ')
                    sleep(0.3)
                    inicio += passo
                else:
                    break
    sleep(0.3)
    print("FIM!")
    sleep(0.3)

contagem(1, 10, 1)
contagem(10, 0, 2)

print('-='*20)
print("Agora e sua vez de personalizar a contagem!")
i = int(input("Inicio: "))
f = int(input("Final: "))
p = int(input("Passo: "))
contagem(i, f, p)
