import sys
from random import choice

blitz = [0,1,2,3,4,5]
blitz = choice(blitz)
n = int(input('Tente advinhar o número, entre 0 e 5, que o Blitz pensou nessa rodada!: '))
print('-=' * 40)

while n < 0 or n > 5:
    n = int(input('Número inválido! Escreva um número entre 0 e 5: (Blitz só sabe contar do 0 até 5): '))

if n == blitz:
    print('Parabéns, você acertou! (Blitz está triste por ter perdido)')
    print('-=' * 40)
    
else:
    print('Você errou! Blitz pensou no número {} (Blitz faz dança da vitória)'.format(blitz))
    print('-=' * 40)
    
codificador = str(input('Deseja brincar novamente com Blitz? s/n: '))

if codificador == chr(115) or codificador == chr(83):
    while codificador == chr(115) or codificador == chr(83):
    
        if codificador == chr (115) or codificador == chr(83):
            print('-=' * 40)
            n = int(input('Tente advinhar o número, entre 0 e 5, que o Blitz pensou nessa rodada!(Blitz feliz por brincar novamente): '))
            while n < 0 or n > 5:
                n = int(input('Número inválido! Escreva um número entre 0 e 5: (Blitz só sabe contar do 0 até 5): '))
            blitz = [0,1,2,3,4,5]
            blitz = choice(blitz)
            if n == blitz:
                print('-=' * 40)
                print('Parabéns, você acertou! (Blitz acha que estão lendo sua mente)')
                print('-=' * 40)
                
            else:
                print('-=' * 40)
                print('Você errou! Blitz pensou no número {} (Blitz solta vapor de felicidade pela sua cabeça)'.format(blitz))
                print('-=' * 40)
                
            codificador = str(input('Deseja brincar novamente com Blitz? s/n: '))
        
        elif codificador == chr(110) or codificador == chr(78):
            print('-=' * 40)
            print('Blitz faz um aceno de despedida com sua mão mecânica (sua mãe está fazendo... biscoitos?)')
            sys.exit(0)
            
        else:
            codificador == str(input('Blitz está ansioso por sua resposta! s/n: '))
        
elif codificador == chr(110) or codificador == chr(78):
    
    print('-=' * 40)
    print('Blitz sente o cheiro de biscoitos fresquinhos! São os de sua mãe.')
    sys.exit(0)
    
else:
    while codificador != chr(115) or codificador != chr(83) or codificador != chr(110) or codificador != chr(78):
        codificador = str(input('Blitz está ansioso por sua resposta! s/n: '))
        
        if codificador == chr (115) or codificador == chr(83):
            n = int(input('Tente advinhar o número, entre 0 e 5, que o Blitz pensou nessa rodada! (Blitz feliz por brincar novamente): '))
            while n < 0 or n > 5:
                n = int(input('Número inválido! Escreva um número entre 0 e 5: (Blitz só sabe contar do 0 até 5): '))
            blitz = [0,1,2,3,4,5]
            blitz = choice(blitz)
            if n == blitz:
                print('-=' * 40)
                print('Parabéns, você acertou! (Blitz acha que estão lendo sua mente)')
                print('-=' * 40)
            
            else:
                print('-=' * 40)
                print('Você errou! Blitz pensou no número {} (Blitz solta vapor de felicidade pela sua cabeça)'.format(blitz))
                print('-=' * 40)
            
            codificador = str(input('Deseja brincar novamente com blitz? s/n: '))
            
        elif codificador == chr(110) or codificador == chr(78):
            print('-=' * 40)
            print('Blitz faz um aceno de despedida com sua mão mecânica! (sua mãe está fazendo... biscoitos?)')
            sys.exit(0)
            
        else:
            codificador == str(input('Blitz está ansioso por sua resposta! s/n: '))   

if codificador == chr(110) or codificador == chr(78):
    print('-=' * 40)    
    print('Blitz faz um aceno de despedida com sua mão mecânica! (sua mãe está fazendo... biscoitos?)')
    sys.exit(0)
    
else:
    while codificador != chr(115) or codificador != chr(83) or codificador != chr(110) or codificador != chr(78):
        codificador = str(input('Blitz está ansioso por sua resposta! s/n: '))
        
        if codificador == chr (115) or codificador == chr (83):
            n = int(input('Tente advinhar o número, entre 0 e 5, que o Blitz pensou nessa rodada! (Blitz feliz por brincar novamente): '))
            while n < 0 or n > 5:
                n = int(input('Número inválido! Escreva um número entre 0 e 5: (Blitz só sabe contar do 0 até 5): '))
            blitz = [0,1,2,3,4,5]
            blitz = choice(blitz)
            if n == blitz:
                print('-=' * 40)
                print('Parabéns, você acertou! (Blitz acha que estão lendo sua mente)')
                print('-=' * 40)
            
            else:
                print('-=' * 40)
                print('Você errou! Blitz pensou no número {} (Blitz solta vapor de felicidade pela sua cabeça)'.format(blitz))
                print('-=' * 40)
            
            codificador = str(input('Deseja brincar novamente com blitz? s/n: '))
            
        elif codificador == chr(110) or codificador == chr(78):
            print('-=' * 40)
            print('Blitz faz um aceno de despedida com sua mão mecânica! (sua mãe está fazendo... biscoitos?)')
            sys.exit(0)
            
        else:
            codificador == str(input('Blitz está ansioso por sua resposta! s/n: '))  
    






