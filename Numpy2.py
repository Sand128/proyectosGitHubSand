#libreria
import numpy as np

def matriz1 (f):
    print("\tMatriz N")
    m1 = [1]*int(f)
    for i in range(f):
        m1[i] = [1]*int(f)
        for j in range(f):
            m1[i][j]= int(input("Ingresa el valor del elemento "+str(i)+","+str(j)+" :"))
    print(m1)
    print(np.linalg.inv(m1))
    return m1

def matriz2 (f):
    print("\tMatriz P")
    m2 = [1]*int(f)
    for i in range(f):
        m2[i] = [1]*int(f)
        for j in range(f):
            m2[i][j]= int(input("Ingresa el valor del elemento "+str(i)+","+str(j)+" :"))
    print(m2)
    print(np.linalg.inv(m2))
    #return m2

def matrizIn (f):
    m = [1]*int(f)
    for i in range(int(f)):
        m[i] = [1]*int(1)
        m[i][0]= int(input("Ingresa el valor del elemento "+str(i)+","+str(0)+" :"))
    return m

def menu():
    num=int(input("\tMenu...\n1.Matriz la matriz puede ser de 2x2,3x3 y 4x4, 0. para Salir: "))
    A = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
    l=0
    if num==0:
        print("Gracias")   
    elif num==2 or num==3 or num==4:
            print("Matriz ",num)
            # Creación de una matriz num x 1 de ceros
            #matriz_ceros = np.zeros([num,1])
            # Creacion de iteraciones
            N = np.array(matriz1(num))
            P = np.array(matriz2(num))
            b = np.array(matrizIn(num))
            print ("\nValores de la multiplicación")
            n =int (input("ingresa el numero Iteraciones =< 9 :"))
            if n <=9 or n>0:
                while l <= n:
                    
                    op1=np.array(np.dot((np.linalg.inv(N)),b))
                    op2=np.array((np.dot((np.linalg.inv(N)),P)))
                    op3=np.array(op1+(np.dot(op2,A[0][l])))
                    print(op3)
                    l+=1 
            else: 
                print("Error")     

            
            
print("¡¡¡¡Bienvenido!!!!") 
menu()

# op1=np.array(np.dot((np.linalg.inv(N)),b))
#             op2=np.array((np.dot((np.linalg.inv(N)),P)))
#             #op3=np.array(op1+(np.dot(op2,matriz_ceros)))
#             op3=np.array(op1+(np.dot(op2,A[0][n])))
#             print(op3)   """


""" import numpy as np
l=0
n =int (input("ingresa el numero Iteraciones =< 9 :"))
#matriz=[l,l,l]
if n <=9 or n>0:
    while l <= n:   
        matriz=[l,l,l]
        x = np.array(matriz)
        print(x)
        l+=1
print(l)
 """
