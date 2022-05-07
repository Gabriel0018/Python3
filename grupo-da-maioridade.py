from datetime import date

lista = ['1ᵃ pessoa: ','2ᵃ pessoa: ', '3ᵃ pessoa: ', '4ᵃ pessoa: ', '5ᵃ pessoa: ', '6ᵃ pessoa: ', '7ᵃ pessoa: ']
lista_idade = []
ano = date.today().year
mes = date.today().month
dia = date.today().day
lista_idade_maior = []
lista_idade_menor = []

print('=' * 70)
print('Escreva a data de nascimento, mês e dia de nascimento de 7 pessoas')
print('=' * 70)

for i in range(0, 7):
    n = int(input(lista[i]))
    
    while n < 0:
        n = int(input('{} {}'.format('(Digite uma data de nascimento válida)', lista[i])))
        
    leitor = int(input("""(1)Janeiro (2)Fevereiro (3)Março (4)Abril (5)Maio (6)Junho
(7)Julho (8)Agosto (9)Setembro (10)Outubro (11)Novembro (12)Dezembro
Escolha o mês do aniversário: """))
    
    while leitor > 12 or leitor < 1:
        print('')
        leitor = int(input("""(1)Janeiro (2)Fevereiro (3)Março (4)Abril (5)Maio (6)Junho
(7)Julho (8)Agosto (9)Setembro (10)Outubro (11)Novembro (12)Dezembro
Escolha o mês do aniversário: """))
    
    if leitor > mes:
        lista_idade.append(ano - n - 1)
        
    elif leitor == mes:
        dia_nascimento = int(input('Digite o dia de nascimento: '))
        
        if dia_nascimento > dia:
            while dia_nascimento < 1 or dia_nascimento > 31:
                dia_nascimento = int(input('Digite o dia de nascimento: '))
                
            lista_idade.append(ano - n - 1)
        
        else:
            lista_idade.append(ano - n)
            
    else:
        lista_idade.append(ano - n)
    
    if lista_idade[i] >= 18:
        lista_idade_maior.append(lista_idade)
    
    else:
        lista_idade_menor.append(lista_idade)
    
    print('')
    
for i in range (0, 7):
    
    if lista_idade[i] >= 18:
        print('{}{:<3} anos -> \033[36mmaioridade\033[m'.format(lista[i], lista_idade[i]))
    
    else:
        print('{}{:<3} anos -> \033[33mmenoridade\033[m'.format(lista[i], lista_idade[i]))
    

print('\nQuantidade de pessoas \033[36mna maioridade\033[m = {}'.format(len(lista_idade_maior)))    
print('Quantidade de pessoas \033[33mmenores de 18 anos\033[m = {}'.format(len(lista_idade_menor)))   

