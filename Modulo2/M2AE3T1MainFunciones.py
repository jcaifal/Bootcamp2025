
import M2AE3T1FuncionesUsar

def main():
     edad = input("Introduce tu edad: ")
     pais = input("Introduce tu país: ")
   
     nueva_edad, nuevo_pais = funciones.Formato(edad, pais)
     es_valido = funciones.Validacion(nueva_edad, nuevo_pais)
    
    if es_valido:
      print(f"Edad: {nueva_edad}, País: {nuevo_pais} - Validado")
    else:
      print(f"Edad: {nueva_edad}, País: {nuevo_pais} - No validado")

if __name__ == "__main__":
