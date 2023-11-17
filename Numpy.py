import numpy as np
#matriz sistemas
f = input("Cuantas filas tiene tu matriz: ")
c = input("Cuantas columnas tiene tu matriz: ")

m = [1]*int(f)

for i in range(int(f)):
    m[i] = [1]*int(c)

for i in range(int(f)):
    for j in range(int(c)):
        m[i][j]= int(input("Ingresa el valor del elelemto "+str(i)+","+str(j)+" :"))
        
print(m)
print("Inversa de la matriz 1")
print (np.linalg.inv(m))
m_inv=np.linalg.inv(m)
print(np.dot(m, m_inv))




Matriz1 = np.array(m)#np es un objeto. y el array que se maneja un objeto
#matriz columna de los terminos independientes
ff = input("Cuantas filas tiene tu matriz: ")
cc = input("Cuantas columnas tiene tu matriz: ")

mm = [1]*int(ff)

for i in range(int(ff)):
    mm[i] = [1]*int(cc)

for i in range(int(ff)):
    for j in range(int(cc)):
        mm[i][j]= int(input("Ingresa el valor del elelemto "+str(i)+","+str(j)+" :"))
        
print(mm)

Matriz2 = np.array(mm)

print("\n")
#print (np.linalg.inv(m))#objeto, inversa a la matriz1
print ("valores de la multiplicación")

print(np.dot(np.linalg.inv(m),mm))#objeto,multplicaion