giss = 1
svar = int(input('Gissa på ett heltal mellan 1-20: '))
while svar != 7 and giss < 3:
    if svar < 7 and svar >= 1:
        print('För litet')
    elif svar > 20:
        print('Inte över 20!')
    elif svar < 1:
        print('Inte under 1!')
    else:
        print('För stort')
    giss = giss + 1
    svar = int(input('Du får en chans till: '))
if svar == 7:
    print('Rätt!')
else:
    print('Du förlora!')