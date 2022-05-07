print('Os números dos numeros ímpares que são múltiplos de três e que se encontram no intervalo de 0 até 500:\n')
contador = 0
soma = 0
for i in range (1, 501):
    if i % 2 != 0:
        if i % 3 == 0:
            contador = contador + 1
            soma = soma + i
            print('{}'.format(i), end = ' ')
        
print('\n\nSoma dos {} valores = \033[33m{}\033[m'.format(contador ,soma))
