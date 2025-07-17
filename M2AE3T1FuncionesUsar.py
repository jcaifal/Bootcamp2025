def Formato(edad, pais):
    nueva_edad = int(edad)
    nuevo_pais = pais.lower()
    return (nueva_edad, nuevo_pais)

def Validacion(edad, pais):
    if edad > 18:
        if pais in ['argentina', 'chile', 'colombia']:
            return True
        else:
            return False