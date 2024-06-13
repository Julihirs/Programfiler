from math import pi

# Programmet ska räkna ut alla sidor i en triangel med hjälp av sinussatsen. En sida och två vinklar måste anges.

def kolla_sida():
    sida = input('Ange sida (a, b, c): ')
    match sida:
        case 'a':
            return 'a'
        case 'b':
            return 'b'
        case 'c':
            return 'c'
    return ''
    
def kolla_värde(sida):
    värde = float(input(f'Ange värde på sida {sida}: '))
    return värde

def kolla_vinkel():
    vinkel = input('Ange vinkel (A, B, C): ')
    match vinkel:
        case 'A':
            return 'A'
        case 'B':
            return 'B'
        case 'C':
            return 'C'
    return ''

def kolla_grader(vinkel):
    grader = float(input(f'Ange grader på vinkel {vinkel}: '))
    return grader

def beräkna(sida, värde, vinkel_1, grader_1, vinkel_2, grader_2):
    if 'A' not in {vinkel_1, vinkel_2}:
        vinkel_3 = 'A'
    elif 'B' not in {vinkel_1, vinkel_2}:
        vinkel_3 = 'B'
    else:
        vinkel_3 = 'C'

    grader_3 = 180 - grader_1 - grader_2
    sin_1 = grader_1 * 180/pi
    sin_2 = grader_2 * 180/pi
    sin_3 = grader_3 * 180/pi

    val_1 = (värde * sin_1)/sin_3
    val_2 = (värde * sin_2)/sin_3

    sida_1 = chr(((ord(sida) - ord('a') + 1) % 3) + ord('a'))
    sida_2 = chr(((ord(sida) - ord('a') + 2) % 3) + ord('a'))
    print(f'Sida {sida} är {round(värde, 0)}, Sida {sida_1} är {round(val_1, 0)}, Sida {sida_2} är {round(val_2, 0)}')
    
    # if sida_a and vinkel_A == 'ja' and vinkel_B == 'ja':
    #     C = 180 - B - A
    #     sin_A = A * 180/pi
    #     sin_B = B * 180/pi
    #     sin_C = C * 180/pi
    #     b = (a * sin_B)/sin_A
    #     c = (a * sin_C)/sin_A

    # if sida_b and vinkel_A and vinkel_C == 'ja':
    #     B = 180 - A - C
    #     sin_A = A * 180/pi
    #     sin_B = B * 180/pi
    #     sin_C = C * 180/pi
    #     c = (b * sin_C)/sin_B
    #     a = (b * sin_A)/sin_B

def main():
    sida = kolla_sida()
    if sida == '':
        print('Odefinierad sida angavs!')
        return
    värde = kolla_värde(sida)

    vinkel_1 = kolla_vinkel()
    if vinkel_1 == '':
        print('Odefinierad vinkel angavs!')
        return
    grader_1 = kolla_grader(vinkel_1)

    vinkel_2 = kolla_vinkel()
    if vinkel_2 == '' or vinkel_2 == vinkel_1:
        print('Odefinierad vinkel angavs!')
        return
    grader_2 = kolla_grader(vinkel_2)

    print(f'Sida {sida} = {värde}, Vinkel {vinkel_1} = {grader_1}, Vinkel {vinkel_2} = {grader_2}')

    beräkna(sida, värde, grader_1, grader_2)

main()
# sida = 'c'
# print(chr((ord(sida) + 1) % ord('c') + ord('a')))