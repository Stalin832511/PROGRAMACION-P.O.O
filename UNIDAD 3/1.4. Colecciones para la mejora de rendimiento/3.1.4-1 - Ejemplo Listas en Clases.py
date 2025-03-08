class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre}, {self.edad} años"


class Curso:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        for estudiante in self.estudiantes:
            print(estudiante)


# Uso de la clase
curso = Curso()
curso.agregar_estudiante(Estudiante("Juan", 20))
curso.agregar_estudiante(Estudiante("Ana", 22))
curso.mostrar_estudiantes()
