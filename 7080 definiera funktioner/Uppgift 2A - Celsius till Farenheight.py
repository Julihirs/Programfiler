def CelsiusToFarenheight(Celsius):
    return Celsius*(9/5) + 32

Celsius = float(input('Skriv temperaturen i celcius: '))
print('Temperaturen i Farenheight är', CelsiusToFarenheight(Celsius))