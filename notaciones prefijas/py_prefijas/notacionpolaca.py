def evaluar_notacion_polaca(expresion):
    pila =[]

    for elementos in expresion.split():
        if elementos.isdigit() or (elementos[0] == '-' and elementos[1:].isdigit()):
            #si es un numero (positivo o negativo), colocarlo en pila
            pila.append(int(elementos))
        else:
            #Es un operador, aplica la operacion a los elementos superiores de la pila 
            operando2 = pila.pop()
            operando1 = pila.pop()

            if elementos == '+':
                resultado = operando1 + operando2
            elif elementos == '-':
                resultado = operando1 - operando2
            elif elementos == '*':
                resultado = operando1 * operando2
            elif elementos == '/':
                resultado = operando1 / operando2
            else:
                raise ValueError(f"Operador no reconocido:{elementos}")
            
            #Colocar resultado de la operacion en la pila 
            pila.append(resultado)

    #El resultado final debe estar en la cima de la pila 
    return pila[0]
#Ejemplo de uso 
expresion_polaca ="3 4 5 * +"
#expresion_polaca=input("Ingresa la cadena, primero numeros despues operadores, recuerda de seprar con espacios: ")
resultado = evaluar_notacion_polaca(expresion_polaca)
print(f"El resultado de la expresion en notacion polaca es: {resultado}")