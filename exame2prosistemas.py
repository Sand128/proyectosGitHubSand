def preguntasL():
        print("¿Qué deseas conocer del Analizador Léxico?")
        n=int(input("1.-¿Qué es un Analizador Léxico?\n2.-Características del Analizador Léxico\n3.-Ejemplo del Analizador Léxico "))
        if n==1:
            print("""¿Qué es un Analizador Léxico?
                    Es la parte fundamental de un compilador o interprete
                    que se encarga de dividir el codigo fuente en unidades mas pequeñas 
                    llamadas Tokens.""")
        elif n==2:
            print("""Características del Analizador Léxico esta dividido en:
                    >>Identidicadores Nombres de variables, nombres de función,...
                    >>Palabras claves  son while, if, return. . .
                    >>Separadores {, }, ;. . . S
                    >>Operadores  son +, *, /, %, ==, !=, &&. . .
                    >>Literal
                    >>comentarios // o #
                    Los simbolos sirven para la etapa de traduccion.""")
        elif n==3:  
            print("""Ejemplo del Analizador Léxico son los automatas al tener un inicio,final y ariastas.
                  """)
        else:
            print("Regreso al menu principal")
    
def preguntasS():
        print("¿Qué deseas conocer del Analizador Semántico")
        n=int(input("1.-¿Qué es Analizador Semántico\n2.-Características del Analizador Semántico\n3.-Ejemplo del Analizador Semántico "))
        if n==1:
            print("""¿Qué es un Analizador Semántico?
                    Es una disiplica que se encarga de comprender el 
                    significado del lenguaje y su relacion con el mundo.""")
        elif n==2:
            print("""Características del Analizador Semántico es que extrae información 
                    valiosa del texto y lenguaje natural. Permite comprender el 
                    significado detras del lengiaje natural. Encontrar patrones, Tendencias
                    y otros datos valiosos.
                    >>Análisis Semántico Manual
                    >>Análisis Semántico Automatico
                    >>Análisis Semántico Basado en la IA""")
        elif n==3:
            print("""Ejemplo del Analizador Semántico
                  Sea la expresión
    int a,b,c;
    a/(b+c^2)
El árbol sintáctico es:

          /
      ---------
      |       |
      a       +
          ---------
          |       |
          b       ^
              ---------
              |       |
              c       2""")
        else:
            print("Regreso al menu principal")
def preguntasA():
        print("""¿Qué es un árbol de derivacón? 
                Es una estructua de datos no lineal 
                en la que cada elemento(NODO) tiene un unico elemento anterior
                denominado PADRE y puede tener mas de un elemento(HIJOS)""")
def preguntasG():
        print("""¿Qué es una Gramática proposional? 
              Son las normas que indican la forma correcta de su secuencia
              ó tambien conosidas como Conjunto de Reglas.
              """)
    



t=0
while t<=4:
    print("\tMenu")
    print("1.-Analizador Léxico")
    print("2.-Analizador Semántico")
    print("3.-Árboles de Derivación")
    print("4.-Gramática Proposional")
    print("5.-Salir")
    t=int(input("Seleciona un tema de tu interes:"))
    if t==1:
        preguntasL()
    elif t==2:
        preguntasS()
    elif t==3:
        preguntasA()
    elif t==4:
        preguntasG()
print("Gracias!")
