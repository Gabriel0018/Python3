print('\033[35m=\033[m' * 60)
print('{:^60}'.format('Análise de dados'))
print('\033[35m=\033[m' * 60)
c = 0

total_sexo = []
total_idade = []
lista_idade = []
lista_homem = []
lista_mulher_20 = []

while True:
    c = c + 1
    print('{}ᵒ cadastro'.format(c))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    while sexo != chr(77) and sexo != chr(70):
        sexo = str(input('Sexo [M/F]: ')).upper().strip()
    
    total_sexo.append(sexo)
        
    if sexo == chr(77):
        lista_homem.append(sexo)
    
    idade = int(input('Idade: '))
    while idade < 0:
        idade = int(input('Idade: '))
    
    total_idade.append(idade)
    
    if idade >= 18:
        lista_idade.append(idade)
        
    if idade <= 20 and sexo == chr(70):
        lista_mulher_20.append(idade)
        
    leitor = str(input('Deseja realizar novos cadastros? [S/N]: ')).upper().strip()
    while leitor != chr(83) and leitor != chr(78):
        leitor = str(input('Deseja realizar novos cadastros? [S/N]: ')).upper().strip()
    
    if leitor == chr(78):
        print('-' * 60)
        d = 0
        for i in range (0, len(total_sexo)):
            d = d + 1
            print('{:<2}ᵒ cadastro: {:<2} anos - {}'.format(d, total_idade[i], total_sexo[i]))
            
        print('\033[35m-\033[m' * 60)
        print('\033[32mA\033[m - {} cadastros tem mais de 17 anos'.format(len(lista_idade)))
        print('\033[33mB\033[m - {} homens foram cadastrados'.format(len(lista_homem)))
        print('\033[36mC\033[m - {} mulheres cadastradas tem menos de 21 anos'.format(len(lista_mulher_20)))
        print('\033[35m-\033[m' * 60)
        break
    
    else:
        print('-=' * 40)
