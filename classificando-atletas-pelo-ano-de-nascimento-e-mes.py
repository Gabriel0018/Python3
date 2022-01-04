from datetime import date

ano_nascimento = int(input('Escreva a data de nascimento do competitdor: '))

while ano_nascimento < 0:
    idade = int(input('Escreva uma data de nascimento válida: '))

print('')

leitor = int(input("""(1)Janeiro (2)Fevereiro (3)Março (4)Abril (5)Maio (6)Junho
(7)Julho (8)Agosto (9)Setembro (10)Outubro (11)Novembro (12)Dezembro

Digite o número correspondente de acordo com o mês de nascimento: """))

while leitor < 0 or leitor > 12:
    print('')
    leitor = int(input("""(1)Janeiro (2)Fevereiro (3)Março (4)Abril (5)Maio (6)Junho
(7)Julho (8)Agosto (9)Setembro (10)Outubro (11)Novembro (12)Dezembro

Digite o número correspondente de acordo com o mês de nascimento: """))
ano = date.today().year
mes = date.today().month
dia = date.today().day

idade = ano - ano_nascimento

if leitor > mes:
    idade = idade - 1
    print('Idade = {} anos'.format(idade))

elif leitor == mes:
    dia_nascimento = int(input('Digite o dia de nascimento: '))
    
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        while dia_nascimento < 1 or dia_nascimento > 31:
            dia_nascimento = int(input('Digite o dia de nascimento: (1 até 31): '))
    
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        while dia_nascimento < 1 or dia_nascimento > 30:
            dia_nascimento = int(input('Digite o dia de nascimento: (1 até 30): '))
    
    elif mes == 2:
        if ano_nascimento % 4 == 0 and ano_nascimento % 100 == 0 and ano_nascimento % 400 != 0:
            while dia_nascimento < 1 or dia_nascimento > 28:
                dia_nascimento = int(input('Digite o dia de nascimento: (1 até 28): '))
                
        elif ano_nascimento % 4 != 0:
            while dia_nascimento < 1 or dia_nascimento > 28:
                dia_nascimento = int(input('Digite o dia de nascimento: (1 até 28): '))
        
        elif ano_nascimento % 4 == 0 and ano_nascimento % 100 != 0 or ano_nascimento % 400 == 0:
            while dia_nascimento < 1 or dia_nascimento > 29:
                dia_nascimento = int(input('Digite o dia de nascimento: (1 até 29): '))
        
    if dia_nascimento < dia:
        print('Idade = {} anos'.format(idade))
        
    else:
        print('Idade = {} anos'.format(idade - 1))
    
else:
    print('Idade = {} anos'.format(idade))

if idade <= 9:
    print('\033[32mCategoria Mirim\033[m')

elif idade <= 14:
    print('\033[33mCategoria Infantil')
    
elif idade <= 19:
    print('\033[34mCategoria Junior')
    
elif idade <= 25:
    print('\033[35mCategoria Sênior')
    
else:
    print('\033[36mCategoria Master')
