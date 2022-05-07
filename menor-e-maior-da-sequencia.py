print('\033[35m=\033[m' * 40)
print('Digite os pesos, em kg, de 5 pessoas')
print('\033[35m=\033[m' * 40)

maior = 0
menor = 0

for i in range(1,6):
    n = float(input('Peso da {}ᵃ pessoa = '.format(i)))
    
    if i == 1:
        maior = n
        menor = n
    
    else:
        if n > maior:
            maior = n
            
        if n < menor:
            menor = n

print('\n\033[36mMaior peso = {}kg'.format(maior))
print('\033[33mMenor peso = {}kg'.format(menor))