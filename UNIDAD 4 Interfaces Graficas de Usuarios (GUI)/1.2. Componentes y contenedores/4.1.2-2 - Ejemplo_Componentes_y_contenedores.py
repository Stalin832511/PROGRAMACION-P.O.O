import tkinter as tk
from tkinter import Frame

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Componentes y Contenedores")
ventana.geometry("300x200")

# Crear un contenedor (frame)
frame = Frame(ventana, bd=2, relief=tk.SUNKEN)
frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Crear componentes dentro del contenedor
etiqueta = tk.Label(frame, text="Dentro del Frame")
entrada = tk.Entry(frame)
boton = tk.Button(frame, text="Aceptar")

# Ubicar componentes dentro del frame
etiqueta.pack(pady=5)
entrada.pack(pady=5)
boton.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()

