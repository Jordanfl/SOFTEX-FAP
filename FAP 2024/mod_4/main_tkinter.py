import tkinter as tk
from tkinter import ttk
import json

class ToDoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        # Frame principal para organizar os widgets
        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Campo de entrada e botão "Adicionar"
        self.task_entry = ttk.Entry(main_frame, width=40)
        self.task_entry.grid(row=0, column=0, padx=(0, 5))
        add_button = ttk.Button(main_frame, text="Adicionar", command=self.add_task)
        add_button.grid(row=0, column=1)

        # Lista de tarefas
        self.task_list = tk.Listbox(main_frame, height=10, width=50)
        self.task_list.grid(row=1, column=0, columnspan=2, pady=10)

        # Botões de ação
        complete_button = ttk.Button(main_frame, text="Concluir", command=self.complete_task)
        complete_button.grid(row=2, column=0, sticky=tk.E, padx=(0, 5))
        remove_button = ttk.Button(main_frame, text="Remover", command=self.remove_task)
        remove_button.grid(row=2, column=1, sticky=tk.W)

    def add_task(self):
        # Lógica para adicionar tarefas (ver seção 12.3)
        task = self.task_entry.get()
        if task:
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        pass

    def complete_task(self):
        # Lógica para marcar como concluída (ver seção 12.3)
        try: 
            index = self.task_list.curselection()[0]
            self.task_list.itemconfig(index, foreground="gray")
        except IndexError:
            pass

    def remove_task(self):
        # Lógica para remover tarefas (ver seção 12.3)
        try:
            index = self.task_list.curselection()[0]
            self.task_list.delete(index)
        except IndexError:
            pass
    def save_tasks(self):
        # Lógica para salvar tarefas (ver seção 12.3)
        tasks = self.task_list.get(0, tk.END)
        with open("tasks.txt", "w") as f:
            json.dump(tasks, f)
        
    def load_tasks(self):
        # Lógica para carregar tarefas (ver seção 12.3)
        try:
            with open("tasks.txt", "r") as f:
                tasks = json.load(f)
                for task in tasks:
                    self.task_list.insert(tk.END, task)
        except FileNotFoundError:
            pass
if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()