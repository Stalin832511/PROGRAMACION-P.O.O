import os
import json
from Producto import Producto


# Definición de la clase Inventario
# Esta clase maneja una colección de productos y los almacena en un archivo.
class Inventario:
    def __init__(self, archivo="inventario.txt"):
        """
        Constructor de la clase Inventario.

        Parámetros:
        archivo (str): Nombre del archivo donde se almacena el inventario.
        """
        self.archivo = archivo
        self.productos = {}
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        """
        Agrega un producto al inventario y lo guarda en el archivo.

        Parámetros:
        producto (Producto): Objeto de la clase Producto.
        """
        if producto.id_producto in self.productos:
            print("Error: Producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_en_archivo()
            print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario y actualiza el archivo.

        Parámetros:
        id_producto (str): Identificador del producto a eliminar.
        """
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("Producto eliminado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Actualiza la cantidad y/o el precio de un producto.

        Parámetros:
        id_producto (str): Identificador del producto.
        cantidad (int, opcional): Nueva cantidad del producto.
        precio (float, opcional): Nuevo precio del producto.
        """
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            self.guardar_en_archivo()
            print("Producto actualizado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        """
        Busca un producto por su nombre y lo muestra en pantalla.

        Parámetros:
        nombre (str): Nombre o parte del nombre del producto.
        """
        encontrado = False
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                print(producto)
                encontrado = True
        if not encontrado:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_en_archivo(self):
        """Guarda los productos en un archivo en formato JSON."""
        try:
            with open(self.archivo, "w") as f:
                json.dump({id_prod: vars(prod) for id_prod, prod in self.productos.items()}, f)
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo.")

    def cargar_desde_archivo(self):
        """Carga los productos desde el archivo al iniciar el programa."""
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, "r") as f:
                    data = json.load(f)
                    self.productos = {id_prod: Producto(**prod) for id_prod, prod in data.items()}
            except (FileNotFoundError, json.JSONDecodeError):
                print("El archivo de inventario estaba vacío o no se pudo leer correctamente.")


# Interfaz de usuario en la consola
def menu():
    inventario = Inventario()
    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad disponible: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == '2':
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco si no desea cambiar): ")
            precio = input("Nuevo precio (dejar en blanco si no desea cambiar): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_inventario()

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida, intente de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    menu()
