def  mcd(lista, a):
    cont=0
    divisores=[]
    for i in range(1, lista+1):
        if(lista % i == 0) and (a % i ==0):
            divisores.append(i)
            cont=cont+1
    return divisores

lista=15
a= 10
print(mcd(lista, a))
