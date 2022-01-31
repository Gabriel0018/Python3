print('\033[35m=\033[m' * 70)
print('{:^70}'.format('Sequência de Fibonacci'))
print('\033[35m=\033[m' * 70)

n = int(input('Quantos termos de Fibonacci deseja visualizar?: '))
i = 0
lista = [0,1]

while i <= n - 3:
    soma = lista[i] + lista [i+1]
    lista.append(soma)
    i = i + 1

if n == 1:
    lista = [0]
    print(lista)

elif n >= 2:
    print(lista)
