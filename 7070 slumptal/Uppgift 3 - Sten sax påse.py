import random
import time
print('Välkommen till STEN SAX PÅSE!')
time.sleep(1)
svar = input('Spela (s) eller avsluta (a): ')
while svar == 's':
    spelare = input('Välj sten, sax eller påse: ')
    dator = random.randrange(3)
    if dator == 0:
        print('STEN')
        if spelare == 'sten':
            print('Oavgjort!')
        elif spelare == 'sax':
            print('Du förlora!')
        elif spelare == 'påse':
            print('Du vann!')
    elif dator == 1:
        print('SAX')
        if spelare == 'sten':
            print('Du vann!')
        elif spelare == 'sax':
            print('Oavgjort!')
        elif spelare == 'påse':
            print('Du förlora!')
    else:
        print('PÅSE')
        if spelare == 'sax':
            print('Du vann!')
        elif spelare == 'påse':
            print('Oavgjort!')
        elif spelare == 'sten':
            print('Du förlora!')
    svar = input('Spela (s) eller avsluta (a): ')
if svar == 'a':
    print('Bra match!')