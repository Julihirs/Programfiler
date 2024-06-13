def FarenheightToCelsius (Farenheight):
    return Farenheight * (5/9) - 32
Farenheight = float(input('Ange temperaturen i farenhegiht: '))
print('Temperaturen i Celsius är', FarenheightToCelsius(Farenheight))