m=[0]*6  #declar matriz con espacio de 6
#paso 3.1
def mitad(x,y):#sacar la mitad
    return  (x+y)/2

#paso 3
def funcion(x):#declarar la funcion
    return  x-3

#paso 2
def tabla():# llenar la tabla
    m[3]=funcion(m[0])
    m[4]=funcion(m[1])
    m[5]=funcion(m[2])
    return 

#paso 1
def asignar():#pedir valores y asignar en las posiciones
    print("Ingresa el valor minimo")
    m[0]=float(input("x= "))
    m[2]=float(input("y= "))
    m[1]=mitad(m[0],m[2])
    return

#paso 4
def signo():
    a=(m[3]*m[4])
    b=(m[5]*m[4])
    if(a>0):
        m[0]=m[1]
    elif(b<0):
        m[0]=m[3]
        return 


def proc():
    e=float(input("|Error|= "))
    print (m)
    while( m[4]<=e or m[5]<=e):
        tabla()
        signo()
        m[1]=mitad(m[0],m[2])
        print (m)

################################################################
print("Funcion x-3=0, Utilizando el Metodo de Diseccion")
##########  metodos #############
asignar()

proc()

