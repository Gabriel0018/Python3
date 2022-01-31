print('\033[35m=\033[m' * 60)
print('{:^60}'.format('Simulador de caixa eletrônico'))
print('{:^60}'.format('Notas de: 200, 100, 50, 20, 10, 5 e 2'))
print('\033[35m=\033[m' * 60)

nota200 = nota100 = nota50 = nota20 = nota10 = nota5 = nota2 = 0

dinheiro = float(input('Valor do saque: R$'))
while dinheiro < 0:
    dinheiro = float(input('Valor do saque: R$'))

while True:
    if dinheiro >= 200:
        dinheiro = dinheiro - 200
        nota200 = nota200 + 1
        
        
    elif dinheiro >= 100:
        dinheiro = dinheiro - 100
        nota100 = nota100 + 1
        
        
    elif dinheiro >= 50:
        dinheiro = dinheiro - 50
        nota50 = nota50 + 1
        
        
    elif dinheiro >= 20:
        dinheiro = dinheiro - 20
        nota20 = nota20 + 1
        
        
    elif dinheiro >= 10:
        dinheiro = dinheiro - 10
        nota10 = nota10 + 1
        
        
    elif dinheiro >= 5:
        dinheiro = dinheiro - 5
        nota5 = nota5 + 1
        
        
    elif dinheiro >= 2:
        dinheiro = dinheiro - 2
        nota2 = nota2 + 1
        
    else:
        if nota200 > 0:
            print(f'{nota200} nota(s) de 200')
        
        if nota100 > 0:
            print(f'{nota100} nota(s) de 100')
            
        if nota50 > 0:
            print(f'{nota50} nota(s) de 50')
            
        if nota20 > 0:
            print(f'{nota20} nota(s) de 20')
            
        if nota10 > 0:
            print(f'{nota10} nota(s) de 10')
            
        if nota5 > 0:
            print(f'{nota5} nota(s) de 5')
            
        if nota2 > 0:
            print(f'{nota2} nota(s) de 2')
        
        if dinheiro != 0:
            print('Sobrou R${:.2f} que não foi possível retirar!'.format(dinheiro))
        break
    