svar = int(input('Gissa på ett random heltal mellan 1-10: '))
while svar != 4:
    if svar > 10:
        print('Det måste vara 10 och under!')
    elif svar < 1:
        print('Det måste vara 1 och över!')
    svar = int(input('Du gissade fel. Gissa på ett annat tal: '))
print('Du gissade rätt!')