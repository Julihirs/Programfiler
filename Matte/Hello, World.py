def f(x):
    return x**3 + 3*x + 5

def f_prim(a):
    h = 0.00000000001
    return (f(a+h)-f(a)) / h

a = 2

print("f'(2) är ungefär", f_prim(a))