class AnalizadorFinanciero:
    # Calcula el total de ingresos en una lista de transacciones
    def calcular_total_ingresos(self, transacciones):
        total = 0
        for ingreso in transacciones:
            total += ingreso
        return total

    # Filtra y retorna solo los ingresos mayores a un umbral dado
    def filtrar_ingresos_altos(self, transacciones, umbral):
        ingresos_altos = []
        for ingreso in transacciones:
            if ingreso > umbral:
                ingresos_altos.append(ingreso)
        return ingresos_altos
       

    # Agrupa ingresos en un diccionario por categorías
    def agrupar_por_categoria(self, transacciones, categorias):
        agrupado = {}
        for categoria, ingreso in zip(categorias, transacciones):
            if categoria in agrupado:
                agrupado[categoria].append(ingreso)
            else:
                agrupado[categoria] = [ingreso]
        return agrupado
          

  

# Main para utilizar la clase AnalizadorFinanciero
if __name__ == "__main__":
    transacciones = [100, 200, 300, 400, 500]
    categorias = ["comida", "transporte", "comida", "entretenimiento", "transporte"]

    analizador = AnalizadorFinanciero()

    print(f"Total de ingresos: {analizador.calcular_total_ingresos(transacciones)}")
    print(f"Ingresos altos: {analizador.filtrar_ingresos_altos(transacciones, 250)}")
    print(f"Ingresos agrupados por categoría: {analizador.agrupar_por_categoria(transacciones, categorias)}")
   




#1● Análisis de las ventajas y limitaciones de las estructuras de datos utilizadas en el código.
### R: Las listas usadas en transacciones y categorias permiten recorrer facilmente los datos.
### , mientras los diccionarios como agrupar las trasacciones por categorias permite una búsqueda rápida y eficiente de los datos  


#2● Código de las funciones optimizadas, incorporando comprensión de listas y estructuras avanzadas como conjuntos.
#R: Es posible usar sum() en vez de los bucles ej:
#def calcular_total_ingresos(self, transacciones):
#        return sum(transacciones)

#3● Descripción detallada de las pruebas implementadas para cada función y los resultados obtenidos.
# R: Se implementaron pruebas para calcular el total de ingresos, filtrar ingresos altos y agrupar por categoría. 
# Los resultados fueron correctos y se verificaron con datos de ejemplo.

#4● Ejemplos de casos de prueba, con los datos de entrada y los resultados esperados.
#SALIDA
#Total de ingresos: 1500
#Ingresos altos: [300, 400, 500]
#Ingresos agrupados por categoría: {'comida': [100, 300], 'transporte': [200, 500], 'entretenimiento': [400]}


#5● Reflexión sobre la experiencia de aplicar optimización de estructuras de datos y sentencias iterativas en este caso.
#R: Mejora la eficiencia del código, hace que mas personas puedan entenderlo y usarlo.