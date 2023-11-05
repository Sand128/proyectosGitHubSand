def pantalones():
    x=float(input("Ingresa el precio del Pantalon: "))
    y=(x*0.10)
    print("Presio original: ")
    print(x)
    print("Descuento 10%\nPrecio con Descuento: ")
    Y=x-y
    print(Y)
    descuento(Y,x)

def camisetas():
    x=float(input("Ingresa el precio de la Camisa: "))
    y=(x*0.05)
    print("Presio original: ")
    print(x)
    print("Descuento 5%\nPrecio con Descuento: ")
    Y=x-y
    print(Y)
    descuento(Y,x)

def chaquetas():
    x=float(input("Ingresa el precio de la Chaqueta: "))
    y=(x*.20)
    print("Presio original: ")
    print(x)
    print("Descuento 20%\nPrecio con Descuento: ")
    Y=x-y
    print(Y)
    descuento(Y,x)
    
def zapatos():
    x=float(input("Ingresa el precio de los Zapatos: "))
    y=(x*0.15)
    print("Presio original: ")
    print(x)
    print("Descuento 15%\nPrecio con Descuento: ")
    Y=x-y
    print(Y)
    descuento(Y,x)

def descuento(Y,x):
    if Y>50 :
        print("Grande")
    elif Y>25 and Y <50:
        print("Mediana")
    elif Y<25:
        print("Chico")   

def menu():
    while True:
        print("Calculadora de Descuentos y Tallas en una Tienda  de Ropa\n1.Pantalones\n2.Camisetas\n3.Chaquetas\n4.Zapatos\n5.Salir")
        op=input("Selecciona una opcion(1/2/3/4/5): ")
        if op=="1":
            pantalones()
        elif op=="2":
            camisetas()
        elif op=="3":
            chaquetas()
        elif op=="4":
            zapatos()
        elif op=="5":
            print("saliendo del programa \n")
            break
        else:
            print("error")


menu()           