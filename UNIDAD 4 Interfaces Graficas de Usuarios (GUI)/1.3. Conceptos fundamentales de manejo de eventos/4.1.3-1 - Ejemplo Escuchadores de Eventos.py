import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get().strip()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")

def complete_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task = task_list.get(selected_task_index)
        task_list.delete(selected_task_index)
        task_list.insert(tk.END, f"✔ {task}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

def delete_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

root = tk.Tk()
root.title("Ejemplo de Escuchadores de Eventos Stalin")
root.geometry("400x300")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

task_list = tk.Listbox(root, width=50, height=10)
task_list.pack(pady=10)

add_button = tk.Button(root, text="Añadir Tarea", command=add_task)
add_button.pack()

complete_button = tk.Button(root, text="Marcar como Completada", command=complete_task)
complete_button.pack()

delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_button.pack()

root.mainloop()