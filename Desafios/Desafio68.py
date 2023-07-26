from random import randint

print('=-'*25)
mens = 'VAMOS JOGAR PAR OU ÍMPAR'
print(f'{mens:^50}')
print('=-'*25)
count = 0
while True:
    nj = int(input("Diga um valor: "))
    pi = input("Par ou Ímpar [P/I]: ").lower().split()
    pi = ''.join(pi)
    nr = randint(0, 10)
    total = nj + nr
    if pi in "pi" and len(pi) == 1:
        if total % 2 == 0:
            if pi == 'p':
                print('-'*25)
                print(f"Você jogou {nj} e o computador jogou {nr}. Total de {total} DEU PAR")
                print('-'*25)
                print('Você GANHOU!')
                count += 1
            if pi == 'i':
                print('-'*25)
                print(f"Você jogou {nj} e o computador jogou {nr}. Total de {total} DEU ÍMPAR")
                print('-'*25)
                print('Você PERDEU!')
                break
        else:
            if pi == 'p':
                print('-' * 25)
                print(f"Você jogou {nj} e o computador jogou {nr}. Total de {total} DEU PAR")
                print('-' * 25)
                print('Você PERDEU!')
                break

            if pi == 'i':
                print('-' * 25)
                print(f"Você jogou {nj} e o computador jogou {nr}. Total de {total} DEU ÍMPAR")
                print('-' * 25)
                print('Você GANHOU!')
                count += 1
    else:
        print("Escolha entre [P/I], por favor!")
print("GAME OVER! Você ganhou {} vezes.".format(count))
