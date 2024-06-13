import random

svar = input('Vill du spela? j/n\n')
while svar == 'j':
    första = random.randrange(6)+1
    andra = random.randrange(6)+1
    print(första, andra)
    if första == andra:
        print('Vinst!')
    elif första == 6 and andra == 6:
        print('MEGA VINST!!!')
    elif andra == första + 1:
        print('Stegvinst!')
    else:
        print('Förlust')
    svar = input('Vill du spela igen? j/n\n')
print('Vad roligt att du spelade en stund!')