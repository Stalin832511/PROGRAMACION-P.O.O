import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "¡Botón presionado!")

def cambiar_texto():
    etiqueta.config(text=entrada.get())

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Componentes Avanzados")
ventana.geometry("300x250")

# Crear componentes
etiqueta = tk.Label(ventana, text="Etiqueta inicial")
entrada = tk.Entry(ventana)
boton_mensaje = tk.Button(ventana, text="Mostrar Mensaje", command=mostrar_mensaje)
boton_cambiar = tk.Button(ventana, text="Cambiar Texto", command=cambiar_texto)

# Ubicar componentes
etiqueta.pack(pady=5)
entrada.pack(pady=5)
boton_mensaje.pack(pady=5)
boton_cambiar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()



