b1 = bool (False)
b2 = bool (False)
b3 = bool (False)

def Funcion(x):
    #return (x-3)
    return ((x*x)+(x)-15)
    #return (x+8)
    #return (x/4)-2/3
    #return(x/3)+8-5

def Mitad (a,b):
    return (a+b)/2

def Obtener_posiciones():
    if (b1):
        m[0] = m [0]
        m[2] = m [1]

    elif (b2):
        m[0] = m [1]
        m[2] = m [2]

def Comparar_error():
    global b3

    if abs(m[3]) < Er:
        b3 = True
    elif abs(m[4]) < Er:
        b3 = True
    elif abs(m[5]) < Er:
        b3 = True

def Valores_iniciales():
    m[0] = float(input("Ingresa el limite inferior: "))
    m[2] = float(input("Ingresa el limite superior: "))

def Llenar_tabla():
    m[3] = Funcion(m[0])
    m[4] = Funcion(m[1])
    m[5] = Funcion(m[2])

def Comparar_signos():
    global b1
    global b2

    if m[3] * m[4] < 0 :
        b1 = True
    else:
        b1 = False

    if m[4] * m[5] < 0 :
        b2 = True
    else:
        b2 = False

def Posicion_resultado():
    print("El valor de x es: ", end = " ")
    print (str(m[1]))
    print ("El error es: ", end = " ")
    print (str(m[4]))

def Control_flujo():
    while not(b3):
        m[1] = Mitad (m[0], m[2])
        Llenar_tabla()
        Comparar_error()
        Comparar_signos()
        print(m)
        Obtener_posiciones()
    Posicion_resultado()

print ("Estás utilizando el método de Bisección para resolver x+3=0")
m = [0] * 6
Er = float(input("Ingresa el error máximo permitido para el resultado: "))

Valores_iniciales()
Control_flujo()