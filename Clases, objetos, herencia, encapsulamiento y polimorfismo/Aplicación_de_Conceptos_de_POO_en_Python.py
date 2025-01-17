# Clase base (padre)
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo público
        self.__edad = edad  # Atributo privado (encapsulación)

    # Método para obtener la edad (encapsulando el acceso al atributo __edad)
    def obtener_edad(self):
        return self.__edad

    # Método general para describir el animal
    def hablar(self):
        print(f"{self.nombre} hace un sonido.")


# Clase derivada (hija)
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.raza = raza  # Nuevo atributo específico para la clase Perro

    # Sobrescritura del método hablar (Polimorfismo)
    def hablar(self):
        print(f"{self.nombre} ladra.")


# Otra clase derivada (hija)
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.color = color  # Nuevo atributo específico para la clase Gato

    # Sobrescritura del método hablar (Polimorfismo)
    def hablar(self):
        print(f"{self.nombre} maúlla.")


# Función para mostrar el comportamiento polimórfico
def hacer_hablar(animal):
    animal.hablar()  # Aquí se usa el polimorfismo, el tipo real del objeto determina qué método se llama


# Instanciación de objetos
perro = Perro("Rex", 5, "Labrador")
gato = Gato("Felix", 3, "Negro")

# Uso de la encapsulación a través de un método
print(f"La edad de {perro.nombre} es {perro.obtener_edad()} años.")
print(f"La edad de {gato.nombre} es {gato.obtener_edad()} años.")

# Uso del polimorfismo
hacer_hablar(perro)  # El método de la clase Perro será llamado
hacer_hablar(gato)  # El método de la clase Gato será llamado
