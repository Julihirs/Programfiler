#inköpslista[ ]
#len(inköpslista)
#inköpslista.append(" ")
#inköpslista.extend([" ", " "])
#inköpslista.insert(1, " ")
#inköpslista.remove(" ")
#last = inköpslista.pop()
#first = inköpslista.pop(0)
#inköpslista.sort()
#inköpslista.reverse()
#inköpslista.index(' ')

import random
lista = []
while len(lista) < 10:
    i = random.randrange(6)+1
    print(i)
    lista.append(i)

lista.sort()
print(lista)

print(sum(lista))
print(sum(lista)/len(lista))
print(min(lista))
print(max(lista))

a = lista
antal6 = 0
for tal in a:
    if tal == 6:
        antal6 = antal6 + 1
print('antal 6:or:', antal6)

a = lista
antal5 = 0
for tal in a:
    if tal == 5:
        antal5 = antal5 + 1
print('antal 5:or:', antal5)

a = lista
antal4 = 0
for tal in a:
    if tal == 4:
        antal4 = antal4 + 1
print('antal 4:or:', antal4)

a = lista
antal3 = 0
for tal in a:
    if tal == 3:
        antal3 = antal3 + 1
print('antal 3:or:', antal3)

a = lista
antal2 = 0
for tal in a:
    if tal == 2:
        antal2 = antal2 + 1
print('antal 2:or:', antal2)

a = lista
antal1 = 0
for tal in a:
    if tal == 1:
        antal1 = antal1 + 1
print('antal 1:or:', antal1)

