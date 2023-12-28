#import statistics as stats
import math
import numpy as np
def promedio_std(lista):
    nwlista=[]
    n=len(lista)
    sum=0
    for elem in lista:
        sum=elem+sum
    x=sum/n#promedio listo y tambien U para la desviacion estandar
    for elem in lista:
        nwlista.append(pow(2,(elem-x)))
    print(np.sum(nwlista))  
    a=(np.sum(nwlista))/n
    y=a**0.5
    return(x,y)
lista=[10,9,8,7.5,6,10,9,7.8]
print(len(lista))
print(promedio_std(lista))