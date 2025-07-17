mi_diccionario = {'emp1':{"nombre": "Juan","edad": 30},
                  'emp2':{"nombre": "Ana","edad": 25},
                  'emp3':{"nombre": "Luis","edad": 35},
                  'emp4':{"nombre": "Marta","edad": 28},
                  'emp5':{"nombre": "Pedro","edad": 20}}

lista_empleados = []
for clave, valor in mi_diccionario.items():
    if valor['edad'] <   30:           
            lista_empleados.append(valor['nombre'])


print("Empleados menores de 30 años:", lista_empleados)


