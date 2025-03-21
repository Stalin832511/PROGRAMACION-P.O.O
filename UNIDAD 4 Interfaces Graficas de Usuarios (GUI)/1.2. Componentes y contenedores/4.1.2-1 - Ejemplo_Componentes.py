import tkinter as tk

def mostrar_mensaje():
    etiqueta.config(text="¡Botón presionado!")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Componentes Básicos")
ventana.geometry("300x200")

# Crear componentes
etiqueta = tk.Label(ventana, text="Hola, Tkinter!")
entrada = tk.Entry(ventana)
boton = tk.Button(ventana, text="Presionar", command=mostrar_mensaje)

# Ubicar componentes
etiqueta.pack(pady=10)
entrada.pack(pady=5)
boton.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()



