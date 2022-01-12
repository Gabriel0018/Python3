n = int(input('Digite um valor inteiro positivo: '))
print('Os números \033[36mpares\033[m entre 0 e {} são:'.format(n))
for i in range(0,n+1):
    if i % 2 == 0:
        print('{} '.format(i), end = '')
        
print('')
print('')

print('Os números \033[33mímpares\033[m entre 0 e {} são: '.format(n))
for i in range(0,n+1):
    if i % 2 != 0:
        print('{} '.format(i), end = '')