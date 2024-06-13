# 4A
text = input('Skriv din text: ')

for bokstav in text:
    print(chr(ord(bokstav) + 1))

print()

# 4B
for bokstav in text:
    print(chr(ord(bokstav) - 1))

print()

# 4C
for bokstav in text:
    print(chr(ord(bokstav) + 2))