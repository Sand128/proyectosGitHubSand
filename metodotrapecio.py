import math
def funcion(a):
    c=(pow(a,3)+2)
    return c

def funcionIntegral(pi,pf):
    a=(((pow(pf,4)/4)+2*pf))
    b=(((pow(pi,4)/4)+2*pi))
    return a-b

def proecedimiento(pi,pf):
    Area=0
    suma=0
    i=0
    Npartes=int(input("Ingresa el numero de partes; "))
    paso=float((pf-pi)/Npartes)#paso=base
    print("(pf-pi)/n=paso\n",(pf-pi),"/",Npartes,"=",paso)
    a=funcion(pi)
    b=funcion(pf)
    #print("paso ",paso)
    print("puntos f(pi)=",a," f(pf)",b)
    res=pow((pf-pi),2)+pow((b-a),2)#siguiendo la formula para calcular la distanca, res=operacion dentro de la raiz
    distancia=(math.sqrt(res))#calcular la distancia sacando la raiz de res
    print("distancia del pi al pf = ",distancia)
    for i in range(Npartes):
        area=(Area+(i*paso))
        Area=area
        print(Area)
        suma=Area+suma
    print(suma," la suma de xn")
    resultado= paso*((a/2)+(b/2)+suma)
    return resultado


print("Metodo del trapecio:  x^3+2")
pi=float(input("Ingresa el Punto Inicial; "))
pf=float(input("Ingresa el Punto Final; "))
print("Resultado de la integral x^3+2, del punto ",pi," al ",pf," = ",funcionIntegral(pi,pf))
resultado=proecedimiento(pi,pf)
print("Area bajo la curva es: ",resultado)

