""" def funcion(num):
    c=pow(num,2)
    return c
 """
def funcion(num):
    c=num+2
    return c

def derivacion(c):
    h=float(input("Valor de h: "))
    a=(c-2*(h))
    b=4*(c-h)
    f=(a-b+(3*c))/(2*h)
    return f

num=float(input("Funcion x^2\nIngresa el valor de x: "))
a=funcion(num)
print(derivacion(a))

