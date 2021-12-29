frase = str(input('Escreva o nome de uma cidade: '))
frase = frase.upper().split()

# Mostrar True se a palavra "SANTO" existir na frase, independente da ordem
if 'SANTO' in frase[::]:
    print('Santo na frase = {}'.format(True))

# Mostrar True se a palavra "SANTO" estiver no começo da frase
if 'SANTO' in frase[0]:
    print('Santo no começo da frase = {}'.format(True))


# Mostrar True se a palavra "Santo" estiver na penúltima frase
final = int(len(frase)) - 2

for i in range (0,final):
    i = i + 1
    
    if i == final and 'SANTO' in frase[final]:
        print('Santo na penúltima frase = {}'.format(True))
        
# Mostrar True se a palavra "Santo" estiver no final da frase    
final = int(len(frase)) - 1

for i in range (0,final):
    i = i + 1
    
    if i == final and 'SANTO' in frase[final]:
        print('Santo no final da frase = {}'.format(True))
        

