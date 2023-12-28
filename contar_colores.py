def color_frecuente (lista):
    nwcolor=[]
    nwcolor2=[]
    cont=0
    print(len(lista))
    for colores in sorted(set(lista)):
        nwcolor.append(colores)
        nwcolor2.append(lista.count((nwcolor[cont])))
        cont=cont+1
    lista1=nwcolor+nwcolor2
    print(nwcolor2)
    return  ""+max(lista1)


    
#mensaje="hay {} elementos coincidentes".format((nwcolor2[0]))
#print(lista.count("azul"))   contar el numero de repeticiones dentro de la lista
    
lista=['azul', 'rojo', 'verde', 'verde', 'verde', 'rojo', 'verde', 'verde', 'azul', 'amarillo', 'azul', 'azul', 'verde', 'verde', 'verde', 'amarillo', 'amarillo']
print(color_frecuente(lista))