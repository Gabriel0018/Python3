nome = str(input('Escreva seu nome completo: '))

maiuscula = nome.strip().split()
print('Maiúsculas = {}'.format(' '.join(maiuscula).upper()))

minuscula = nome.strip().split()
print('Minúsculas = {}'.format(' '.join(minuscula).lower()))

letras = nome.strip().split()
letras = ''.join(letras)
print('Quantidade de letras = {}'.format(len(letras)))

letras1nome = nome.strip().split()
letras1nome = letras1nome[0]
print('Quantidade de letras no primeiro nome = {}'.format(len(letras1nome)))

