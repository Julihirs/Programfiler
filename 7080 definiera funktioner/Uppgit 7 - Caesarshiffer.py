def f(c):
    return c + x

c = input('Skriv din text: ')
x = int(input('Skriv hur många steg du vill förflytta bokstäverna: '))

print('Ordet blir då:')
for bokstav in c:
    print(chr(ord(bokstav) + x))