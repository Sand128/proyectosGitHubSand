#En un grupo donde las calificaciones se almacenan en un arreglo
#debe eliminar la calificación más baja e imprimir el arreglo sin ella
# porteriormente calcular el promedio de las calificaciones:
calificaciones = [8,9,10,5,9,6,9]
calificaciones.sort() #acomoda la cadena de menor a mayor
calificaciones.pop(0) #eliminar la posicion 0=menor
print(calificaciones)
promedio = (calificaciones[0]+calificaciones[1]+calificaciones[2]+
            calificaciones[3]+calificaciones[4]+calificaciones[5])/6
print("El promedio grupal es: " +str(promedio))
