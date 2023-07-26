frase = input("Digite uma frase: ").lower().split()
frasej = ''.join(frase)
n = True
for i in range(0, len(frasej)//2):
    l = frasej[i]
    if l == frasej[len(frasej)-i-1]:
        n = True
    else:
        n = False
    if not n:
        break
if n:
    print("Este é um palíndromo!")
else:
    print("Este não é um palíndromo...")

# Também dá para usar o inverso usando 'inverso = frase[::-1]'
