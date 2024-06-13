import random
import time
print("VÄLKOMMEN TILL LUCKY SEVEN!")
hej = int(input("Skriv hur många kr du vill sätta in: "))
print()
print("Varje spel kostar 2 kr\nTre lika = vinst (25 kr)\nTre sjuor = dubbelvinst (50 kr)\nTvå lika = minivinst (5 kr)\nEn sjua = sjuvinst (3 kr)\nDu har", hej, "kr vid start\n")
time.sleep(3)
print()
i = hej
svar = input("Skriv s för att spela och a för att avsluta: ")
while i > 0:
    while svar == "s":
        i = i - 2
        tal1 = (random.randrange(10))
        tal2 = (random.randrange(10))
        tal3 = (random.randrange(10))
        print(tal1, tal2, tal3)
        if tal1 == tal2 == tal3:
            if tal1 == 7:
                print("Dubbelvinst!")
                i = i + 50
                print("Kvar att spela för:", i, "kr")
            else:
                print("Vinst!")
                i = i + 25
                print("Kvar att spela för:", i, "kr")
        elif tal1 == tal2:
            print("Minivinst!")
            i = i + 5
            print ("Kvar att spela för", i, "kr")
        elif tal2 == tal3:
            print("Minivinst!")
            i = i + 5
            print ("Kvar att spela för", i, "kr")
        elif tal1 == tal3:
            print("Minivinst!")
            i = i + 5
            print ("Kvar att spela för", i, "kr")
        elif (tal1 == 7) or (tal2 == 7) or (tal3 == 7):
            print("Sjuvinst!")
            i = i + 3
            print("Kvar att spela för:", i, "kr")
        else:
            print("Förlust")
            print("Kvar att spela för:", i, "kr")
        svar = input("Skriv s för att spela och a för att avsluta: ")
        if svar == "a":
            print("Tack för att du spelade en stund!")