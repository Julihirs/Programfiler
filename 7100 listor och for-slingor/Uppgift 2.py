def primtal(x):
    if x <= 1:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

lista_primtal = []

for tal in range(2, 100):
    if primtal(tal):
        lista_primtal.append(tal)

print(lista_primtal)