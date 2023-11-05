import re 

#DEFINICION TOKENS
TOKEN_REGEX = r'(\d+)|(\bif\b|\belse\b|\bwhile\b|\bfor\b)|(\w+)'

#FUNCION PARA ANALIZAR EL CODIGO FUENTE Y GENERAR TOKENS
def lexer(code):
    tokens = re.findall(TOKEN_REGEX,code)
    result = []
    for token in tokens:
        for i in range(len(token)):
            if token[i]:
                result.append(token[i])
    return result

#CODIGO DE EJEMPLO 
source_code = "if x > 5: \n   print ('Mayor que 5')\nelse:\n    print('Menor o igusl a 5')"

#LLAMADA AL ANALIZADOR LEXICO
tokens = lexer(source_code)

#IMPRIMIR LOS TOKENS
for token in tokens:
    print(token)