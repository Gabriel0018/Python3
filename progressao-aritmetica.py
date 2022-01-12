print('=' * 55)
print('\033[33m{:^55}\033[m'.format('10 Termos de uma PA'))
print('=' * 55)

n1 = int(input('Digite o primeiro termo da \033[36mProgressão Aritmética: \033[m'))
razao = int(input('Digite a razão: '))
termo = ['1ᵒ termo','2ᵒ termo','3ᵒ termo','4ᵒ termo','5ᵒ termo','6ᵒ termo','7ᵒ termo','8ᵒ termo','9ᵒ termo','10ᵒ termo']
soma = n1

print('')
print('{:>9} = {}'.format(termo[0], n1))

for i in range (1,10):
    soma = soma + razao
    print('{:>9} = {}'.format(termo[i], soma))
