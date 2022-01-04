import random
from time import sleep

leitor = chr(115)

while leitor == chr(115) or leitor == chr(83):
    blitz = random.randint(1,3)
    jogador = int(input("""Blitz feliz de poder brincar com você!
\033[32m(1)Pedra\033[m
\033[33m(2)Papel\033[m
\033[36m(3)Tesoura\033[m
Blitz deseja brincar de jokenpô com você! Escolha o número correspondente: """))

    while jogador < 1 or jogador > 3:
        print('')
        jogador = int(input("""Blitz feliz de poder brincar com você!
\033[32m(1)Pedra\033[m
\033[33m(2)Papel\033[m
\033[36m(3)Tesoura\033[m
Blitz deseja brincar de jokenpô com você! Escolha o número correspondente: """))
    
    print('')
    print('Jo')
    sleep(1)
    print('ken')
    sleep(1)
    print('pô!')
    sleep(1)

    if jogador == blitz and jogador == 1:
        print('')
        print("""Você e Blitz escolheram \033[32mPedra!\033[m Foi um empate
(Blitz dá soquinhos em sua mão)""")

    if jogador == blitz and jogador == 2:
        print('')
        print("""Você e Blitz escolheram \033[33mPapel!\033[m Foi um empate
(Blitz envolve suas mãos como uma luva)""")

    if jogador == blitz and jogador == 3:
        print('')
        print("""Você e Blitz escolheram \033[36mTesoura!\033[m Foi um empate
(Blitz fica dançando em posição de V com as mãos)""")

    elif jogador == 1 and blitz == 2:
        print('')
        print("""Você escolheu \033[32mPedra\033[m e Blitz escolheu \033[33mPapel.\033[m Você perdeu!!
(Blitz embrulha uma pedra em um papel de presente e dâ para você!)""")

    elif jogador == 1 and blitz == 3:
        print('')
        print("""Você escolheu \033[32mPedra\033[m e Blitz escolheu \033[36mTesoura.\033[m Você venceu!!
(Blitz está dançando com as mãos em posição de V abaixadas e sem animação)""")

    elif jogador == 2 and blitz == 1:
        print('')
        print("""Você escolheu \033[33mPapel\033[m e Blitz escolheu \033[32mPedra.\033[m Você venceu!!
(Blitz projeta um holograma envolvendo suas próprias mãos robóticas com sacos de arroz galáticos! São deliciosos)""")

    elif jogador == 2 and blitz == 3:
        print('')
        print("""Você escolheu \033[33mPapel\033[m e Blitz escolheu \033[36mTesoura.\033[m Você perdeu!!
(Blitz dança em volta de você em posição de siri e com as mãos mecânicas em V)""")

    elif jogador == 3 and blitz == 1:
        print('')
        print("""Você escolheu \033[36mTesoura\033[m e Blitz escolheu \033[32mPedra.\033[m Você perdeu!!
(Blitz dá soquinhos na parede que estremece e... desaba...Sua mãe irá descontar o conserto da parede de sua mesada)""")

    elif jogador == 3 and blitz == 2:
        print('')
        print("""Você escolheu \033[36mTesoura\033[m e Blitz escolheu \033[33mPapel.\033[m Você venceu!!
(Blitz solta um barulho estranho em seu interior... Ele se finge de morto e gera outra parte de sí, que logo se junta novamente)""")
    
    leitor = chr(65)
    
    while leitor != chr(115) and leitor != chr(83) and leitor != chr(110) and leitor != chr(78):
        print('')
        leitor = input('Deseja brincar novamente com Blitz? \033[34ms\033[m/\033[31mn\033[m: ')
        print('')
        
        if leitor == chr(110) or leitor == chr(78):
            print('Foi divertida a brincadeira! (Blitz se ajeitou para dormir em uma caixinha com cobertores)')
    


