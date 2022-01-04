n1 = int(input('\033[33mPrimeiro valor: '))
n2 = int(input('\033[36mSegundo valor:  '))

if n1 > n2:
    print('\033[mValor maior = \033[33m{}\033[m'.format(n1))
    print('Valor menor = \033[36m{}\033[m'.format(n2))
    
elif n1 == n2:
    print('\033[mOs valores são iguais \033[33m{}\033[m = \033[36m{}\033[m'.format(n1, n2))

else:
    print('\033[mValor maior = \033[36m{}\033[m'.format(n2))
    print('Valor menor = \033[33m{}\033[m'.format(n1))