distancia = int(input('Escreva a distância, em km, da sua viagem: '))

if distancia > 200:
    print('Passagem = R${:.2f}'.format(distancia * 0.45))
    
else:
    print('Passagem = R${:.2f}'.format(distancia * 0.50))