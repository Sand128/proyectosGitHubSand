#crear un arreglo donde le indiques el tamaño por teclado y crear una funcion que rellene al arreglo
#con los multipoos de un numero solicitado por teclado.
tam=int(input("Tamaño del arreglo: "))
valor=int(input("Ingresa el numero: "))
arreglo=[]
for i in range(0 ,tam):
    arreglo.append( i * valor)
    print (arreglo)



