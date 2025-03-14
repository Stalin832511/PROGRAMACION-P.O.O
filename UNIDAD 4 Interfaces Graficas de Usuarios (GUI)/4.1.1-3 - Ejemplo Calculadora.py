import tkinter as tk
from functools import partial  # Importamos partial para evitar problemas en los botones

# Función para agregar un carácter al campo de entrada
def agregar_caracter(caracter):
    texto_actual = entrada.get()
    # Evita que haya un cero innecesario al inicio
    if texto_actual == "0" and caracter.isdigit():
        entrada.delete(0, tk.END)
    entrada.insert(tk.END, caracter)

# Función para realizar el cálculo de la expresión
def calcular(*args):
    try:
        expresion = entrada.get()
        resultado = eval(expresion)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))  # Aseguramos que el resultado se muestra correctamente
        log.config(text=f"Operación: {expresion}, Resultado: {resultado}")
    except ZeroDivisionError:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Math Error")
        log.config(text="Error: División por 0")
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")
        log.config(text=f"Error: {str(e)}")

# Función para limpiar el campo de entrada
def limpiar():
    entrada.delete(0, tk.END)
    log.config(text="")

# Función para salir de la aplicación
def salir():
    ventana.quit()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Stalin G")
ventana.geometry("350x350")

# Crear un menú
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)
menu_archivo = tk.Menu(barra_menu)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Limpiar", command=limpiar)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)

# Crear un campo de entrada
entrada = tk.Entry(ventana, font=("Arial", 18), justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entrada.bind("<Return>", calcular)
entrada.bind("<Escape>", lambda event: limpiar())

# Crear un label para visualizar las operaciones en formato de log
log = tk.Label(ventana, text="", font=("Arial", 12))
log.grid(row=1, column=0, columnspan=4, padx=10, pady=5)

# Crear los botones de los números
numeros = "789456123"
for i, num in enumerate(numeros):
    tk.Button(ventana, text=num, font=("Arial", 14), command=partial(agregar_caracter, num)).grid(row=(i//3)+2, column=(i%3), padx=5, pady=5)

# Colocamos el botón del "0" correctamente
tk.Button(ventana, text="0", font=("Arial", 14), command=lambda: agregar_caracter("0")).grid(row=5, column=0, padx=5, pady=5)

# Botón para el punto decimal
tk.Button(ventana, text=".", font=("Arial", 14), command=lambda: agregar_caracter(".")).grid(row=5, column=1, padx=5, pady=5)

# Botón para borrar toda la entrada (C) en la posición correcta
tk.Button(ventana, text="C", font=("Arial", 14), command=limpiar).grid(row=5, column=2, padx=5, pady=5)

# Crear los botones de las operaciones
operadores = ["+", "-", "*", "/"]
for i, operador in enumerate(operadores):
    tk.Button(ventana, text=operador, font=("Arial", 14), command=partial(agregar_caracter, operador)).grid(row=i+2, column=3, padx=5, pady=5)

# Botón para el cálculo ("=") en la fila final, ocupando todo el ancho
tk.Button(ventana, text="=", font=("Arial", 14), command=calcular).grid(row=6, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

# Ejecutar el bucle de eventos
ventana.mainloop()

