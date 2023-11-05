#definicíon de la tabla de símbolos como un diccionario
symbol_table = {}

#función para agregar un identificador y su valor a la tabla de símbolos
def add_to_symbol_table(identifier,value):
    symbol_table[identifier] = value

#función paran buscar un identificador en la tabla de símbolos
def lookup_in_symbol_table(identifier):
    return symbol_table.get(identifier, None)

#código de ejemplo para agregar y buscar identificadores en la tabla de símbolos
add_to_symbol_table(1,"Niño")
add_to_symbol_table(2,"Adolecente")
add_to_symbol_table(3,"Adulto")
add_to_symbol_table(4,"Chavorruco")
add_to_symbol_table(5,"Ruco")
add_to_symbol_table(6,"Ya casi te vas")


def iden(edad):
    #buscar un identificador en la tabla de símbolos
    if edad<=13:
        identifier_to_find=1
    elif edad>13 and edad<=19:
        identifier_to_find=2
    elif edad>19 and edad<=35:
        identifier_to_find=3
    elif edad>15 and edad<=45:
        identifier_to_find=4
    elif edad>45 and edad<=60:
        identifier_to_find=5
    elif edad>60 and edad<=70:
        identifier_to_find=6    
    #identifier_to_find=op
    value = lookup_in_symbol_table(identifier_to_find)
    if value is not None:
        print(f"Es un  {value} porque tiene", edad)
    else:
        print(f"{identifier_to_find} no se encuentra en la tabla de símbolos")

#menu
while True:
    edad=int(input("0 para salir\nIngresa una edad y te tigo tu estado: "))
    if edad==0:
        print("Gracias")
        break
    else:
        iden(edad)