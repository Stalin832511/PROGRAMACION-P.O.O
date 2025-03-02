# Operaciones comunes con tuplas en Python

# Crear una tupla
tupla = (100, 200, 300, 400, 500)

# Acceder a elementos
primer_elemento = tupla[0]
ultimo_elemento = tupla[-1]

# Desempaquetado de tuplas
a, b, c, d, e = tupla

# Conteo de elementos en la tupla
conteo = tupla.count(300)

# Imprimir resultados
print("Primer elemento:", primer_elemento)
print("Último elemento:", ultimo_elemento)
print("Valores desempaquetados:", a, b, c, d, e)
print("Cantidad de veces que aparece 300:", conteo)
