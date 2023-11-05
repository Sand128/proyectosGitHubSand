#crear arreglos vaíos para su uso
nombre=[]
identificadores=[]
#definir tamaño de los arreglos
taman=3
#leer los datos y agregrlos al arreglo
for i in range(taman):
    print("Ingrese datos de la primera persona",i+1)
    nomb=input("nombre: ")
    identificador=input("identificacion: ")
    nombre.append(nomb)
    identificadores.append(identificador)
#mostrar los datos del arreglo
for i in range(taman):
    print("Mostrando los datos de la persona ",i+1)
    print("nombre:" +nombre[i])
    print("identificaion: ", identificadores[i])
