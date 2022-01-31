print('\033[35m=\033[m' * 60)
print('{:^60}'.format('Somador de valores - FLAG: 999'))
print('\033[35m=\033[m' * 60)

n = soma = 0
lista = []
while n != 999:
    n = int(input('Digite um valor (999 para parar):  '))
    
    if n == 999:
        break
    
    lista.append(n)
    soma = soma + n

print(f'Valores digitados = \033[33m{lista}\033[m')    
print(f'Soma dos valores = \033[36m{soma}\033[m')