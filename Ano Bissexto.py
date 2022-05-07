from datetime import date
ano = int(input('Digite o ano para descobrir se ele é Bissexto: (digitar 0 analisa o ano atual): '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 == 0 and ano % 400 != 0:
    print('O ano informado não é Bissexto, o ano Bissexto mais próximo será em {}'.format(ano + 4))

elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano informado é Bissexto, e o próximo ano Bissexto será em {}'.format(ano + 4))

else:
    while ano % 4 != 0:
        ano = ano + 1
    print('O ano informado não é Bissexto, o ano Bissexto mais próximo será em {}'.format(ano))


