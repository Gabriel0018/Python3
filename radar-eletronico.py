velocidade = int(input('Escreva a velocidade, em km/h, que o automóvel ultrapassou no radar: '))

if velocidade > 80:
    print('Velocidade = {}km/h = {:.2f}m/s'.format(velocidade, velocidade / 3.6))
    print("""Você excedeu o limite de velocidade de 80km/h permitido na pista
A multa será = R${:.2f}""".format((velocidade - 80) * 7))

else:
    print('Velocidade = {}km/h = {:.2f}m/s'.format(velocidade, velocidade / 3.6))
    print('Velocidade de {}km/h dentro do limite de 80km/h permitido na pista'.format(velocidade))