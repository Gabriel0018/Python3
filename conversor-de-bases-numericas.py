# Introdução ao programa

n = int(input('Digite um valor positivo inteiro ou zero para converter a base numérica: '))

while n < 0:
    n = int(input('Insira valores positivos ou zero: '))
    
leitor = int(input("""\033[33m(1)Binário\033[m
\033[36m(2)Octal\033[m
\033[32m(3)Hexadecimal\033[m
Escolha a conversão de base desejada: """))

while leitor < 0 or leitor > 3:
    print('')
    leitor = int(input("""\033[33m(1)Binário\033[m
\033[36m(2)Octal\033[m
\033[32m(3)Hexadecimal\033[m
Escolha a conversão de base desejada: """))

# Binário

if leitor == 1:
    
    sobra = []
    num = n
    
    while num > 0:
        resto = num % 2
        num = num // 2
        sobra.append(resto)

    sobra = sobra[::-1]
    tamanho = int(len(sobra))
    print('{} = '.format(n), end = '')
    
    for i in range (0, tamanho):
        print('{}{}'.format('\033[33m', sobra[i]), end = '')
        i = i + 1

# Octal

elif leitor == 2:
    
    sobra = []
    num = n
    
    while num > 0:
        resto = num % 8
        num = num // 8
        sobra.append(resto)
        
    sobra = sobra[::-1]
    tamanho = int(len(sobra))
    print('{} = '.format(n), end = '')
    
    for i in range (0, tamanho):
        print('{}{}'.format('\033[36m', sobra[i]), end = '')
    
# Hexadecimal

elif leitor == 3:
    print('{} = \033[32m{}'.format(n, hex(n)[2:]), end = '')
    