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
    mat=np.array(np.linalg.inv(N))
    return mat

def matriz2 (mat):
    f=len(np.array( mat))
    P = [0]*int(f)
    for i in range(f):
        P[i] = [1]*int(f)
        for j in range(f):
            if i>=1 and j<i:
                P[i][j]=mat[i][j]
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

def sustitucion (op3):
    f=len(np.array(op3))
    sus = [1]*int(f)
    for i in range(int(f)):
        sus[i] = [1]*int(1)
        sus[i][0]=op3
    return sus


def menu():
    num=int(input("[1. para Salir]\n\tMenu...\nIngresa la long de la Matriz: "))
    l=1
    if num==1:
        print("Gracias, Adios")  
    else:
            matriz_ceros = np.zeros([num,1])
            M= matrizCo(num)
            N = np.array(matriz1(M))
            P = np.array(matriz2(M))
            b = np.array(matrizRe(num))
            print ("\nValores de la multiplicación")
            n =int (input("Ingresa el numero Iteraciones: "))
            if n>0:
                op1=np.dot(N,b)
                op2=np.dot(N,P)
                op3=op1+(np.dot(op2,matriz_ceros))
                print(op3)               
                while l <= n:
                    print(op3)
                    result=np.dot(M,op3)
                    print(result)
                    if (result == b).all():
                        print(result)
                        break
                    else:
                        print(" \t\tIteracion",l)
                        op4=op1+(np.dot(op2,op3))
                        op3=op4
                        print(op4)
                        #los resultados de la iteracion se sustitullen en la matris original ya que son x,y u z
                        #con una condicional que se detenga cuando se aproxcime al resultado matrizRe
                        l+=1  




    
print("¡¡¡¡Bienvenido!!!!") 
menu()


