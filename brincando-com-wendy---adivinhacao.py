import random

print('\033[35m=\033[m' * 78)
print('''Você está brincando de adivinhação com a irmãzinha mais nova de \033[33mBlitz\033[m!
Tente adivinhar, \033[32mentre 0 e 10\033[m, o valor que Wendy pensou''')
print('\033[35m=\033[m' * 78)

leitor = chr(83)

while leitor == chr(83):
    wendy = random.randint(0,10)
    lista = []

    jogador = int(input('1ᵒ palpite: '))
    
    if jogador > wendy:
        print('\033[36mÉ um número menor!\033[m')
        
    elif jogador < wendy:
        print('\033[35mÉ um número maior!\033[m')
        
    while jogador > 10 or jogador < 0:
        jogador = int(input('\033[36m(valores entre 0 e 10)\033[m 1ᵒ palpite: '))
    lista.append(jogador)
    print('{}{}{}'.format('\033[33m', lista, '\033[m'))

    tentativa = 1

    while jogador != wendy:
        tentativa += 1
        jogador = int(input('{}ᵒ palpite: '.format(tentativa)))
    
        while jogador > 10 or jogador < 0:
            jogador = int(input('\033[36m(valores entre 0 e 10)\033[m {}ᵒ palpite: '.format(tentativa)))
    
        while jogador in lista:
            jogador = int(input('(Já tentou esse valor) {}ᵒ palpite: '.format(tentativa)))
    
        lista.append(jogador)
        print('{}{}{}'.format('\033[33m', lista, '\033[m'))
    
        if jogador > wendy:
            print('\033[36mÉ um valor menor!\033[m')
    
        elif jogador < wendy:
            print('\033[35mÉ um valor maior!\033[m')
    
    if tentativa == 1:
        print('-' * 82)
        print('''Parabéns, você adivinhou de primeira o número que Wendy pensou!
(Wendy sorri de aprovação para você. Ela mostra seu ursinho floppy)''')
        print('-' * 82)
        
    elif tentativa < 4:
        print('-' * 82)
        print('''Você adivinhou o número que Wendy pensou depois de {} tentativas!
(Wendy sorri vagamente para você. Ela parece tímida para ser capaz mostrar seu ursinho de pelúcia)'''.format(tentativa))
        print('-' * 82)
        
    elif tentativa < 7:
        print('-' * 82)
        print('''Você adivinhou o número que Wendy pensou depois de {} tentativas!
(Wendy olha com indiferença para você. Ela chama Blitz para ir ao parquinho.)'''.format(tentativa))
        print('-' * 82)
        
    else:
        print('-' * 82)
        print('''...Finalmente adivinhou o número que Wendy pensou depois de {} tentativas!
(Wendy tenta conter a risada pelo seu fracasso como adivinhador! Ela parece feliz)'''.format(tentativa))
        print('-' * 82)
        
    leitor = chr(65)
    while leitor != chr(83) and leitor != chr(78):
        leitor = str(input('Deseja brincar novamente com Wendy? (S/N): ')).upper()
    
    if leitor == chr(83):
        print('-' * 82)
        print('Wendy feliz de poder brincar novamente!')
        print('-' * 82)
        
print('\033[35m=\033[m' * 82)
print('''Wendy estica sua mão para golpear a cabeça de Blitz!
(Ela se despede enquanto seu braço é puxado pelo seu irmão...)''')
print('\033[35m=\033[m' * 82)

