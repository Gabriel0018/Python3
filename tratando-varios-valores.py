print('\033[35m=\033[m' * 85)
print('{:^85}'.format('Somador de valores'))
print('{:^85}'.format('Digitar 999 sai do programa e mostra o somatório dos números'))
print('\033[35m=\033[m' * 85)

lista = []

n = 0
while n != 999:
    n = int(input('Valor: '))
    
    if n == 999:
        break;
    
    lista.append(n)

i = 0
soma = 0
while i <= len(lista) - 1:
    soma = soma + lista[i]
    i = i + 1

print('\n{} \033[33m= {}{}{}'.format('Lista dos valores digitados', '\033[33m', lista, '\033[m'))    
print('{} \033[36m= {}{}'.format('Soma dos valores', '\033[36m', soma))
