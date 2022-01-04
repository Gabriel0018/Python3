n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota:  '))
media = (n1 + n2) / 2

if media >= 7:
    print("""Média total = {}
\033[34mAprovado\033[m""".format(media))

elif media >= 5 and media < 7:
    print("""Média total = {}
\033[33mRecuperação\033[m""".format(media))

else:
    print("""Média total = {}
\033[31mReprovado\033[m""".format(media))