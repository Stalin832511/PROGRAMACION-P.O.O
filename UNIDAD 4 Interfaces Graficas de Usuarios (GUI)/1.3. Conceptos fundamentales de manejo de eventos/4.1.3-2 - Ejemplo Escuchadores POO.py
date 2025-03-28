import tkinter as tk
from tkinter import messagebox


class TaskManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Comentarios Stalin")
        self.master.geometry("400x300")

        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.pack(pady=10)

        self.task_list = tk.Listbox(master, width=50, height=10)
        self.task_list.pack(pady=10)

        self.add_button = tk.Button(master, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack()

        self.complete_button = tk.Button(master, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack()

        self.delete_button = tk.Button(master, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")

    def complete_task(self):
        try:
            selected_task_index = self.task_list.curselection()[0]
            task = self.task_list.get(selected_task_index)
            self.task_list.delete(selected_task_index)
            self.task_list.insert(tk.END, f"✔ {task}")
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

    def delete_task(self):
        try:
            selected_task_index = self.task_list.curselection()[0]
            self.task_list.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()