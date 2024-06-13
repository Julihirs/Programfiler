tal = int(input('Hur många fibonacci-tal ska skrivas ut? '))
i = 0
x = 1
y = 1
while (i < tal):
    print(x)
    n = x + y
    x = y
    y = n
    i = i + 1
print('klar')