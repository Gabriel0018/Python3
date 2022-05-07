salario = float(input('Escreva o salário mensal do cliente: R$'))
casa = float(input('Escreva o valor da casa que será financiada: R$'))
anos = float(input('Escreva a quantidade de anos que serão necessárias para quitar a dívida: '))

meses = anos * 12
valor = casa / meses

if valor < salario * 0.3:
    print('-=-' * 30)
    print('30% do salário do cliente = \033[35mR${:.2f}\033[m \nPorcentagem do salário do cliente a ser pago = \033[33m{:.2f}%\033[m'.format(salario * 0.3, (100 * valor)/salario ))
    print('O valor mensal a ser pago será = \033[36mR${:.2f}\033[m'.format(valor))

else:
    print('-=-' * 30)
    print('30% do salário do cliente = \033[35mR${:.2f}\033[m \nPorcentagem do salário do cliente a ser pago = \033[33m{:.2f}%\033[m'.format(salario * 0.3, (100 * valor)/salario))
    print('Não será possível financiar a casa, valor a ser pago no financiamento será \033[31msuperior a 30% da renda mensal do cliente!')
