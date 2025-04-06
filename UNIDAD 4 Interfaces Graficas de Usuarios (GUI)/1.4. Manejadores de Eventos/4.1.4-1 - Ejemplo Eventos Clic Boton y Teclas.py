
import tkinter as tk
from tkinter import messagebox

# Función para añadir tarea desde botón
def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        tasks[task] = False  # Estado: pendiente
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Campo vacío", "Por favor, ingresa una tarea.")

# Función para marcar tarea como completada desde botón
def mark_task_complete():
    try:
        index = task_listbox.curselection()[0]
        task = task_listbox.get(index)
        if not tasks.get(task, False):
            task_listbox.delete(index)
            completed_task = f"[✔] {task}"
            task_listbox.insert(index, completed_task)
            tasks[completed_task] = True
            del tasks[task]
    except IndexError:
        messagebox.showinfo("Sin selección", "Selecciona una tarea para marcarla como completada.")

# Función para eliminar tarea desde botón
def delete_task():
    try:
        index = task_listbox.curselection()[0]
        task = task_listbox.get(index)
        task_listbox.delete(index)
        if task in tasks:
            del tasks[task]
        else:
            original_task = task.replace("[✔] ", "")
            if original_task in tasks:
                del tasks[original_task]
    except IndexError:
        messagebox.showinfo("Sin selección", "Selecciona una tarea para eliminarla.")

# Crear ventana principal
root = tk.Tk()
root.title("Gestión de Tareas - Botones - Stalin G.")
root.geometry("450x450")

# Entrada de texto
task_entry = tk.Entry(root, width=50, font=("Arial", 12))
task_entry.pack(pady=10)
task_entry.focus()

# Botones
add_button = tk.Button(root, text="Añadir Tarea", width=25, command=add_task)
add_button.pack(pady=5)

complete_button = tk.Button(root, text="Marcar como Completada", width=25, command=mark_task_complete)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Eliminar Tarea", width=25, command=delete_task)
delete_button.pack(pady=5)

# Lista de tareas
task_listbox = tk.Listbox(root, width=60, height=15, font=("Arial", 10))
task_listbox.pack(pady=10)

# Diccionario para guardar tareas
tasks = {}

# Ejecutar ventana
root.mainloop()
