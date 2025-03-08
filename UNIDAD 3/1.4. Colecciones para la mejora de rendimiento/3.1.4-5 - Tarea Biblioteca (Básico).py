class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, titulo):
        self.libros.append(titulo)

    def mostrar_libros(self):
        for libro in self.libros:
            print(libro)


# Uso de la clase
biblioteca = Biblioteca()
biblioteca.agregar_libro("Cien años de soledad")
biblioteca.agregar_libro("1984")
biblioteca.mostrar_libros()
