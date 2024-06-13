import random
import time
print('Välkommen till STEN SAX PÅSE')
print('Varje spel kostar 1 kr\nVid vinst frå du 2 kr')
time.sleep(2)
i = int(input('Skriv hur många kronor du vill spela för: '))
svar = input('Spela (s) eller avsluta (a): ')
while i > 0:
    while svar == 's':
        i = i - 1
        spelare = input('Välj sten, sax eller påse: ')
        lista = ['sten', 'sax', 'påse']
        a = lista[random.randrange(3)]
        print(a)
        if spelare == a:
            print('Oavgjort')
        elif spelare == 'sten' and a == 'sax':
            print('Du vann!')
            i = i + 2
        elif spelare == 'påse' and a == 'sax':
            print('Du förlora...')
        elif spelare == 'sax' and a == 'påse':
            print('Du vann!')
            i = i + 2
        elif spelare == 'sten' and a == 'påse':
            print('Du förlora...')
        elif spelare == 'påse' and a == 'sten':
            print('Du vann!')
            i = i + 2
        elif spelare == 'sax' and a == 'sten':
            print('Du förlora...')
        print ("Kvar att spela för:", i, "kr")
        svar = input('Spela (s) eller avsluta (a): ')
        if svar == 'a':
            print('Bra match!')