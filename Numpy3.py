#libreria
import numpy as np
def matrizCo (f):
    print("\tMatriz Coeficientes")
    m = [1]*int(f)
    for i in range(f):
        m[i] = [1]*int(f)
        for j in range(f):
            m[i][j]= int(input(">"+str(i)+","+str(j)+" :"))
    return m


def matriz1 (mat):
    f=len(np.array( mat))
    N = [0]*int(f)
    for i in range(f):
        N[i] = [1]*int(f)
        for j in range(f):
            if i>=1 and j<i:
                N[i][j]=0
            else:
                N[i][j]=mat[i][j]
    N=np.array(np.linalg.inv(N))
    return N

def matriz2 (mat):
    f=len(np.array( mat))
    P = [0]*int(f)
    for i in range(f):
        P[i] = [1]*int(f)
        for j in range(f):
            if i>=1 and j<i:
                P[i][j]=(mat[i][j])*(-1)
            else:
                P[i][j]=0    
    return P

def matrizRe (f):
    print("Resultados")
    m = [1]*int(f)
    for i in range(int(f)):
        m[i] = [1]*int(1)
        m[i][0]= int(input("<"+str(i)+","+str(0)+" :"))
    return m

def menu():
    num=int(input("[1. para Salir]\n\tMenu...\nIngresa un numero para las columnas y filas de la Matriz: "))
    l=1
    if num==1:
        print("Gracias, Adios")  
    else:
            matriz_ceros = np.zeros([num,1])
            # Creacion de iteraciones
            M = matrizCo(num)
            N = np.array(matriz1(M))
            #print("Matriz N\n",N)
            P = np.array(matriz2(M))
            #print("Matriz P\n",P)
            b = np.array(matrizRe(num))
            #print("Matriz b\n",b)
            print ("\nValores de la multiplicación")
            n =int (input("Ingresa el numero Iteraciones: "))
            #lim=float(input("limite: "))

            if  n>0:
                op1=np.dot(N,b)#primera operacion
                op2=np.matmul(N,P)#ó op2=P@N 
                #print(op2)
                op3=op1+(np.dot(op2,matriz_ceros))
                print(op3)
                while l <= n:  
                    newmatR=op1+(np.dot(op2,op3))
                    print(op3)
                    #con=(np.subtract(b,newmatR))
                    con=np.allclose(op3,newmatR)
                    if con == True:
                        op3=newmatR
                        l+=1
                        print(con)
                    else:
                        print(op3)
                        con==True
                        print("\t\t",con)
                        break

print("¡¡¡¡Bienvenido!!!!") 
menu()