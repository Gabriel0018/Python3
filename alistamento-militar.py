from datetime import date
idade = int(input('Informe o ano de nascimento: '))
ano = date.today().year

while idade < 0:
    idade = int(input('Informe uma data de nascimento válida: '))

if (ano - idade) < 18:
    print('Ainda não chegou seu período de alistamento militar, faltam \033[34m{} ano(s)\033[m'.format(18 - (ano - idade)))
    
elif (ano - idade) == 18:
    print("""Seu período de alistamento militar é esse ano. Fique atento aos prazos no site \033[36mhttps://alistamento.eb.mil.br/
\033[mOu procure um posto de atendimento presencial da junta militar""")

else:
    print("""Já ocorreu seu período de alistamento militar à \033[31m{} ano(s)\033[m 
Procure um posto de atendimento presencial da junta militar""".format((ano - idade) - 18))

