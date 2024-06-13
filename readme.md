# Logbok

## 23.12.08
Gjorde:
### Classes & Objects

## 23.10.23
Gjorde:

## 23.10.20
Gjorde:

## 23.10.16
Gjorde:
### Egna saker - binära talsystem
Fil: Binära talsystem
Lärde mig hur man konverterar talsystem på datorn och matematikst

Exemple:
print(bin(100).lstrip('-0b'))
--> 1100100

Klurigt men gick bra tillslut

### 7096 for each-slinga
Fil: 20996 for each-slinga
Lärde mig om for slingor och strings

Exempel:

text = "hej"
antalE = 0
for bokstav in text:
    if bokstav == 'e':
        antalE = antalE + 1
print('antal e:', antalE)

Gick fint fint!

## 23.10.13
Gjorde:
### Egna saker (på matten)
Fil: Hello, World
Lärde mig hur man räknar ut derivatan för ett värde på x för en graf.

Exempel:

def f(x):
    return x**x
def f_prim(a):
    h = 0.00000000001
    return (f(a + h) - f(a)) / h
a = 2
print(f_prim(a))

Gick bra!

### Sten sax påse (med pengar) - slumptal och spel
Fil: StenSaxPåse
Övade på att implatera pengar i spel, i detta fall sten sax påse.

Klurigt men förstod tillslut.

### 7095 for-slingor med range
fil: 7095 Uppgift 1
Lärde mig använda for-slingor med range och förstå hur det funkar.

Exempel:

for n in range(1, 11):
    print(n)

Gick bra!

## 23.10.09
Gjorde:
### Egna saker
Fil: 20 okt (lista - sten sax påse)
Lärde mig hur man använder lista samt hur man printar ut random saker från listan.
Denna lärdom har jag inplanterat i spelet "sten sax påse".

Exempel:

import random
Lista = ['Äpple', 'banan', 'kiwi']
a = Lista[random.randrange(3)]
print(a)

Gick bra!