nome = str(input('Escreva seu nome completo: '))
nome = nome.strip().capitalize().split()
final = int(len(nome)) - 1

if final > 0:
    print('Primeiro nome = {} \nÚltimo nome   = {}'.format(nome[0], nome[final].capitalize()))

else:
    print('Primeiro nome = {}'.format(nome[0]))