def KelvinToCelsius(kelvin):
    return kelvin - 273.15

temp = float(input('Ange temperaturen i kelvin: '))
print('Temperaturen är', KelvinToCelsius(temp), 'grader celsius')