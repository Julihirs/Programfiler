giss = 1
svar = int(input('Gissa på ett random heltal: '))
while svar != 42:
    if svar < 42:
        print('För litet')
    else:
        print('För stort')
    giss = giss + 1
    svar = int(input('Du får en chans till: '))
print('Rätt!')
print('Du behövde', giss, 'gissningar för att hitta rätt svar!')