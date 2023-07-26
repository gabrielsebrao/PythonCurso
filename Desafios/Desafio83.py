expr = input("Digite a expressao: ")
abre = fecha = 0
for simb in expr:
    if simb == '(':
        abre += 1
    elif simb == ')':
        fecha += 1
if abre != fecha or expr.index('(') != 0:
    print('Sua expressao e invalida!')
else:
    print('Sua expressao e valida!')
