def mezclador(string_a, string_b):
    if len(str1) < 2 or len(str2) < 2:  # Si los string no son lo suficientemente largos
        return "Los string deben de ser de largo > 2"
    str_resultado = str1[0:2] + str2[-2:]
    return str_resultado




def ocurrencias(string):
	c1 = string.count("1")
	c0 = string.count("0")
	return(c1-c0)



def remover_enesimo(s, n):
    s = list(s)
    del s[n]
    s = "".join(s)
    return s