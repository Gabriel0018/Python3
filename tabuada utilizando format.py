n = int(input('Digite um número entre 1 e 10 para calcular a tabuada: '))

while n <= 0 or n > 10:
    n = int(input('Digite um número entre 1 e 10 para calcular a tabuada: '))
    
print(' 1 x {} = {}\n 2 x {} = {}\n 3 x {} = {}\n 4 x {} = {}\n 5 x {} = {}'.format(n,n*1,n,n*2,n,n*3,n,n*4,n,n*5))
print(' 6 x {} = {}\n 7 x {} = {}\n 8 x {} = {}\n 9 x {} = {}\n10 x {} = {}'.format(n,n*6,n,n*7,n,n*8,n,n*9,n,n*10))