ano = int(input('Digite o ano para descobrir se ele é Bissexto: '))

if ano % 4 == 0:
    print('O ano informado é Bissexto, e o próximo ano Bissexto será em {}'.format(ano + 4))

else:
    while ano % 4 != 0:
        ano = ano + 1
    print('O ano informado não é Bissexto, o ano Bissexto mais próximo será em {}'.format(ano))
