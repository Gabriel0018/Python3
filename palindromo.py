print('\033[35m=\033[m' * 70)
print("""Palíndromo é quando a forma escrita contrária for igual a original
Exemplo: ana -> ana  bob -> bob  ama -> ama  anilina -> anilina""")
print('\033[35m=\033[m' * 70)

frase = str(input('Escreva alguma frase: ')).strip()
frase = frase.replace(' ', '')
frase = (' ').join(frase).split()
tamanho = int(len(frase))
print('{}{}{}'.format('\033[32m', frase, '\033[m'))

frase_invertida = []

for i in range (tamanho - 1, -1, -1):
    frase_invertida.append(frase[i])

print('{}{}{}'.format('\033[33m', frase_invertida, '\033[m'))
    
if frase_invertida == frase:
    print('A frase é palíndromo')
    
else:
    print('A frase não é palíndromo')