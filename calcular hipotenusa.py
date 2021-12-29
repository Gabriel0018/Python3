from math import sqrt, pow, hypot
h = float(input('Digite a altura do triângulo retângulo: '))
b = float(input('Digite a base do triângulo retângulo: '))
x = sqrt(pow(h,2) + pow(b,2))
print('-=' * 30)
print('hipotenusa = {:.2f}'.format(x))
print('-=' * 30)
print('hipotenusa = {:.2f}'.format(hypot(h,b)))
