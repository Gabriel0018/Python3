#A vista 10% de desconto
#Cartão de débito 5% de desconto
#Cartão de crédito 1x ou 2x parcelas é preço normal
#Cartão de crédito acima de 2x parcelas 20% de juros

print('\033[36m{:-^45}'.format('BEM DOCES'))
produto = float(input('\033[mDigite o preço inicial do produto: R$'))

while produto < 0:
    produto = float(input('Digite o preço inicial do produto: R$'))
    
leitor =int(input("""\033[32m(1)Dinheiro\033[m
\033[33m(2)Cartão de débito\033[m
\033[35m(3)Parcela de 1x ou 2x no cartão de crédito\033[m
\033[36m(4)Mais parcelas no cartão de crédito\033[m
Selecione a forma de pagamento: """))

while leitor < 1 or leitor > 4:
    print('')
    leitor =int(input("""\033[32m(1)Dinheiro\033[m
\033[33m(2)Cartão de débito\033[m
\033[35m(3)Parcela de 1x ou 2x no cartão de crédito\033[m
\033[36m(4)Mais parcelas no cartão de crédito\033[m
Selecione a forma de pagamento: """))

if leitor == 1:
    print('Preço do produto = R${:.2f}'.format(produto))
    print('Preço a pagar = \033[32mR${:.2f}\033[m'.format(produto * 0.9))
    
elif leitor == 2:
    print('Preço do produto = R${:.2f}'.format(produto))
    print('Preço a pagar = \033[33mR${:.2f}\033[m'.format(produto * 0.95))
    
elif leitor == 3:
    parcelas = int(input("""(1)Parcela 1x   (2)Parcela 2x
Selecione a quantidade de parcelas: """))

    while parcelas < 1 or parcelas > 2:
        parcelas = int(input("""(1)Parcela 1x   (2)Parcela 2x
Selecione a quantidade de parcelas: """))
    
    if parcelas == 1:
        print('Preço do produto = R${:.2f}'.format(produto))
        print('Preço a pagar = \033[35mR${:.2f}\033[m'.format(produto))
        
    elif parcelas == 2:
        print('Preço do produto = R${:.2f}'.format(produto))
        print('Preço total = R${:.2f}'.format(produto))
        print('Preço a pagar = \033[35mR${:.2f}\033[m'.format(produto / parcelas))

elif leitor == 4:
    parcelas = int(input('Digite a quantidade de parcelas: '))
    
    while parcelas <= 0:
        parcelas = int(input('Digite a quantidade de parcelas (não é possível parcelar por 0 ou negativo): '))
    
    if parcelas == 1:
        print('Preço do produto = R${:.2f}'.format(produto))
        print('Preço a pagar = \033[35mR${:.2f}\033[m'.format(produto))
    
    elif parcelas == 2:
        print('Preço do produto = {:.2f}'.format(produto))
        print('Preço total = R${:.2f}'.format(produto))
        print('Preço a pagar por mês = \033[35mR${:.2f}\033[m'.format((produto / parcelas)))
    
    
    else:
        print('Preço do produto = R${:.2f}'.format(produto))
        print('Preço total = R${:.2f}'.format(produto * 1.2))
        print('Preço a pagar por mês = \033[36mR${:.2f}\033[m'.format((produto * 1.2) / parcelas))


