import numpy as np
lista = []
def llenar():
    nm=True
    cont=1
    print("Para salir de la lista ingresa 000")
    while (nm == True):
        num=input("Ingresa un valor: ")
        if num =="000":
            nm=False
        else:
            lista.append(num)
            cont=cont+1
    return 
def mostrar():
    print(lista)
def calcular():
    n=len(lista)
    suma=sum(int(num) for num in lista)
    promedio=suma/n
    return "El promedio de la lista es "+promedio
def ordenar():
    newlist=[]
    for num in lista[::-1]:
        newlist.append(num)
    return newlist
def menulista():
    print("\t****Menu1****")
    opc=True
    while(opc==True):
        print("""
            1.-LLenar lista
            2.-Mostrar lista
            3.-Calcular promedio
            4.-Ordenar lista de forma ascendente
            5.-Salir
                """)
        op=int(input("selecciona una opcion: "))
        if op==1:
            llenar()
        elif op==2:
            mostrar()
        elif op==3:
            print(calcular())
        elif op==4:
            print(ordenar())
        else:
            print("........................................\n\tGracias")
            opc=False
listanombre=list()
listanumeros=list()
def agregar(a,b):
    listanombre.append(a)
    listanumeros.append(b)
    return
def mostrarcont():
    print("****************\nLista de contactos\nNombre\tNumero")
    for nom, num in sorted(set(zip(listanombre,listanumeros))):
        print(nom,"\t",num)
def buscar(a):
    nom=a
    if nom in listanombre:
        lugar=listanombre.index(nom)
        print("Si existe "+nom+" numero ",listanumeros[lugar-1])
    else:
        print("No se encuentra.")
    return

def menugestion():
    print("\t****Menu2****")
    opc=True
    while(opc==True):
        print("""
            1.-Agregar un nuevo contacto
            2.-Mostrar todos los contactos
            3.-Buscar un contacto por nombre
            4.-Salir
                """)
        op=int(input("selecciona una opcion: "))
        if op==1:
            nombre=input("Ingresa el nombre de tu contacto: ")
            numero=int(input("Ingresa el numero de "+nombre+": "))
            agregar(nombre,numero)
        elif op==2:
            print(mostrarcont())
        elif op==3:
            nombre=input("Busco a : ")
            print(buscar(nombre))
        else:
            print("........................................\n\tGracias")
            opc=False



print("\t****Menu****")
opc=True
while(opc==True):
    print("""
        1.-Operaciones con listas
        2.-Gestion de contactos
        3.-Salir
            """)
    op=int(input("selecciona una opcion: "))
    if op==1:
        menulista()
    elif op==2:
        menugestion()
    else:
        print("........................................\n\tGracias")
        opc=False



