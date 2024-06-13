import random
print("Välkommen att kasta tärning\nEtt spel kostar 1 krona\nVinstplan:\nTvå lika - 5 kr\nEn sexa - 3 kr\nEn stege - 3 kr\n")
svar = input("Välj att spela (s), sätta in pengar (i), tag ut pengar (u), eller avsluta (a): ")
kronor = 0
wallet = 100
while svar != "a":
    if svar != "i" and svar != "s" and svar != "u":
        svar = input("Förstod inte, spela (s), sätta in pengar (i), tag ut pengar (u), eller avsluta (a): ")
    if svar == "u":
        print("Plånbok:",wallet,"\nI maskin:",kronor)
        add = int(input("Ange belopp att ta ut: "))
        if add >= 0:
            if kronor >= add:
                wallet = wallet + add
                kronor = kronor - add
            else:
                print("Maskinen har inga pengar kvar!")
        else:
            print("Försök inte ta mer än vad du får")
        svar = input("Välj att spela (s), sätta in pengar (i), tag ut pengar (u), eller avsluta (a): ")
    if svar == "i":
        print("Plånbok:",wallet,"\nI maskin:",kronor)
        add = int(input("Ange belopp att sätta in: "))
        if add >= 0:
            if wallet >= add:
                kronor = kronor + add
                wallet = wallet - add
            else:
                print("Du har inga pengar att sätta in!")
        else:
            print("Scammer")
        svar = input("Välj att spela (s), sätta in pengar (i), tag ut pengar (u), eller avsluta (a): ")
    if svar == "s":
        if kronor < 1:
            print("Pank")
        if kronor > 0:
            a = random.randrange(20)+1
            b = random.randrange(20)+1
            print(a,b)
            if a == b:
                kronor = kronor + 5
                print("Lika! +5!")
            if a == 6:
                kronor = kronor + 3
                print("En sexa! +3!")
            elif b == 6:
                kronor = kronor + 3
                print("En sexa! +3!")
            if a == b-1:
                kronor = kronor + 3
                print("En stege! +3")
            elif a == b+1:
                kronor = kronor + 3
                print("En stege! +3")
            kronor = kronor - 1
        print("Att spela för:",kronor)
        svar = input('Välj att spela (s), sätta in pengar (i), tag ut pengar (u) eller avsluta (a): ')
    if svar == "a":
        print("Kul att du spela, ses igen snart! >:)")
    if kronor + wallet == 0:
        print("Du är nu fattig, ha det så bra!")
        svar = "a"