soma_par = 0
soma_impar = 0
numero = ['Primeiro','Segundo','Terceiro','Quarto','Quinto','Sexto']

print('Digite 6 valores inteiros \033[35mpositivos\033[m para calcular a soma dos números \033[36mpares\033[m e dos números \033[33mímpares\033[m ')

for i in range (0,6):
    n = int(input('{} número: '.format(numero[i])))
    
    while n < 0:
        n = int(input('\033[35m{} número: \033[m'.format(numero[i])))
    
    if n % 2 == 0:
        soma_par = soma_par + n
    
    else:
        soma_impar = soma_impar + n
        
print('Soma dos valores \033[36m pares\033[m  = {}'.format(soma_par))
print('Soma dos valores \033[33mímpares\033[m = {}'.format(soma_impar))