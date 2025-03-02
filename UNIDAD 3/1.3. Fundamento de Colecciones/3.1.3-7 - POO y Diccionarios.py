# POO con diccionarios en Python

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Diccionario de productos
productos = {
    "P001": Producto("Laptop", 1200),
    "P002": Producto("Mouse", 25),
    "P003": Producto("Teclado", 45)
}

# Mostrar productos
for clave, producto in productos.items():
    print(f"{clave}: {producto.nombre} - ${producto.precio}")
