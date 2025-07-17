def es_mayor(edad):
    if edad > 18:
        return True
    else:
        return False

    




nombre = input("¿Cuál es tu nombre? ")

edad = int(input("¿Cuál es tu edad? "))


validacion = es_mayor(edad)

if validacion == True:
        print(f"Hola {nombre}, eres mayor de edad.")
else:
        print(f"Hola {nombre}, eres menor de edad.")


print("Gracias por participar.")