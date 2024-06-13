import random
print('Välkommen till STEN SAX PÅSE')
svar = input('Spela (s) eller avsluta (a): ')
while svar == 's':
    spelare = input('Välj sten, sax eller påse: ')
    lista = ['sten', 'sax', 'påse']
    a = lista[random.randrange(3)]
    print(a)
    if spelare == a:
        print('Oavgjort')
    elif spelare == 'sten' and a == 'sax':
        print('Du vann!')
    elif spelare == 'påse' and a == 'sax':
        print('Du förlora...')
    elif spelare == 'sax' and a == 'påse':
        print('Du vann!')
    elif spelare == 'sten' and a == 'påse':
        print('Du förlora...')
    elif spelare == 'påse' and a == 'sten':
        print('Du vann!')
    elif spelare == 'sax' and a == 'sten':
        print('Du förlora...')
    svar = input('Spela (s) eller avsluta (a): ')
    if svar == 'a':
        print('Bra match!')