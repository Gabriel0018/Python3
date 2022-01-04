peso = float(input('Escreva o peso, em kg: '))

while peso < 0:
    peso = float(input('Escreva o peso, em kg: '))
    
altura = float(input('Escreva a altura, em metros: '))

while altura < 0:
    altura = float(input('Escreva a altura, em metros: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('IMC = {:.2f}\n\033[36mAbaixo do peso\033[m'.format(imc))
    
elif imc >= 18.5 and imc <= 25:
    print('IMC = {:.2f}\n\033[32mPeso ideal\033[m'.format(imc))
    
elif imc > 25 and imc <= 30:
    print('IMC = {:.2f}\n\033[33mSobrepeso\033[m'.format(imc))

elif imc > 30 and imc <= 40:
    print('IMC = {:.2f}\n\033[35mObesidade\033[m'.format(imc))

else:
    print('IMC = {:.2f}\n\033[31mObesidade mórbida'.format(imc))
