tal = int(input('Hur många fibonacci-tal ska max skrivas ut? '))
gräns = int(input('Ange en gräns för högsta talet som får skrivas ut: '))
i = 0
x = 1
y = 1
while i < tal and x <= gräns:
    print(x)
    n = x + y
    x = y
    y = n
    i = i + 1
print('klar')