print('\033[35m=\033[m' * 70)
print('{:^70}'.format('Média, maior e menor valor'))
print('\033[35m=\033[m' * 70)

lista = []

n = int(input('Valor: '))
lista.append(n)
leitor = str(input('Deseja continuar? (S/N): ')).upper()

menor = n
maior = n

while leitor == chr(83):
    n = int(input('Valor: '))
    lista.append(n)
    
    if n > maior:
        maior = n
            
    elif n < menor:
        menor = n
    
    leitor = str(input('Deseja continuar? (S/N): ')).upper()
    
    while leitor != chr(83) and leitor != chr(78):
        leitor = str(input('Deseja continuar? (S/N): ')).upper()
        
print('\nLista dos valores digitados \033[33m= {}\033[m'.format(lista))

i = 0
soma = 0

while i <= len(lista) -1:
    soma = soma + lista[i]
    i = i + 1
    
media = soma / len(lista)

print('Média \033[36m= {:.2f}\033[m'.format(media))

if len(lista) == 1 or maior == menor:
    print('Não existe valor \033[32mmaior\033[m ou \033[35mmenor\033[m!')

else:
    print('Maior valor \033[32m= {}\033[m'.format(maior))
    print('Menor valor \033[35m= {}\033[m'.format(menor))
    