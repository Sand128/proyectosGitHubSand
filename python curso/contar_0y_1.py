def ocurrencias(s):
	c1 = s.count("1")
	c0 = s.count("0")
	return(c1-c0)
print(ocurrencias("101010100100101010101"))