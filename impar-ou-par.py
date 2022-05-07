import random
from time import sleep

print('\033[35m=\033[m' * 60)
print('{:^80}'.format('Brincando com Blitz em: \033[36mPar\033[m ou \033[32mÍmpar\033[m'))
print('\033[35m=\033[m' * 60)

c = 0

while True:
    n = int(input('Digite um valor: '))
    leitor = str(input('\033[36mPar\033[m ou \033[32mÍmpar\033[m? [P/I]: ')).upper()
    
    while leitor != chr(80) and leitor != chr(73):
        leitor = str(input('\033[36mPar\033[m ou \033[32mÍmpar\033[m? [P/I]: ')).upper()

    blitz = random.randint(0,100)

    soma = n + blitz

    if leitor == chr(80) and soma % 2 == 0:
        c = c + 1
        print('-' * 60)
        sleep(0.85)
        print('''Blitz escolheu o número \033[34m{}\033[m e você escolheu o número \033[35m{}\033[m
soma = {} -> \033[36mPar\033[m
\033[33mVenceu!\033[m'''.format(blitz, n, soma))
        print('-' * 60)
    
    elif leitor == chr(73) and soma % 2 == 1:
        c = c + 1
        print('-' * 60)
        sleep(0.85)
        print('''Blitz escolheu o número \033[34m{}\033[m e você escolheu o número \033[35m{}\033[m 
soma = {} -> \033[32mÍmpar\033[m
\033[33mVenceu!\033[m'''.format(blitz, n, soma))
        print('-' * 60)
    
    elif leitor == chr(80) and soma % 2 == 1:
        print('-' * 60)
        sleep(0.85)
        print('''Blitz escolheu o número \033[34m{}\033[m e você escolheu o número \033[35m{}\033[m  
soma = {} -> \033[32mÍmpar\033[m
Você \033[31mperdeu\033[m após {} vitórias consecutivas'''.format(blitz, n, soma, c))
        print('-' * 60)
        break
    
    else:
        print('-' * 60)
        sleep(0.85)
        print('''Blitz escolheu o número \033[34m{}\033[m e você escolheu o número \033[35m{}\033[m
soma = {} -> \033[36mPar\033[m
Você \033[31mperdeu\033[m após {} vitórias consecutivas'''.format(blitz, n, soma, c))
        print('-' * 60)
        break
    