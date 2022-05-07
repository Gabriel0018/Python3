print('\033[35m=\033[m' * 60)
print('{:^60}'.format('10 primeiros termos de uma PA'))
print('\033[35m=\033[m' * 60)

n = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))

print('{} \033[33m->\033[m '.format(n), end = '')

somador = n
c = 2
while c <= 10:
    somador = somador + r
    print('{} \033[33m->\033[m '.format(somador), end = '')
    c += 1
    
print('\033[33m...\033[m')

cont = int(input('Deseja que o programa mostre mais quantos termos da PA?: '))

c = 1
while cont > 0:
    while c <= cont:
        somador = somador + r
        print('{} \033[33m->\033[m '.format(somador), end = '')
        cont -= 1
    
    print('\033[33m...\033[m', end = '')  
    cont = int(input('\nDeseja que o programa mostre mais quantos termos da PA?: '))
    
print('\033[33mFinal\033[m', end = '')
