from math import *

# En sida och två vinklar ska anges av en triangel.

def vilka_sidor():
    sida = input('Ange en sida (a, b, c): ')
    match sida:
        case 'a':
            return 'a'
        case 'b':
            return 'b'
        case 'c':
            return 'c'
    return ''

def vilket_värde(sida):
    värde = float(input(f'Ange värde på sida {sida}: '))
    return värde

def vilka_vinklar():
    vinkel = input('Ange en vinkel (a, b, c): ')
    match vinkel:
        case 'a':
            return 'a'
        case 'b':
            return 'b'
        case 'c':
            return 'c'
    return ''

def vilken_grad(vinkel):
    grader = float(input(f'Ange grader på vinkel {vinkel}: '))
    return grader

def beräkna(värde, sida, vinkel_1, vinkel_2, grader_1, grader_2):
    if 'a' not in {vinkel_1, vinkel_2}:
        vinkel_3 = 'a'
    if 'b' not in {vinkel_1, vinkel_2}:
        vinkel_3 = 'b'
    else:
        vinkel_3 = 'c'
        
    grader_3 = 180 - grader_2 - grader_1
    sin_1 = sin(grader_1 * pi/180)
    sin_2 = sin(grader_2 * pi/180)
    sin_3 = sin(grader_3 * pi/180)

    if vinkel_1 == sida:
        sida_2 = (värde * sin_2)/sin_1
        sida_3 = (värde * sin_3)/sin_1
        sida_1 = värde
    elif vinkel_2 == sida:
        sida_1 = (värde * sin_1)/sin_2
        sida_3 = (värde * sin_3)/sin_2
        sida_2 = värde
    else:
        sida_1 = (värde * sin_1)/sin_3
        sida_2 = (värde * sin_2)/sin_3
        sida_3 = värde

    print('Sidorna av triangeln är:')   
    print(sida_1, sida_2, sida_3)

def main():
    sida = vilka_sidor()
    while sida == '':
        print('Odefinerad sida!')
        sida = vilka_sidor()
    värde = vilket_värde(sida)

    vinkel_1 = vilka_vinklar()
    while vinkel_1 == '':
        print('Odefinerad vinkel!')
        vinkel_1 = vilka_vinklar()
    grader_1 = vilken_grad(vinkel_1)

    vinkel_2 = vilka_vinklar()
    while vinkel_2 == '' or vinkel_2 == vinkel_1:
        print('Odefinerad vinkel!')
        vinkel_2 = vilka_vinklar()
    grader_2 = vilken_grad(vinkel_2)

    beräkna(värde, sida, vinkel_1, vinkel_2, grader_1, grader_2)

main()