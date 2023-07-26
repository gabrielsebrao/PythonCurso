lista = [2, 4, 5, 2, 2, 1]
print(lista)
lista.insert(1, 't')
while True:
    if 2 in lista:
        lista.remove(2)
    else:
        break
print(lista)
