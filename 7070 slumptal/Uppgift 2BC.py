import random
import time
print("VÄLKOMMEN TILL LUCKY SEVEN!")
print()
time.sleep(1)
print("Tre lika = vinst\nTre sjuor = dubbelvinst\nTvå lika = minivinst\nEn sjua = sjuvinst")
svar = input("Skriv s för att spela och a för att avsluta: ")
while svar == "s":
    tal1 = (random.randrange(10))
    tal2 = (random.randrange(10))
    tal3 = (random.randrange(10))
    print(tal1, tal2, tal3)
    if tal1 == tal2 == tal3:
        if tal1 == 7:
            print("Dubbelvinst!")
        else:
            print("Vinst!")
    elif tal1 == tal2:
        print("Minivinst!")
    elif tal2 == tal3:
        print("Minivinst!")
    elif tal1 == tal3:
        print("Minivinst!")
    elif (tal1 == 7) or (tal2 == 7) or (tal3 == 7):
        print("Sjuvinst!")
    else:
        print("Förlust")
    svar = input("Skriv s för att spela och a för att avsluta: ")
if svar == "a":
    print("Tack för att du spelade en stund!")