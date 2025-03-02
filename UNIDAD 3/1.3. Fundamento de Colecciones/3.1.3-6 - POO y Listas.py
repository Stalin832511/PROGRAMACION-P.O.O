# POO con listas en Python

class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre}, {self.edad} años"

# Lista de estudiantes
estudiantes = [
    Estudiante("Carlos", 20),
    Estudiante("María", 22),
    Estudiante("José", 19)
]

# Mostrar estudiantes
for estudiante in estudiantes:
    print(estudiante)
