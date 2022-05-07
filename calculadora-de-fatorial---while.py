print('\033[35m=\033[m' * 60)
print('{:^60}'.format('Calculadora de fatorial'))
print('\033[35m=\033[m' * 60)

n = int(input('Valor: '))
fatorial = 1
tot = 0

#Resolvendo com WHILE

while n >= 1:
    fatorial = fatorial * n
    n -= 1
    tot += 1

if n >= 0:    
    print('{}! = {}'.format(n + tot, fatorial))
    
else:
    print('{}! = Não existe'.format(n))
