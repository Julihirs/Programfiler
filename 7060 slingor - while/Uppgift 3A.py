# Om jag tolkat uppgiften rätt: koden skriver ut 1, sedan 1/1, 2/1, 3/2 osv.

i = 0
x = 1
y = 1
while (i < 30):
    if i == 0:
        print(x)
    else:
        kvoten = x / föregående_x
        print(kvoten)
    föregående_x = x
    n = x + y
    x = y
    y = n
    i = i + 1
print('klar')