import sys
print('\033[35m=\033[m' * 60)
print('{:^60}'.format('Compra de produtos'))
print('\033[35m=\033[m' * 60)

lista_nome = []
lista_valor = []
lista_50 = []
barato = []
caro = []
soma = 0
c = 0

while True:
    c = c + 1
    print('{}ᵒ produto'.format(c))
    nome = str(input('Nome: ')).capitalize().strip()
    lista_nome.append(nome)
    
    valor = float(input('Valor: R$'))
    lista_valor.append(valor)
    soma = soma + valor
    
    if valor >= 50:
        lista_50.append(nome)
    
    leitor = str(input('Há mais algum produto no carrinho? [S/N]: ')).upper().strip()
    while leitor != chr(78) and leitor != chr(83):
        leitor = str(input('Há mais algum produto no carrinho? [S/N]: ')).upper().strip()
    
    if leitor == chr(78):
        print('\033[35m-=\033[m' * 30)
        print('{:^16} | {:^10}'.format('Produto', 'Valor'))
        
        for i in range(0, len(lista_nome)):
            print('{:^16} | R${:.2f}'.format(lista_nome[i], lista_valor[i]))
        
        for i in range(0, len(lista_valor)):
            if lista_valor[i] == min(lista_valor):
                barato.append(lista_nome[i])
                break
        
        for i in range(0, len(lista_valor)):
            if lista_valor[i] == max(lista_valor):
                caro.append(lista_nome[i])
                break
        
        if len(lista_50) == 0:
            lista_50 = ['Nenhum']
        
        
        if max(lista_valor) == min(lista_valor):
            print('\033[36m-=\033[m' * 30)
            print('Total da compra = \033[36mR${:.2f}\033[m'.format(soma))
            print('Produtos que custam mais que R$49.99 = \033[33m{}\033[m'.format(lista_50))
            print('O(s) produto(s) possui(em) o mesmo valor!')
            break
        
        elif max(lista_valor) != min(lista_valor):
            print('\033[36m-=\033[m' * 30)
            print('Total da compra = \033[36mR${:.2f}\033[m'.format(soma))
            print('Produtos que custam mais que R$49.99 = \033[33m{}\033[m'.format(lista_50))
            print('O produto mais barato custa R${:.2f} = \033[32m{}\033[m'.format(min(lista_valor), barato))
            print('O produto mais caro custa R${:.2f} = \033[34m{}\033[m'.format(max(lista_valor), caro))
            print('\033[36m-=\033[m' * 30)
            break
    else:
        print('-' * 60)
