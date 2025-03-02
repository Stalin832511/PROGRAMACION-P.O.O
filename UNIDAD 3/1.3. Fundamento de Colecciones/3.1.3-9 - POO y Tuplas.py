# POO con tuplas en Python

class Ciudad:
    def __init__(self, nombre, poblacion):
        self.nombre = nombre
        self.poblacion = poblacion

# Crear una tupla de ciudades
ciudades = (
    Ciudad("Quito", 1800000),
    Ciudad("Guayaquil", 2700000),
    Ciudad("Cuenca", 700000)
)

# Mostrar ciudades
for ciudad in ciudades:
    print(f"{ciudad.nombre} - {ciudad.poblacion} habitantes")
