def reemplazo(string):
    mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    palabra = ""
    for letra in string:
        if letra in mayusculas:
            palabra = palabra + "$"
        else: 
            palabra = palabra + letra
    return palabra
    
print(reemplazo("Viva la Vida"))
