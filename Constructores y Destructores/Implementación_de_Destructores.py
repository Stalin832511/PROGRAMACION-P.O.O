# Program: destructor.py

# Definición de la clase Recurso
class Recurso:
    def __init__(self, id):
        """
        Constructor: Inicializa el recurso con el ID proporcionado.
        """
        self.id = id  # Inicializa el ID del recurso
        print(f"Recurso {self.id} inicializado.")

    def __del__(self):
        """
        Destructor: Se llama cuando el objeto es destruido (eliminado).
        En este caso, limpia los recursos y muestra un mensaje.
        """
        print(f"Recurso {self.id} liberado.")

# Instanciación de un objeto Recurso
mi_recurso = Recurso(1)

# Eliminar el objeto para invocar el destructor
del mi_recurso

# Explicación:
# El constructor __init__ inicializa el recurso cuando se crea una nueva instancia de Recurso.
# El destructor __del__ se activa cuando el objeto es eliminado (usando 'del') para liberar el recurso.
