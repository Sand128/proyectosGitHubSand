opcion=int(input("Que notacion deseas ver:\n1.-Notacion posfija 3 4 5 * +\n2.-La notacion prefija + * 3 4 5\nSelecciona una: "))
#while opcion>0 and opcion<3
if opcion==1:
    from py_prefijas import notacionpolaca as np
elif opcion==2:
    from py_prefijas import notacionpolaca2 as p
else:
    print("Error")
