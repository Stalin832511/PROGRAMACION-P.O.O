# Operaciones comunes con diccionarios en Python

# Crear un diccionario
persona = {"nombre": "Ana", "edad": 30, "ciudad": "Guayaquil"}

# Agregar un nuevo par clave-valor
persona["profesion"] = "Ingeniera"

# Modificar un valor
persona["edad"] = 31

# Eliminar una clave
del persona["ciudad"]

# Obtener claves y valores
claves = list(persona.keys())
valores = list(persona.values())

# Imprimir resultados
print("Diccionario final:", persona)
print("Claves:", claves)
print("Valores:", valores)
