#def dividir(a,b):
#    if b == 0:
#        return None
#    return a/b

def dividir(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print('no se puede dividir entre ceros')

num1 = int(input('ingrese un numero: '))
num2 = int(input('ingrese un numero: '))
print(dividir(num1, num2))