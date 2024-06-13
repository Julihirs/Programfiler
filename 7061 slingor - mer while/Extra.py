def primtal(x):
    if x <= 1:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i = i + 1
    return True

tal = int(input('Ange ett random heltal: '))
if primtal(tal):
    print(tal, "är ett primtal")
else:
    print(tal, 'är inte ett primtal')