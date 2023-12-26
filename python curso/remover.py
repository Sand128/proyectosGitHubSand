def remover_enesimo(s, n):
    l=len(s)
    cadena=s
    i=0
    while i<l:
        if i==n:
            print(cadena[i])
            cadena="".join(cadena)
            break
        i=i+1
    return cadena
a="hola juan jose alias pato"
b=16
print(remover_enesimo(a,b))