import tkinter as tk

# Función para agregar un carácter al campo de entrada
def agregar_caracter(caracter):
    entrada.insert(tk.END, caracter)

# Función para realizar el cálculo de la expresión
def calcular(*args):
    try:
        expresion = entrada.get()
        resultado = eval(expresion)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
        log.config(text=f"Operación: {expresion}, Resultado: {resultado}")
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")
        log.config(text="Error")

# Función para limpiar el campo de entrada
def limpiar():
    entrada.delete(0, tk.END)
    log.config(text="")

# Función para salir de la aplicación
def salir():
    ventana.quit()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x300")

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
numeros = "7894561230"
for i, num in enumerate(numeros):
    tk.Button(ventana, text=num, font=("Arial", 14), command=lambda num=num: agregar_caracter(num)).grid(row=(i//3)+2, column=(i%3), padx=5, pady=5)

# Botón para el punto decimal
tk.Button(ventana, text=".", font=("Arial", 14), command=lambda: agregar_caracter(".")).grid(row=5, column=1, padx=5, pady=5)

# Botón para el cálculo
tk.Button(ventana, text="=", font=("Arial", 14), command=calcular).grid(row=5, column=0, padx=5, pady=5)

# Botón para borrar toda la entrada
tk.Button(ventana, text="C", font=("Arial", 14), command=limpiar).grid(row=5, column=2, padx=5, pady=5)

# Crear los botones de las operaciones
operadores = ["+", "-", "*", "/"]
for i, operador in enumerate(operadores):
    tk.Button(ventana, text=operador, font=("Arial", 14), command=lambda op=operador: agregar_caracter(op)).grid(row=i+2, column=3, padx=5, pady=5)

# Ejecutar el bucle de eventos
ventana.mainloop()
