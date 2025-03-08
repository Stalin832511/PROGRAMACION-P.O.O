class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, id_producto, nombre, precio):
        self.productos[id_producto] = {"nombre": nombre, "precio": precio}

    def buscar_producto(self, id_producto):
        return self.productos.get(id_producto, "Producto no encontrado")


# Uso de la clase
inventario = Inventario()
inventario.agregar_producto(1, "Monitor", 200)
inventario.agregar_producto(2, "Teclado", 50)

print(inventario.buscar_producto(1))
print(inventario.buscar_producto(3))
