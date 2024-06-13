import random

svar = input('Vill du spela? j/n\n')
while svar == 'j':
    första = random.randrange(6)+1
    andra = random.randrange(6)+1
    print(första, andra)
    if första == andra:
        print('Vinst!')
    else:
        print('Förlust!')
    svar = input('Vill du köra igen? j/n\n')
print('Vad roligt att du spelade en stund!')