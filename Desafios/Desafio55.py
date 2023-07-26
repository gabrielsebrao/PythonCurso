p = 0
pm = 0
pn = 0
for c in range(0,5):
    p = int(input("Qual e o seu peso? "))
    if c == 0:
        pm = p
        pn = p
    else:
        if p > pm:
            pm = p
        if p < pn:
            pn = p
print("O maior peso foi de {}".format(pm))
print("O menor peso foi de {}".format(pn))




