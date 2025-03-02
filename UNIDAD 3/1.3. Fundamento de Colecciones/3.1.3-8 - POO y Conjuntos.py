# POO con conjuntos en Python

class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre

# Crear conjuntos de alumnos
grupoA = {Alumno("Juan"), Alumno("María"), Alumno("Pedro")}
grupoB = {Alumno("Pedro"), Alumno("Lucía"), Alumno("Ana")}

# Intersección (alumnos en ambos grupos)
comunes = grupoA & grupoB

# Mostrar resultados
print("Alumnos en ambos grupos:")
for alumno in comunes:
    print(alumno.nombre)
