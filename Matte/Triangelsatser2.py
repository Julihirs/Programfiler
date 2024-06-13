from math import *

# Programmet ska räkna ut alla sidor i en triangel med hjälp av sinussatsen. En sida och två vinklar måste anges.


print('Vilka sidor vet du?')
sida_a = input('Vet du sida a? ja/nej: ')
if sida_a == 'ja':
    a = float(input('Ange värde på sida a: '))
else:
    sida_b = input('Vet du sida b? ja/nej: ')
    if sida_b == 'ja':
        b = float(input('Ange värde på sida b: '))
    else:
        sida_c = input('Vet du sida c? ja/nej: ')
        if sida_c == 'ja':
            c = float(input('Ange värde på sida c: '))


vinkel_A = input('Vet du vinkel A? ja/nej: ')
if vinkel_A == 'ja':
    A = float(input('Ange grader på vinkel A: '))
vinkel_B = input('Vet du vinkel B? ja/nej: ')
if vinkel_B == 'ja':
    B = float(input('Ange grader på vinkel B: '))
elif vinkel_B and vinkel_A == 'nej':
    print('För lite information!')
else:
    vinkel_C = input('Vet du vinkel C? ja/nej: ')
    if vinkel_C == 'ja':
        C = float(input('Ange grader på vinkel C: '))
    elif vinkel_C == 'nej':
        print('För lite information!')

if sida_a and vinkel_A and vinkel_B == 'ja':
    C = 180 - B - A
    sin_A = A * 180/pi
    sin_B = B * 180/pi
    sin_C = C * 180/pi
    b = (a * sin_B)/sin_A
    c = (a * sin_C)/sin_A
    print('Sida a är ca' ,round(a,0), 'cm, sida ca' ,round(b, 0), 'cm och sidan c' ,round(c,0), 'cm.')

if sida_b and vinkel_A and vinkel_C == 'ja':
    B = 180 - A - C
    sin_A = A * 180/pi
    sin_B = B * 180/pi
    sin_C = C * 180/pi
    c = (b * sin_C)/sin_B
    a = (b * sin_A)/sin_B