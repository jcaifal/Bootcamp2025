class Libro:
    def __init__(self, titulo, autor, stock):
        self.titulo = titulo
        self.autor = autor
        self.stock = stock

class LibroNoDisponibleError(Exception):
    """Excepción personalizada para libros no disponibles."""
    pass

class Biblioteca:
    def __init__(self):
        self.catalogo = {}

    def agregar_libro(self, libro):
        self.catalogo[libro.titulo] = libro

    def prestar_libro(self, titulo):
        if titulo in self.catalogo:
            libro = self.catalogo[titulo]
            if libro.stock > 0:
                libro.stock -= 1
                print(f"Se ha prestado el libro: '{titulo}'. Stock restante: {libro.stock}")
            else:
                raise LibroNoDisponibleError(f"No hay ejemplares disponibles de '{titulo}'.")
        else:
            print(f"El libro '{titulo}' no está en el catálogo.")

# Ejemplo de uso
if __name__ == "__main__":
    biblioteca = Biblioteca()
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 2)
    biblioteca.agregar_libro(libro1)

    try:
        biblioteca.prestar_libro("Cien años de soledad")
        biblioteca.prestar_libro("Cien años de soledad")
        biblioteca.prestar_libro("Cien años de soledad")  # Esto lanzará la excepción
    except LibroNoDisponibleError as e:
        print(f"Error: {e}")
