edades=[22,22,19,25]
#recorrer elementos posiciones del arreglo
for edad in edades:
    print(edad)
#recorrer indices del arreglo
for i in range(len(edades)):
    print(edades[i])
#recorrer posiciones del arreglo con while
indice=0
while indice < len (edades):
    print(edades[indice])
    indice += 1
#agregar datos al arreglo de forma estatica
numero=[]
numero.append(20)
numero.append(60)
numero.append(15)
numero.append(18)
numero.append(22)
numero.append(77)
print(numero)
#unir datos a una lista superando la funcion append
numero1=[]
numero1=numero1+[1,2,3,4,5,6,7,8,9]
print(numero1)
#remover datos de un arreglo utilizando la funcion pop
saludo=["hola","holis","que onda"]
saludo.pop(1)#borrar posicion
print(saludo)
#eliminar elementos de una posicion utilizando la funcion pop
saludo1=["hola!","holis!","que ondas!","que hubo!","que tranza!","que onda!"]
saludo1.remove("que onda!")#borrar posicion
print(saludo1)