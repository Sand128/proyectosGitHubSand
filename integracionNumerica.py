def funcion(a):
    altura=int(input("Ingresa el valor de x; "))
    print(a)
    c=float(altura*a)
    return c

def sumatoria(Npartes,pi,pf,paso):
    areaT=0
    i=0
    area=[1]*Npartes
    for i in range (Npartes):
        area[i]=float(pow((pi+(i*paso)),2))
        areaT=areaT+area[i]
    sum=areaT*paso
    return sum

print("Integracion Numerica, función x^2")
Npartes=int(input("Ingresa el numero de partes; "))
pi=float(input("Ingresa el Punto Inicial; "))
pf=float(input("Ingresa el Punto Final; "))
paso=float((pf-pi)/Npartes)
a=sumatoria(Npartes,pi,pf,paso)
print("Area bajo la curva es: ",funcion(a))
