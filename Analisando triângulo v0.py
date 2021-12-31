a1 = float(input('Primeira reta: '))
a2 = float(input('Segunda reta:  '))
a3 = float(input('Terceira reta: '))

if a1 + a2 > a3 and a1 + a3 > a2 and a2 + a3 > a1:
    
    if a1 == a2 == a3:
        print('É possível formar um triângulo equilátero!')
        
    elif a1 == a2 or a1 == a3 or a2 == a3:
        print('É possível formar um triângulo isósceles!')
    
    else:
        print('É possível formar um triângulo escaleno!')
    
else:
    print('Não é possível formar um triângulo com as três retas')
    


