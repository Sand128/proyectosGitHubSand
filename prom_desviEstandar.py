#import statistics as stats
from math import sqrt
import numpy as np
def promedio_std(lista):
    nwlista=[]
    n=len(lista)
    sum=0
    for elem in lista:
        sum=elem+sum
    #print(sum)
    x=sum/n#promedio listo y tambien U para la desviacion estandar
    #print(x)
    for elem in lista:
        nwlista.append((elem-x)*(elem-x))
    #print(np.sum(nwlista))  
    a=(np.sum(nwlista))/n
    #print(a)
    y=sqrt(a)
    return(x,y)
lista = [81, 14, 45, 72, 57, 15, 67, 80, 40, 46, 19, 76, 87, 33, 56]
print(len(lista))
print(promedio_std(lista))



"""
Con lista = [81, 14, 45, 72, 57, 15, 67, 80, 40, 46, 19, 76, 87, 33, 56]
promedio_std(lista) debió entregar 52.533 y 23.916, pero entregó 52.533 y 40257.383 
Vuelve a intentarlo!

"""