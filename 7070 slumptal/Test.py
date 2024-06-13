import random
svar = input('Vill du spela? j/n\n')
while svar == 'j':
    första = random.randrange(6)+1
    andra = random.randrange(6)+1
    print(första, andra)
    if första == andra:
        if första == 6:
            print('MEGA VINST')
        elif första == 1:
            print('Vinst, men du suger')
        else:
            print('Vinst!')
    else:
        print('You suck!')
    svar = input('Vill du köra igen? j/n\n')


