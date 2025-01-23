# Program: constructor.py

# Definición de la clase Libro
class Libro:
    def __init__(self, titulo, autor):
        """
        Constructor: Se llama automáticamente cuando se crea una nueva instancia de la clase.

        Atributos:
        - titulo: El título del libro.
        - autor: El autor del libro.
        """
        self.titulo = titulo  # Inicializa el atributo 'titulo' con el valor proporcionado
        self.autor = autor  # Inicializa el atributo 'autor' con el valor proporcionado

        print(f"Libro creado: {self.titulo} por {self.autor}")


# Instanciación de un objeto Libro
mi_libro = Libro("1984", "George Orwell")

# Explicación:
# El constructor __init__ se activa automáticamente al crear un objeto (en este caso, 'mi_libro').
# El código dentro del constructor se ejecuta para inicializar el objeto con los valores proporcionados.
