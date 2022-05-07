n = int(input('Digite um número entre 1 e 9 para efetuar a tabuada: '))

while n < 1 or n > 9:
    n = int(input('Digite um número entre 1 e 9 para efetuar a tabuada: '))
    
for i in range (1,11):
    print('{} x {:^2} = \033[33m{}\033[m'.format(n, i, n * i))
