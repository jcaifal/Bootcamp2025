#Calculadora

def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def calculadora(a, b, operacion):
    if operacion == 'suma':
        return suma(a, b)
    elif operacion == 'resta':
        return resta(a, b)
    elif operacion == 'multiplicacion':
        return multiplicacion(a, b)
    elif operacion == 'division':
        return division(a, b)
    else:
        return "Operación no válida"    
    
# Ejemplo de uso
if __name__ == "__main__":
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (suma, resta, multiplicacion, division): ").strip().lower()
    
    resultado = calculadora(a, b, operacion)
    print(f"El resultado de la {operacion} es: {resultado}")