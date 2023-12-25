def evaluar_notacion_polaca_prefija(expresion):
    pila = []
    elementos = expresion.split()
    for elemento in reversed (elementos):
        if elemento.isdigit() or (elemento[0] == '-'and elemento[1:].isdigit()):
            pila.append(int(elemento))
        else:
            operando1 = pila.pop()
            operando2 = pila.pop()

            if elemento == '+':
                resultado = operando1 + operando2
            elif elemento == '-':
                resultado = operando1 - operando2
            elif elemento == '*':
                resultado = operando1 * operando2
            elif elemento == '/':
                resultado = operando1 / operando2
            else:
                raise ValueError(f"Operador no reconocido: {elemento}")
            pila.append(resultado)
    return pila[0]
expresion_polaca_prefija = "+ * 3 4 5"
#expresion_polaca_prefija=input("Ingresa la cadena, primero operadores despues numeros, recuerda de seprar con espacios: ")
resultado = evaluar_notacion_polaca_prefija(expresion_polaca_prefija)
print(f"El resultado de la expresion en notacion polaca prefija es: {resultado}")