def suma(n):
    num=0
    i=0
    for i in range(i,n+1): 
        if i%2 ==0: 
            num=num+i
    print("La suma de los numeros pares desde 2 hasta ")
    print(n)         
    print("es: ")
    print(num)

print("Suma de numeros pares enteros")
n=int(input("Ingresa un numero entoro positivo: "))
suma(n)