print('\033[35m=\033[m' * 40)
print('Digite os pesos, em kg, de 5 pessoas')
print('\033[35m=\033[m' * 40)

### Resolvendo como listas + "For"

lista = []
contador0 = []
contador1 = []
contador2 = []
contador3 = []
contador4 = []

for i in range (1,6):
    n = float(input('Peso da {}ᵃ pessoa = '.format(i)))
    lista.append(n)
    
for i in range(0,5):
    if lista[0] > lista[i]:
        contador0.append(lista[i])

for i in range(0,5):        
    if lista[1] > lista[i]:
        contador1.append(lista[i])

for i in range(0,5):        
    if lista[2] > lista[i]:
        contador2.append(lista[i])
  
for i in range(0,5):    
    if lista[3] > lista[i]:
        contador3.append(lista[i])

for i in range(0,5):        
    if lista[4] > lista[i]:
        contador4.append(lista[i])

# Achando o maior peso

print('\n\033[36m', end = '') # Adicionando cores

if len(contador0) == 4:
    print('Maior peso = {}kg'.format(lista[0]))
    
elif len(contador1) == 4:
    print('Maior peso = {}kg'.format(lista[1]))

elif len(contador2) == 4:
    print('Maior peso = {}kg'.format(lista[2]))

elif len(contador3) == 4:
    print('Maior peso = {}kg'.format(lista[3]))

elif len(contador4) == 4:
    print('Maior peso = {}kg'.format(lista[4]))

# Achando o menor peso

print('\033[33m', end = '') # Adicionando cores

if len(contador0) == 0:
    print('Menor peso = {}kg'.format(lista[0]))
    
elif len(contador1) == 0:
    print('Menor peso = {}kg'.format(lista[1]))

elif len(contador2) == 0:
    print('Menor peso = {}kg'.format(lista[2]))

elif len(contador3) == 0:
    print('Menor peso = {}kg'.format(lista[3]))

elif len(contador4) == 0:
    print('Menor peso = {}kg'.format(lista[4]))
