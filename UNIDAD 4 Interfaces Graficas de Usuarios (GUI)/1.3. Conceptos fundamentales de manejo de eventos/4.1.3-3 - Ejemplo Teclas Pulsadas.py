import tkinter as tk
from tkinter import messagebox


def add_task(event=None):
    task = task_entry.get().strip()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")


def delete_task(event=None):
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")


def close_app(event):
    root.quit()


root = tk.Tk()
root.title("Ejemplo Avanzado de Manejo de Eventos de Teclado Stalin")
root.geometry("400x300")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)
task_entry.bind("<Return>", add_task)  # Permitir añadir tarea con Enter

task_list = tk.Listbox(root, width=50, height=10)
task_list.pack(pady=10)

task_list.bind("<Delete>", delete_task)  # Permitir eliminar con Supr
root.bind("<Escape>", close_app)  # Cerrar con Esc

root.mainloop()