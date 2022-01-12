print('\033[35m=\033[m' * 70)
print('O programa coleta dados pessoais - nome, idade e gênero de 4 pessoas')
print('\033[35m=\033[m' * 70)

media = []
xnome = []
xgenero = []
genero_total = []

for i in range(1,5):
    print('{}{}ᵃ pessoa {} '.format('-' * 8, i, '-' * 8))
    nome = str(input('Nome: '.format(i))).strip().capitalize()
    xnome.append(nome)
    
    idade = int(input('Idade: '.format(i)))
    media.append(idade)
    
    while idade < 0:
        idade = int(input('Idade da {}ᵃ pessoa: '.format(i)))
    
    genero = str(input("""(H)Homem (M)Mulher
Gênero : """.format(i))).strip()
    
    while genero != chr(109) and genero != chr(77) and genero != chr(72) and genero != chr(104):
        genero = str(input("""(1)Homem (2)Mulher
Gênero : """.format(i))).strip()
    
    genero_total.append(genero)
    
    if genero == 2:
        if idade < 20:
            xgenero.append(genero)
        
    
    print('')
    

genero_total = (' ').join(genero_total)
genero_total = genero_total.upper().split()


print('{:^12} {:>6}  {:>6}'.format('Nome', 'Idade','Gênero'))

for i in range(0,4):
    print('{:^12}  {:^5}  {:^6}'.format(xnome[i], media[i], genero_total[i]))

    
print('\nA Média das idades é de \033[36m{} anos\033[m '.format((media[0] + media[1] + media[2] + media[3]) / 4))

if media[0] > media[1] and media[0] > media[2] and media[0] > media[3]:
    print('O nome da pessoa mais velha é \033[33m{}'.format(xnome[0]))
    
elif media[1] > media[0] and media[1] > media[2] and media[1] > media[3]:
    print('O nome da pessoa mais velha é \033[33m{}'.format(xnome[1]))
    
elif media[2] > media[0] and media[2] > media[1] and media[2] > media[3]:
    print('O nome da pessoa mais velha é \033[33m{}'.format(xnome[2]))
    
elif media[3] > media[0] and media[3] > media[1] and media[3] > media[2]:
    print('O nome da pessoa mais velha é \033[33m{}'.format(xnome[3]))

else:
    print('Não existe o mais velho do grupo')

print('\033[mNo grupo \033[32m{}\033[m mulher(es) tem menos de 20 anos'.format(len(xgenero)))

