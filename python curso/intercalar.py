def intercalar(string_a, string_b):
    cont=0
    c=""
    long1=len(string_a)
    while cont<long1:
        b=string_a[cont]+string_b
        c=c+b
        cont=cont+1
    return c

a="paz"
b="po"
print(intercalar(a,b))