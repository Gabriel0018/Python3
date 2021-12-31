a1 = float(input('Primeira reta: '))
a2 = float(input('Segunda reta:  '))
a3 = float(input('Terceira reta: '))

if a1 + a2 > a3 and a1 + a3 > a2 and a2 + a3 > a1:
    print('É possível formar um triângulo com três retas!')

else:
    print('Não é possível formar um triângulo com as três retas')