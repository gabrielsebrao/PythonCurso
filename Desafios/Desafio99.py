from time import sleep

def maior(* num, vazio=False):
    print('=-' * 35)
    print("Analisando os valores passados...")
    sleep(1)
    if vazio:
        print(f'Foram analisados 0 valores ao todo.')
        print(f'O maior valor informado foi 0')
        sleep(1)
    else:
        for n in num:
            print(n, end=' ')
            sleep(0.3)
        print(f'Foram analisados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(vazio=True)