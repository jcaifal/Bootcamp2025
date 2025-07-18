nombre = input("¿Cuál es tu nombre? ")

edad = int(input("¿Cuál es tu edad? "))

pais = input("¿Cuál es tu país? ")

pais_valido = ["argentina", "chile", "colombia"]

if pais.lower() in pais_valido:
    if edad > 18:
        print(f"Hola {nombre}, debido a que tu país es: {pais}, y tienes: {edad}, tienes acceso al sistema.")
    else:
        print(f"Hola {nombre}, debido a que tu país es: {pais}, y tienes: {edad}, no tienes acceso al sistema.")

else:
    print(f"Hola {nombre}, debido a que tu país es: {pais}, no tienes acceso al sistema.")
print("Gracias por participar.")

        
