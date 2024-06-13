import random
print('Välkommen att kasta tärning\nEtt spel kostar 1 krona\nVinstplan:\nTvå lika - 5 kr\nEn sexa - 3 kr\nEn stege - 3 kr\n')
svar = input('Välj spela (s), sätta in pengar (i), eller avsluta (a): ')
kronor = 0
while svar != 'a':
    if svar != 'i' and svar != 's':
        svar = input('Förstod inte, spela (s), sätta in pengar (i), eller avsluta (a): ')
    if svar == 'i':
        add = int(input('Ange belopp att sätta in: '))
        if add >= 0:
            kronor = kronor + add
        else:
            print('Nja nu blev det lite fel va?')
        svar = input('Välj spela (s), sätta in pengar (i), eller avsluta (a): ')
    if svar == 's':
        if kronor < 1:
            print('Pank')
        if kronor > 0:
            a = random.randrange(20)+1
            b = random.randrange(20)+1
            print(a,b)
            if a == b:
                kronor = kronor + 5
                print('Lika! +5 kr')
            if a == 6:
                kronor = kronor + 3
                print('En sexa! +3 kr')
            elif b == 6:
                kronor = kronor + 3
                print('En sexa! +3 kr')
            if a == b-1:
                kronor = kronor + 3
                print('En stege! +3 kr')
            elif a == b+1:
                kronor = kronor + 3
                print('En stege! +3 kr')
            kronor = kronor - 1
        print('Att spela för:',kronor,'kr')
        svar = input('Välj spela (s), sätta in pengar (i), eller avsluta (a): ')
    if svar == "a":
        print('Kul att du spela, ses snart igen!')