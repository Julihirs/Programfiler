# A antal ettor
import random
lista = []
while len(lista) < 5:
    i = random.randrange(6)+1
    print(i)
    lista.append(i)

a = lista
antal1 = 0
for tal in a:
    if tal == 1:
        antal1 = antal1 + 1
print('antal 1:or:', antal1)

# B Yatzy - fem lika
svar = input('Vill du spela Yatzy? ja eller nej: ')
if svar == 'ja':
    lista = []
while len(lista) < 5:
    i = random.randrange(6)+1
    print(i)
    lista.append(i)
    