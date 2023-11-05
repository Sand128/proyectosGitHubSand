def saludo():
    nom=input("escribe tu nombre: ")
    print("Hola "+ nom)

def producto():
    print("Resultado es: ")
    print (8*10*20)

def factorial():
    valor=int(input("Ingresa un valor: "))
    num=1
    i=0
    for i in range(1,valor+1): 
        num=num*i  
    print(num)     
    
def suma():
    num1=int(input("Primer numero: "))
    num2=int(input("segundo numero: "))
    print ( num1+num2)

while True:
    print("\tMenu de opciones")
    print("1.- Saludo")
    print("2.- Producto de 3 numeros")
    print("3.- Fatorial de un numero")
    print("4.- Suma dinamica")
    print("5.- Salir")
    op=input("\tSelecciona una opccion: ")
    if op=="1":
        saludo()
    elif op=="2":
        producto()
        
    elif op=="3":
        factorial()
    elif op=="4":
        suma()
    else:
        print("Error")
        break    



