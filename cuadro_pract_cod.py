def si(a):
    if a<18:
        return "Es menor de edad"

def sino(a):
    if a<18:
        return "Es manor de edad"
    else:   
        return "es mayor de edad"
    
def mientras():
    i=0
    x=1
    while i<=4:
        x=x*2
        i+=1
    return x

def mientras_que():
    return

def para():
    a=0
    for i in range(3):
        a=a+1
    return a

def dividir(num,div):
    return num/div
def m_ex(a,b):
    print("manejo de excepciones:\n ingresa dos valores para la divicion")
    a=input
    b=input
    try:
        res=dividir(a,b)
    except ZeroDivisionError:
        print("Trataste de dividir entre cero :( ") 

def segun(decimal):

    if decimal == '0':
        return "000"
    elif decimal == '1':
        return "001"

tabla_switch = {
        '0': '000',
        '1': '001',
}

def segun2(decimal):
    return tabla_switch.get(decimal, "NA")

def menu():
    while True:
        opcion=input("Python \n\tMenu\n1.if\n2.elif\n3.while\n4.do while\n5.for\n6.try\n7.switch\nseleciona una opcion: ")

        if opcion=="1":
            edad=18
            print("Condicional\n",si(edad))
            
        elif opcion=="2":
            edad=18
            print("Condicional con 2 resultados\n",sino(edad))
            
        elif opcion=="3":
            print("Ciclo i=0 y x=1\n",mientras())

        elif opcion=="4":
            print("No hay ejercicio")

        elif opcion=="5":
            print("Ciclo para\n a=0 hasta 3",para())

        elif opcion=="6":
            m_ex()
        
        elif opcion=="7":
            num=int(input("ingresa un valor [1 ó 0]\nmetodo 1 ",segun(num),"\nmetodo 2 ",segun2(num)))          

        else:
            print("gracias")
            break

menu()
    

