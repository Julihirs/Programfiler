def KelvinTofarenheight (Kelvin):
    return (Kelvin - 273.15) * (9/5) + 32

def KelvinToCelsius(Kelvin):
    return Kelvin - 273.15

def FarenheightToCelsius (Farenheight):
    return Farenheight * (5/9) - 32

def FarenheightToKelvin(Farenheight):
    return Farenheight * (5/9) - 32 + 273.15

def CelsiusToFarenheight(Celsius):
    return Celsius*(9/5) + 32

def CelsiusToKelvin(Celsius):
    return Celsius + 273.15

svar = input('Vilken temperaurenhet använder du: farenheight, celsius eller kelvin?\nSkriv ditt svar: ')
if svar == 'farenheight':
    svar2 = input('Till vilken temperatur vill du skriva om till: farenheight, celsius eller kelvin?\nSkriv ditt svar: ')
    if svar2 == 'celsius':
        Farenheight = float(input('Ange temperaturen i farenhegiht: '))
        print('Temperaturen i celsius är', FarenheightToCelsius(Farenheight))
    elif svar2 == 'kelvin':
        Farenheight = float(input('Ange temperaturen i farenheight: '))
        print('Temperaturen i kelvin är', FarenheightToKelvin(Farenheight))
    else:
        print('Inget att göra om!')
elif svar == 'celsius':
    svar2 = input('Till vilken temperatur vill du skriva om till: farenheight, celsius eller kelvin?\nSkriv ditt svar: ')
    if svar2 == 'farenheight':
        Celsius = float(input('Skriv temperaturen i celcius: '))
        print('Temperaturen i farenheight är', CelsiusToFarenheight(Celsius))
    elif svar2 == 'kelvin':
        Celsius = float(input('Skriv din temperatur i celsius: '))
        print('Temperaturen i kelvin är', CelsiusToKelvin(Celsius))
    else:
        print('Inget att göra om!')
elif svar == 'kelvin':
    svar2 = input('Till vilken temperatur vill du skriva om till: farenheight, celsius eller kelvin?\nSkriv ditt svar: ')
    if svar2 == 'celsius':
        Kelvin = float(input('Skriv din temperatur i kelvin: '))
        print('Din temperatur i celsius är', KelvinToCelsius(Kelvin))
    elif svar2 == 'farenheight':
        Kelvin = float(input('Skriv din temperatur i kelvin: '))
        print('Din temperatur i farenheight är', KelvinTofarenheight(Kelvin))
    else:
        print('Inget att göra om till!')
else:
    print('Huh?')