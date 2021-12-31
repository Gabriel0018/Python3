salario = float(input('Escreva seu salário: R$'))

while salario < 0:
    salario = float(input('Escreva seu salário (não é possível receber um valor negativo): R$'))

if salario > 1250:
    print('Salário com aumento de 10% = R${:.2f}'.format(salario + (salario * 0.1)))
    
else:
    print('Salário com aumento de 15% = R${:.2f}'.format(salario + (salario * 0.15)))
