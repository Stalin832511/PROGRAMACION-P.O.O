class Biblioteca:
    def __init__(self):
        self.libros = {}

    def agregar_libro(self, id_libro, titulo, autor):
        self.libros[id_libro] = {"titulo": titulo, "autor": autor}

    def buscar_libro(self, id_libro):
        return self.libros.get(id_libro, "Libro no encontrado")

    def mostrar_libros(self):
        for id_libro, datos in self.libros.items():
            print(f"ID: {id_libro}, Título: {datos['titulo']}, Autor: {datos['autor']}")


# Uso de la clase
biblioteca = Biblioteca()
biblioteca.agregar_libro(1, "Cien años de soledad", "Gabriel García Márquez")
biblioteca.agregar_libro(2, "1984", "George Orwell")

print(biblioteca.buscar_libro(1))
print(biblioteca.buscar_libro(3))
biblioteca.mostrar_libros()
