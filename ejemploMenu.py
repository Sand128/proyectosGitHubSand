#PROGRAMA PARA REALIZAR UN MENU EN PYTOHN
def nombre():
    print("Seleccionaste la primer opcion\n")
    #agregar todo el codigo que sea necesario para ejecutar la primer opcion
    nombre="sand"
    print(nombre)
def nombre2():
    print("Seleccionaste la segunda opcion\n")
    nomb=input("¿Cual es tu nombre?\n")
    print(nomb)
while True:
    #mostar opciones al usuario en pantalla
    print("Menu de opciones")
    print("1.... nombre estatico")
    print("2.... nombre solicitado")
    print("3.... salir")
    #ejecuta la eleccion del usuario
    eleccion=input("selecciona una opcion :\n")
    #comparar la eleccion del usuario
    if eleccion=="1":
        nombre()
    elif eleccion=="2":
        nombre2()
    elif eleccion=="3":
        print("saliendo del programa \n")
        break
    else:
        print("error")
    