def tal(heltal):
    return heltal % 2

heltal = int(input('Skriv ett heltal: '))
if tal(heltal) == 0:
    print('Talet är jämnt')
else:
    print('Talet är udda')