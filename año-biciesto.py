def año_biciesto(año):
    if isinstance(año,int):
        if año % 4 == 0 and (año % 400 == 0 or año % 100 != 0 ):
            return print('el año es biciesto')
        else:
            return print('el año no es biciesto')
    else:
        return print('ingrese un numero entero')

año_biciesto(2012)