def color_frecuente (lista):
    nwcolor=[]
    n=len(lista)
    for colores in sorted(set(lista)):
        a=(lista.count((colores)))
        nwcolor.append([colores,a])
    mensaje=nwcolor.pop()
    return  mensaje   
lista=['azul', 'rojo', 'verde', 'verde', 'verde', 'rojo', 'verde', 'verde', 'azul', 'amarillo', 'azul', 'azul', 'verde', 'verde', 'verde', 'amarillo', 'amarillo']
print(color_frecuente(lista))