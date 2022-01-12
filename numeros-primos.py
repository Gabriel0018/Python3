print('\033[35m=\033[m' * 85)
print('{}'.format('Número primo é aquele que é apenas divisível por 1 e por ele mesmo, ou seja, divisível exclusivamente por dois valores'))
print('\033[35m=\033[m' * 85)
n = int(input('Digite um número \033[32mpositivo\033[m inteiro: '))
while n < 1:
    n = int(input('Apenas número \033[32mpositivo:\033[m inteiro: '))
total = 0
for i in range (1, n + 1):
    if n % i == 0:
        print('\033[34m', end = '')
        total = total + 1
    else:
        print('\033[31m', end = '')
        
    print('{} '.format(i), end = '')

if total > 2:
    print("""\n\033[mO número {} não é primo!
pois foi divisível \033[34m{} vezes""".format(n, total))

elif total == 2:
    print("""\n\033[mO número {} é primo!
pois foi divisível \033[34m2 vezes""".format(n,))

else:
    print("""\n\033[mO número {} não é primo!
pois foi divisível \033[34muma única vez""".format(n))
