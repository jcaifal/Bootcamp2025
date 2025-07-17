list_calificaciones = [60,50,60, 78, 98,77, 99, 55,100, 90, 80, 70, 85, 95, 65, 75]


largo_lista = len(list_calificaciones)

suma = 0

lista_aprobados = []
lista_reprobados = []

for i in range(largo_lista):
    suma = suma + list_calificaciones[i]
    if list_calificaciones[i] >= 60:
        lista_aprobados.append(list_calificaciones[i])
    else:   
        lista_reprobados.append(list_calificaciones[i])
promedio = suma / largo_lista


print("El promedio total de las calificaciones es: ", promedio)

print("La lista de aprobados es: ", lista_aprobados)
print("El número de aprobados es: ", len(lista_aprobados))

print("La lista de reprobados es: ", lista_reprobados)
print("El número de reprobados es: ", len(lista_reprobados))

