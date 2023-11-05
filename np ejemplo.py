import numpy as np

def MatCoef(f,c):
    print("\tMatriz Coeficientes")
    m = [1]*int(f)
    for i in range(f):
        m[i] = [1]*int(c)
        for j in range(c):
            m[i][j]= int(input(">"+str(i)+","+str(j)+" :"))
    print(m)
    return m






    



print("\t¡¡¡¡Bienvenido!!!!\nMetodo de Gauss-Seidel") 
f = input("Cuantas filas tiene tu matriz: ")
c = input("Cuantas columnas tiene tu matriz: ")
MatCoef(f,c)
#P = matriz2(matrizor)
#b = matrizRe(f)
