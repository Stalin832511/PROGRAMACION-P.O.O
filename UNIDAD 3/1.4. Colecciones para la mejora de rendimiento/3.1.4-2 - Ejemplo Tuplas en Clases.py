class Producto:
    def __init__(self, id_producto, nombre, precio):
        self.producto = (id_producto, nombre, precio)

    def mostrar_producto(self):
        print(f"ID: {self.producto[0]}, Nombre: {self.producto[1]}, Precio: ${self.producto[2]}")


# Uso de la clase
producto1 = Producto(101, "Laptop", 850.50)
producto1.mostrar_producto()
