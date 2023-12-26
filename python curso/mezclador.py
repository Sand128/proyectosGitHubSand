def mezclador(str1, str2):
    if len(str1) < 2 or len(str2) < 2:  # Si los string no son lo suficientemente largos
        return "Los string deben de ser de largo > 2"
    str_resultado = str1[0:2] + str2[-2:]
    return str_resultado
  
print(mezclador("familia","abrigarse"))