import ply.lex as lex

 

# Lista de nombres de tokens

tokens = (

    'NUMBER',

    'PLUS',

    'MINUS',

    'TIMES',

    'DIVIDE',

    'LPAREN',

    'RPAREN'

)

 

# Definición de tokens usando expresiones regulares

t_PLUS = r'\+'

t_MINUS = r'-'

t_TIMES = r'\*'

t_DIVIDE = r'/'

t_LPAREN = r'\('

t_RPAREN = r'\)'

 

# Definición de un token para números

def t_NUMBER(t):

    r'\d+'

    t.value = int(t.value)

    return t

 

# Ignorar caracteres en blanco (espacios y tabuladores)

t_ignore = ' \t'

 

# Capturar el número de línea

def t_newline(t):

    r'\n+'

    t.lexer.lineno += len(t.value)

 

# Manejo de errores

def t_error(t):

    print(f"Error: Caracter inesperado '{t.value[0]}' en la línea {t.lexer.lineno}")

    t.lexer.skip(1)

 

# Crear el analizador léxico

lexer = lex.lex()

 

# Prueba del analizador léxico

data = "3 + 4 * ( 2 - 1 )"

lexer.input(data)

 

while True:

    tok = lexer.token()

    if not tok:

        break

    print(tok)