i = 0
x = 1
y = 1
while (i < 101):
    i = i + 1
    print(x)
    if i % 20 == 0:
        print(y/x)
    n = x + y
    x = y
    y = n
print('klar')

i = 0
x = 1
y = 1
while (i < 2000):
    i = i + 1
    print(x)
    if i < 1001:
        print(y/x)
    n = x + y
    x = y
    y = n