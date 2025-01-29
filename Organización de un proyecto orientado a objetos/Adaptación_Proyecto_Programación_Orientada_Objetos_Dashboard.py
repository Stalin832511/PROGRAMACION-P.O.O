import os
import subprocess

def mostrar_codigo(ruta_script):
    """
    Lee y muestra el código del archivo Python especificado.

    Parámetros:
        ruta_script (str): Ruta al archivo de script que se desea mostrar.

    Retorna:
        str: El código fuente del archivo si se lee correctamente,
             o None si hay un error.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)  # Convertir la ruta al formato absoluto
    try:
        with open(ruta_script_absoluta, 'r') as archivo:  # Abrir el archivo en modo de lectura
            codigo = archivo.read()  # Leer el contenido completo del archivo
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)  # Imprimir el código fuente
            return codigo  # Retornar el código leído
    except FileNotFoundError:
        print("El archivo no se encontró.")  # Manejo de error si el archivo no existe
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    """
    Ejecuta el archivo Python especificado dependiendo del sistema operativo.

    Parámetros:
        ruta_script (str): Ruta al archivo de script que se desea ejecutar.
    """
    try:
        if os.name == 'nt':  # Si el sistema operativo es Windows
            if ruta_script.endswith('.py'):
                subprocess.Popen(['cmd', '/k', 'python', ruta_script])  # Ejecutar Python en Windows
            elif ruta_script.endswith('.js'):
                subprocess.Popen(['cmd', '/k', 'node', ruta_script])  # Agregado soporte para JavaScript
            else:
                print("Lenguaje no soportado")  # Verifica si el lenguaje es soportado
        else:  # Si el sistema es basado en Unix (Linux/Mac)
            if ruta_script.endswith('.py'):
                subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])  # Ejecutar Python en Unix
            elif ruta_script.endswith('.js'):
                subprocess.Popen(['xterm', '-hold', '-e', 'node', ruta_script])  # Agregado soporte para JavaScript
            else:
                print("Lenguaje no soportado")  # Verifica si el lenguaje es soportado
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")  # Manejo de excepciones

def mostrar_menu():
    """
    Muestra el menú principal para seleccionar unidades y permitir la navegación.
    """
    ruta_base = os.path.dirname(__file__)  # Ruta base donde se encuentra el dashboard.py

    # Modificación para incluir más unidades
    unidades = {
        '1': 'Unidad 1',
        '2': 'Unidad 2',
        '3': 'Unidad 3',  # Se añade una unidad más
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú principal
        for key in unidades:
            print(f"{key} - {unidades[key]}")
        print("0 - Salir")

        eleccion_unidad = input("Elige una unidad o '0' para salir: ")
        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_sub_menu(ruta_unidad):
    """
    Muestra el submenú de carpetas dentro de la unidad seleccionada y permite navegar entre ellas.
    """
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]  # Busca subcarpetas en la ruta de la unidad

    while True:
        print("\nSubmenú - Selecciona una subcarpeta")
        # Imprime las subcarpetas disponibles
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == '0':
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_scripts(ruta_sub_carpeta):
    """
    Muestra los scripts disponibles en la subcarpeta seleccionada y permite verlos o ejecutarlos.
    """
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]  # Busca archivos .py

    while True:
        print("\nScripts - Selecciona un script para ver y ejecutar")
        # Muestra los scripts disponibles para su visualización y ejecución
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        eleccion_script = input("Elige un script, '0' para regresar o '9' para ir al menú principal: ")
        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return  # Regresar al menú principal
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)  # Mostrar el contenido del script
                    if codigo:
                        # Modificación para permitir ejecutar el código en diferentes lenguajes
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)  # Ejecutar el código
                        elif ejecutar == '0':
                            print("No se ejecutó el script.")
                        else:
                            print("Opción no válida. Regresando al menú de scripts.")
                        input("\nPresiona Enter para volver al menú de scripts.")
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()  # Iniciar la función del menú principal
