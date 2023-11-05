def Funcion(x):
    return x-15

def Inicio_algoritmo(Partida, Paso, Error, Av):
    Paso =Av*Paso
    if Av <0:
        Av=Av*(-1)

    m[0][0]=Partida
    m[0][1]=Partida+Paso

    llenar_tabla(Partida,Paso,Error,Av)

def llenar_tabla(Partida, Paso, Error, Av):
    m[1][0]=Funcion(m[0][0])
    m[1][1]=Funcion(m[0][1])
    Comprovar_Error(Partida,Paso,Error,Av)

def Comprovar_Error(Partida,Paso,Error,Av):
    print(m)
    if abs(m[1][0])<=Error:
        Posicion_resultado(0)
    elif abs(m[1][1])<=Error:
        Posicion_resultado(1)
    elif abs(m[1][1])> Error:
        if(abs (m[1][0])-abs(m[1][1]))<0:
            Av=Av*(-1)
        print(Av)
        Inicio_algoritmo(Partida+Paso,Paso,Error,Av)
    
def Posicion_resultado(posi):
    print("El valor de x: es ", end="")
    print(str(m[0][posi]))
    print("El error es: ",end="")
    print(str(m[1][posi]))

print("Metodo de aproximaciones sucesivas para la ecucaion x + 3 = 0") 
m=[0]*2
for i in range(2):
    m[i]=[0]*2

Pp=float(input("Ingresa el Punto de Partida "))
Pas=float(input("Ingresa el paso "))
Er=float(input("Ingresa el error maximo permitido "))
Av =int (1)
Inicio_algoritmo(Pp,Pas,Er,Av)