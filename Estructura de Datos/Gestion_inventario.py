from Producto import Producto, Inventario  #


# Función para mostrar el menú en consola
def mostrar_menu():
    print("\nSistema de Gestión de Inventarios")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar todos los productos")
    print("6. Salir")


# Función principal para gestionar el inventario
def menu():
    inventario = Inventario()  # Crear una instancia de Inventario

    while True:
        mostrar_menu()  # Mostrar el menú de opciones
        opcion = input("Selecciona una opción (1-6): ")

        if opcion == '1':
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(nuevo_producto)

        elif opcion == '2':
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje en blanco para no modificar): ")
            precio = input("Ingrese el nuevo precio (deje en blanco para no modificar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_inventario()

        elif opcion == '6':
            print("Saliendo del sistema.")
            break

        else:
            print("Opción inválida, intenta nuevamente.")


# Llamada a la función del menú
if __name__ == "__main__":
    menu()
