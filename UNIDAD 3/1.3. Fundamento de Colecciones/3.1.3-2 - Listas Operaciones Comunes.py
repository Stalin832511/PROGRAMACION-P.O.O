# Operaciones comunes con listas en Python

# Crear una lista
numeros = [10, 20, 30, 40, 50]

# Agregar elementos
numeros.append(60)  # Agregar al final
numeros.insert(2, 25)  # Insertar en posición específica

# Eliminar elementos
numeros.remove(30)  # Elimina el primer 30 que encuentre
ultimo = numeros.pop()  # Elimina el último elemento

# Ordenar la lista
numeros.sort()  # Ordenar de menor a mayor

# Imprimir resultados
print("Lista final:", numeros)
print("Último eliminado:", ultimo)
