def funcion(a):
    #c=float(pow(a,3)-6*(pow(a,2))+(11*a)-6)
    #c=float(pow(a,2)+10*a)
    #c=float(pow(a,2))
    #c=float(pow(a,3)+5*a)
    c=float(a)
    return c

def sumatoria(pi,pf):
    Area=0
    i=0
    Npartes=int(input("Ingresa el numero de partes; "))
    paso=float((pf-pi)/Npartes)#paso=base
    a=funcion(pi)
    b=funcion(pf)
    resta=pf-pi
    print("paso ",paso)
    print("pf-pi= ",resta)
    print("puntos pi,pf ",a," y ",b)
    for i in range(Npartes-1):
        area=(pi+(i*paso))
        Area=area+Area
    resultado= paso*((a/2)+(b/2)+Area)
    return resultado

#print("Metodo del trapecio:  x^3-6x^2+11x-6")
#print("Metodo del trapecio:  x^2+10x")
#print("Metodo del trapecio:  x^2")
#print("Metodo del trapecio:  x^3+5x")
print("Metodo del trapecio:  x")


pi=float(input("Ingresa el Punto Inicial; "))
pf=float(input("Ingresa el Punto Final; "))

resultado=sumatoria(pi,pf)
print("Area bajo la curva es: ",resultado)

