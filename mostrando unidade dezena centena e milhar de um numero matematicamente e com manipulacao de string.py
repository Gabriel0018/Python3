import sys
n = int(input('Digite um número entre 0 e 9999: '))

if n < 0 or n > 9999:
    print('Número inválido!')
    sys.exit(0)


# Resolvendo com propriedades matemáticas:

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Resolvido matemáticamente')
print('Milhar  = {} \nCentena = {} \nDezena  = {} \nUnidade = {}'.format(m, c, d, u))

print('-=' * 30)

# Resolvendo com propriedades de String:

n = str(n)
n = n.strip().split()
n = ''.join(n)

if len(n) == 1:
    somador = '000'
    n = '000' + n
    n = ' '.join(n)
    n = n.split()
    print('Resolvido como string' )
    print('Milhar  = {} \nCentena = {} \nDezena  = {} \nUnidade = {}'.format(n[0],n[1],n[2],n[3])) 

elif len(n) == 2:
    somador = '00'
    n = '00' + n
    n = ' '.join(n)
    n = n.split()
    print('Resolvido como string')
    print('Milhar  = {} \nCentena = {} \nDezena  = {} \nUnidade = {}'.format(n[0],n[1],n[2],n[3]))

elif len(n) == 3:
    somador = '0'
    n = '0' + n
    n = ' '.join(n)
    n = n.split()
    print('Resolvido como string')
    print('Milhar  = {} \nCentena = {} \nDezena  = {} \nUnidade = {}'.format(n[0],n[1],n[2],n[3]))
    
else: 
    len(n) == 4
    n = ' '.join(n)
    n = n.split()
    print('Resolvido como string')
    print('Milhar  = {} \nCentena = {} \nDezena  = {} \nUnidade = {}'.format(n[0],n[1],n[2],n[3]))








    

