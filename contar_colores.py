def color_frecuente (lista):
    a=(lista.count(("azul")))
    b=(lista.count(("verde")))
    c=(lista.count(("rojo")))
    d=(lista.count(("amarillo")))
    for colores in sorted(set(lista)):
        num=lista.count((colores))
        if a>=num and num>c and num>d and num>b:
            mensaje="azul",a
        elif b>=num and num>c and num>d and num>a:
            mensaje="verde",b
        elif c>=num and num>a and num>d and num>b:
            mensaje="rojo",c
        elif d>=num and num>c and num>a and num>b:
            mensaje="amarillo",d
    return mensaje

#lista =['amarillo', 'amarillo', 'amarillo', 'amarillo', 'amarillo', 'rojo', 'azul', 'verde', 'verde', 'azul', 'azul', 'amarillo', 'azul', 'azul', 'azul', 'amarillo', 'azul', 'azul', 'azul', 'azul', 'amarillo', 'azul', 'amarillo', 'rojo', 'azul', 'azul', 'azul', 'amarillo', 'rojo']
lista =['amarillo', 'amarillo', 'amarillo', 'amarillo','amarillo', 'amarillo', 'amarillo', 'amarillo','amarillo', 'amarillo', 'amarillo', 'amarillo', 'amarillo', 'rojo', 'azul', 'verde', 'verde', 'azul', 'azul', 'amarillo', 'azul', 'azul', 'azul', 'amarillo', 'azul', 'azul', 'azul', 'azul', 'amarillo', 'azul', 'amarillo', 'rojo', 'azul', 'azul', 'azul', 'amarillo', 'rojo']
#lista = ['verde', 'amarillo', 'verde', 'azul', 'amarillo', 'azul', 'amarillo', 'rojo', 'amarillo', 'verde', 'verde', 'amarillo', 'rojo', 'rojo', 'rojo', 'verde', 'azul', 'azul', 'amarillo', 'amarillo', 'amarillo', 'amarillo', 'rojo', 'verde', 'rojo', 'rojo', 'verde', 'azul', 'verde', 'rojo', 'rojo', 'azul', 'azul', 'verde', 'amarillo', 'rojo', 'azul', 'verde', 'rojo', 'azul', 'rojo', 'amarillo', 'amarillo', 'rojo', 'amarillo']
print(color_frecuente(lista))


"""
Con lista = ['amarillo', 'amarillo', 'amarillo', 'amarillo', 'amarillo', 'rojo', 'azul', 'verde', 'verde', 'azul', 'azul', 'amarillo', 'azul', 'azul', 'azul', 'amarillo', 'azul', 'azul', 'azul', 'azul', 'amarillo', 'azul', 'amarillo', 'rojo', 'azul', 'azul', 'azul', 'amarillo', 'rojo']
color_frecuente(lista) debió entregar "azul" y 14, pero entregó "verde" y 2 
Vuelve a intentarlo!

"""