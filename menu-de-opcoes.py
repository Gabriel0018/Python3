print('\033[35m=\033[m' * 92)
print('Digite dois valores inteiros e o número correspondente no \033[34mMenu\033[m para realizar as operações')
print('\033[35m=\033[m' * 92)

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

print('\033[34m=\033[m' * 88)
leitor = int(input('''\033[31m[1]\033[mSomar
\033[32m[2]\033[mMultiplicar
\033[33m[3]\033[mMaior
\033[35m[4]\033[mNovos números
\033[36m[5]\033[mSair do programa
Opção: '''))

while leitor > 5 or leitor < 1:
    leitor = int(input('Opção: '))
print('\033[34m=\033[m' * 88)

while leitor != 5:
    if leitor == 1:
        print('\033[31mSoma -> {} + {} = {}'.format(n1, n2, n1 + n2))
    
    elif leitor == 2:
        print('\033[32mMultiplicação -> {} x {} = {} '.format(n1, n2, n1 * n2))
    
    elif leitor == 3:
        if n1 > n2:
            print('\033[33mMaior = {} > {} = {} '.format(n1, n2, n1))
        elif n1 == n2:
            print('\033[33mOs dois possuem o mesmo valor')
        else:
            print('\033[33mMaior = {} < {} = {} '.format(n1, n2, n2))
    else:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        
    leitor = int(input('''\033[31m[1]\033[mSomar
\033[32m[2]\033[mMultiplicar
\033[33m[3]\033[mMaior
\033[35m[4]\033[mNovos números
\033[36m[5]\033[mSair do programa
Opção: '''))
    while leitor > 5 or leitor < 1:
        leitor = int(input('Opção: '))
    print('\033[34m=\033[m' * 88)
