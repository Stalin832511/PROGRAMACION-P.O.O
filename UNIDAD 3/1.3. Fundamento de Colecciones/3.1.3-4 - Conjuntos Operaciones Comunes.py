# Operaciones comunes con conjuntos en Python

# Crear conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

# Operaciones de conjuntos
union = conjunto1 | conjunto2  # Unión
interseccion = conjunto1 & conjunto2  # Intersección
diferencia = conjunto1 - conjunto2  # Diferencia

# Agregar y eliminar elementos
conjunto1.add(10)
conjunto1.remove(2)

# Imprimir resultados
print("Unión:", union)
print("Intersección:", interseccion)
print("Diferencia:", diferencia)
print("Conjunto 1 final:", conjunto1)
