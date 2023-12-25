import numpy as np

def matrizCo (f):
    print("\tMatriz Coeficientes")
    m = [1]*int(f)
    for i in range(f):
        m[i] = [1]*int(f)
        for j in range(f):
            m[i][j]= float(input(">"+str(i)+","+str(j)+" :"))
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

def sustitucion (n):
    f=len(np.array(n))
    sus = [1]*int(f)
    for i in range(int (f)):
        sus[i]=[1]*int (1)
        sus[i][0]= n[i][0]
    return sus

def Matrizresultados(Mcoe,n):
    m1=np.array(Mcoe)
    m2=np.array(n)
    m=np.dot(m1,m2)
    return m



def menu():
    l=1
    num=int(input("[1. para Salir]\n\tMenu...\nIngresa la long de la Matriz: "))
    if num==1:
        print("Gracias, Adios")  
    else:
            matriz_ceros = [0,0,0]
            M= np.array(matrizCo(num))#print(M)
            N = np.array(matriz1(M))#print(N)
            P = np.array(matriz2(M))# print(P)
            b = np.array(matrizRe(num))# print(b)
            n=int(input("Numero de iteraciones: "))
            l=1
            if  n>0:
                print ("\nValores de la multiplicación")
                op1=np.dot(N,b)#print(op1)
                op2=np.dot(N,P)#print(op2)
                op3=np.dot(op2,matriz_ceros)#op3=op1+(np.dot(op2,matriz_ceros))
                print("Valores de X,Y y Z\n",np.array(op3),"\n")#print(op3)
                op4=op1+op3#print(op4)
                op4=sustitucion(op4)#valores 
                print("Valores de X,Y y Z\n",np.array(op4))#muestra los resultados de la primera operacion
                x= np.array(Matrizresultados(M,op4))#multiplica los resultados op4 sustituyendolos en la funcion matrizCo (f):
                print("Sustitucion en la ecuacion,\tIteracion #",l,"\n",np.array(sustitucion(x)))
                #print("Sustitucion en la ecuacion,\tIteracion #",l,"\n",np.array(np.dot(M,x)))
                while l<=n:
                    l+=1
                    op1=np.dot(N,x)
                    op3=np.dot(op2,op4)
                    op4=op1+op3
                    #print("op3\n",op3)
                    op4=sustitucion(op4)
                    #print("op4\n",op4)
                    print("Valores de X, Y y Z\n",np.array(sustitucion(op4)))
                    x= np.array(Matrizresultados(M,op4))
                    print("Sustitucion en la ecuacion,\tIteracion #",l,"\n",np.array(sustitucion(x)))
                     
print("¡¡¡¡Bienvenido!!!!") 
menu()



