from math import radians, cos, sin, tan
a = float(input("Digite um ângulo: "))
sin = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))
print("O seno de {}° é {}".format(a, sin))
print("O cosseno de {}° é {}".format(a, cos))
print("A tangente de {}° é {}".format(a, tan))
