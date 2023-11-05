try:
    n1=int(input("Dijita el valor del primer número "))
    n2=int(input("Dijita el valor del segundo número "))
    n3=int(input("Dijita el valor del tercer número "))
except ValueError:
    print("No es un numero")
else:
    suma=n1+n2+n3
    print(str(suma))
