n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número:  '))
n3 = int(input('Terceiro número: '))

if n1 <= n2 and n1 <= n3:
    print('Menor valor = {}'.format(n1))
    
elif n2 <= n1 and n2 <= n3:
    print('Menor valor = {}'.format(n2))
    
else:
    print('Menor valor = {}'.format(n3))
    
if n1 >= n2 and n1 >= n3:
    print('Maior valor = {}'.format(n1))

elif n2 >= n1 and n2 >= n3:
    print('Maior valor = {}'.format(n2))

else:
    print('Maior valor = {}'.format(n3))

