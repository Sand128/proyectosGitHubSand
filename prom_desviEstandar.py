from math import sqrt
import numpy as np
def promedio_std(lista):
    n=len(lista)
    sum=0
    for elem in lista:
        sum=elem+sum
    x=sum/n#promedio listo y tambien U para la desviacion estandar
    z=0
    for elem in lista:
        a=(elem-x)*(elem-x)
        z=z+a
    b=z/n
    y=b**0.5
    return(x,y)
lista = [81, 14, 45, 72, 57, 15, 67, 80, 40, 46, 19, 76, 87, 33, 56]
print(promedio_std(lista))


"""
Con lista = [81, 14, 45, 72, 57, 15, 67, 80, 40, 46, 19, 76, 87, 33, 56]
promedio_std(lista) debió entregar 52.533 y 23.916, pero entregó 52.533 y 40257.383 
Vuelve a intentarlo!

"""