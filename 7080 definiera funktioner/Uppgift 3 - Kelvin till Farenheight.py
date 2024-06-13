def KelvinTofarenheight (Kelvin):
    return (Kelvin - 273.15) * (9/5) + 32

Kelvin = float(input('Skirv din temperatur i Kelvin: '))
print('Din temperatur i farenheight är', KelvinTofarenheight(Kelvin))