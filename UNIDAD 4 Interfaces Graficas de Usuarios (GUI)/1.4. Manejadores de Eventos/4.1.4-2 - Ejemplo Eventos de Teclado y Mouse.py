
import tkinter as tk
from tkinter import messagebox

# Funciones para atajos de teclado
def add_task(event=None):
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        tasks[task] = False
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Campo vacío", "Por favor, ingresa una tarea.")

def mark_task_complete(event=None):
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

def delete_task(event=None):
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

def exit_app(event=None):
    root.quit()

# Crear ventana principal
root = tk.Tk()
root.title("Gestión de Tareas - Atajos de Teclado - Stalin G.")
root.geometry("450x450")

# Entrada de texto
task_entry = tk.Entry(root, width=50, font=("Arial", 12))
task_entry.pack(pady=10)
task_entry.focus()

# Lista de tareas
task_listbox = tk.Listbox(root, width=60, height=15, font=("Arial", 10))
task_listbox.pack(pady=10)

# Diccionario para guardar tareas
tasks = {}

# Atajos de teclado
root.bind('<Return>', add_task)          # Añadir con Enter
root.bind('<c>', mark_task_complete)     # Marcar como completada con 'c'
root.bind('<C>', mark_task_complete)
root.bind('<d>', delete_task)            # Eliminar con 'd'
root.bind('<D>', delete_task)
root.bind('<Delete>', delete_task)       # Eliminar con Suprimir
root.bind('<Escape>', exit_app)          # Salir con Escape

# Ejecutar ventana
root.mainloop()
