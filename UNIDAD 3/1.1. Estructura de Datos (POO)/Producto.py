# Definición de la clase Producto
# Esta clase modela un producto con su ID, nombre, cantidad y precio.
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.

        Parámetros:
        id_producto (str): Identificador único del producto.
        nombre (str): Nombre del producto.
        cantidad (int): Cantidad disponible en inventario.
        precio (float): Precio del producto.
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        """
        Representación en cadena del producto.

        Retorna:
        str: Información del producto en formato legible.
        """
        return f"{self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"
