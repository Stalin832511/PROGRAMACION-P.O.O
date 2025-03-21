import tkinter as tk
from tkinter import messagebox

# Función para mostrar un mensaje
def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "Hola, esto es un mensaje de prueba.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de GUI con Tkinter")
ventana.geometry('400x400')  # Establecer el tamaño de la ventana

# Crear un botón
boton = tk.Button(ventana, text="Mostrar mensaje", command=mostrar_mensaje)
boton.pack(pady=20)  # Empaquetar el botón con un poco de espacio en y

# Ejecutar el bucle de eventos
ventana.mainloop()
