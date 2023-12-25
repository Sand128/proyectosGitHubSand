import math
def funcion1(x):
    c=(pow(x,3)+2)
    return c

def funcionIntegral(pi,pf):
    a=(((pow(pf,4)/4)+2*pf))
    b=(((pow(pi,4)/4)+2*pi))
    return a-b

def funcionseno(x):
    c=math.sin(x)
    return c

def funcionsenoIntegral(pi,pf):
    a=math.cos(pf)
    b=math.cos(pi)
    return b-a

def funcionE1(x):
    i=0
    b=0
    sum=0
    for i in range(0):
        c=1/((calculaFactorial(i))*((2*i)+1))
        b=c
        sum=sum+b
    return sum

def funcionE2(x):
    i=0
    b=0
    sum=0
    for i in range(11):
        c=1/((calculaFactorial(i))*((2*i)+1))
        b=c
        sum=sum+b
    return sum

def calculaFactorial(n):
    if n>0:
        n = n * calculaFactorial(n - 1)
    else:
        n = 1
    return n

def funcion2(x):
    c=pow(x,-2)
    return c

def funcion2Integral(pi,pf):
    a=pow(pi,-2)
    b=pow(pf,-2)
    return b-a

def funcionxsenx(x):
    c=x*(math.sin(x))
    return c

def funcionxsenxIntegral(pi,pf):
    a=pi*(math.sin(pi))
    b=pf*(math.sin(pf))
    return b-a

def menu():
    print("\tMenu")
    print("""1.-Metodo del trapecio:  x^3+2
             2.-Metodo del trapecio: sen x
             3.-Metodo del trapecio: e^(x^2)
             4.-Metodo del trapecio: x^-2
             5.-Metodo del trapecio: x sen x  """)
    op=int(input("Elige una funcion: "))
    if op==1:
        funcion1()
    elif op==2:
        funcionseno()



def proecedimiento(pi,pf):
    Area=0
    suma=0
    i=0
    Npartes=int(input("Ingresa el numero de partes; "))
    paso=float((pf-pi)/Npartes)#paso=base
    print("(pf-pi)/n=paso\n",(pf-pi),"/",Npartes,"=",paso)
    #a=funcion1(pi)
    #b=funcion1(pf)
    #a=funcionseno(pi)
    #b=funcionseno(pf)
    #a=funcionE1(pi)
    #b=funcionE2(pf)
    #a=funcion2(pi)
    #b=funcion2(pf)
    a=funcionxsenx(pi)
    b=funcionxsenx(pf)
    print("puntos f(pi)=",a," f(pf)",b)
    res=pow((pf-pi),2)+pow((b-a),2)#siguiendo la formula para calcular la distanca, res=operacion dentro de la raiz
    distancia=(math.sqrt(res))#calcular la distancia sacando la raiz de res
    print("distancia del pi al pf = ",distancia)
    for i in range(Npartes):
        area=(pi+(i*paso))
        Area=area
        #print(i,"",Area)
        suma=Area+suma
    print(suma," la suma de xn")
    print(paso*((a/2)+(b/2)+funcionxsenx(suma)))
    resultado= paso*((a/2)+(b/2)+suma)

    return resultado


#menu()
pi=float(input("Ingresa el Punto Inicial; "))
pf=float(input("Ingresa el Punto Final; "))
print("Resultado de la integral del punto ",pi," al ",pf," = ",funcionxsenxIntegral(pi,pf))
#print("Resultado de la integral del punto ",pi," al ",pf," = ",funcion2Integral(pi,pf))
#print("Resultado de la integral del punto ",pi," al ",pf," = ",funcionsenoIntegral(pi,pf))
#print("Resultado de la integral del punto ",pi," al ",pf," = ",funcionIntegral(pi,pf))
resultado=proecedimiento(pi,pf)
print("Area bajo la curva es: ",resultado)

