print('\033[35m=\033[m' * 60)
print('{:^60}'.format('Super tabuada! Valor negativo sai programa'))
print('\033[35m=\033[m' * 60)

i = 1
n = int(input('Deseja ver a tabuada de qual valor?: '))

while n >= 0:
    print('-' * 60)
    
    for i in range (1,11):
        multiplicacao = n * i
        print('{} x {:<2} = {:<2}'.format(n, i, multiplicacao))
        
    print('-' * 60)
    
    n = int(input('Deseja ver a tabuada de qual valor?: '))
