def color_frecuente (lista):
    nwcolor=[]
    for colores in sorted(set(lista)):
        a=(lista.count((colores)))
        nwcolor.append([a,colores])
    mensaje=max(nwcolor)
    return mensaje
lista =['amarillo', 'amarillo', 'amarillo', 'amarillo', 'amarillo', 'rojo', 'azul', 'verde', 'verde', 'azul', 'azul', 'amarillo', 'azul', 'azul', 'azul', 'amarillo', 'azul', 'azul', 'azul', 'azul', 'amarillo', 'azul', 'amarillo', 'rojo', 'azul', 'azul', 'azul', 'amarillo', 'rojo']
print(color_frecuente(lista))


"""
Con lista = ['amarillo', 'amarillo', 'amarillo', 'amarillo', 'amarillo', 'rojo', 'azul', 'verde', 'verde', 'azul', 'azul', 'amarillo', 'azul', 'azul', 'azul', 'amarillo', 'azul', 'azul', 'azul', 'azul', 'amarillo', 'azul', 'amarillo', 'rojo', 'azul', 'azul', 'azul', 'amarillo', 'rojo']
color_frecuente(lista) debió entregar "azul" y 14, pero entregó "verde" y 2 
Vuelve a intentarlo!

"""