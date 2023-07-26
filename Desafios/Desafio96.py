def area(comp, larg):
    area = comp * larg
    print(f'A area de um terreno {comp} x {larg} e {area} m²')

print(f'{"Controle de Terrenos":^30}')
print('='*30)
c = float(input("Largura: (m) "))
l = float(input("Comprimento: (m) "))
area(c, l)