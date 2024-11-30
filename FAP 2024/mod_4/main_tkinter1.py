import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import datetime


class Tarefa:
    def __init__(self, descricao, prioridade, data):
        self.descricao = descricao
        self.prioridade = prioridade
        self.data = data


class ToDoApp(tk.Tk):
    """Classe principal para a aplicação To-Do List."""


    def __init__(self):
        """Inicializa a aplicação."""
        super().__init__()
        self.title("To-Do List")
        self.geometry("620x330") # Define tamanho da janela
        self.tasks = []  # Lista para armazenar as tarefas
        self.create_widgets()


    def create_widgets(self):
        """Cria os widgets da interface."""
        main_frame = ttk.Frame(self, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Rótulo e entrada para Tarefa
        ttk.Label(main_frame, text="Tarefa:").grid(row=0, column=0, padx=(0, 5), pady=5, sticky=tk.W)
        self.task_entry = ttk.Entry(main_frame, width=20)
        self.task_entry.grid(row=0, column=1, padx=(0, 5), pady=5, sticky=tk.W)

        # Rótulo e combobox para Prioridade
        ttk.Label(main_frame, text="Prioridade:").grid(row=0, column=2, padx=(10, 5), pady=5, sticky=tk.W)
        self.priority_var = tk.StringVar()
        self.priority_combobox = ttk.Combobox(
            main_frame, textvariable=self.priority_var, values=["Baixa", "Média", "Alta"], state="readonly", width=10
        )
        self.priority_combobox.grid(row=0, column=3, padx=(0, 5), pady=5, sticky=tk.W)
        self.priority_combobox.current(0)  # Define a opção padrão

        # Rótulo e DateEntry para Data
        ttk.Label(main_frame, text="Data:").grid(row=0, column=4, padx=(10, 5), pady=5, sticky=tk.W)
        self.date_entry = DateEntry(main_frame, date_pattern='mm/dd/yy')
        self.date_entry.grid(row=0, column=5, padx=(0, 5), pady=5, sticky=tk.W)

        # Botões para adicionar, concluir e remover tarefas
        action_frame = ttk.Frame(main_frame)
        action_frame.grid(row=1, column=0, columnspan=6, pady=5)

        ttk.Button(action_frame, text="Adicionar", command=self.add_task).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(action_frame, text="Concluir", command=self.complete_task).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(action_frame, text="Remover", command=self.remove_task).grid(row=0, column=2, padx=5, pady=5)

        # Lista de tarefas
        self.task_list = ttk.Treeview(main_frame, columns=("priority", "date", "status"), show='headings')
        self.task_list.heading("priority", text="Prioridade")
        self.task_list.heading("date", text="Data")
        self.task_list.heading("status", text="Status")
        self.task_list.grid(row=2, column=0, columnspan=6, pady=10, sticky='nsew')


    def add_task(self):
        """Adiciona uma nova tarefa à lista."""
        task = self.task_entry.get()
        priority = self.priority_var.get()
        date_str = self.date_entry.get()
        
        try:
            # Ajuste o formato da data para corresponder ao formato fornecido (mes/dia/ano com ano de 2 dígitos)
            date = datetime.datetime.strptime(date_str, '%m/%d/%y').date()
        except ValueError:
            messagebox.showerror("Erro de Data", "Formato da data inválido. Use MM/DD/YY.")
            return

        if task:
            new_task = Tarefa(task, priority, date)
            self.tasks.append(new_task)
            self.task_list.insert("", tk.END, values=(priority, date.strftime('%m/%d/%Y'), "Pendente"))
            self.task_entry.delete(0, tk.END)
            self.priority_var.set("Baixa")
            self.date_entry.set_date(datetime.date.today())
        else:
            messagebox.showwarning("Aviso", "Por favor, insira uma tarefa.")


    def complete_task(self):
        """Marca a tarefa selecionada como concluída."""
        try:
            selected_item = self.task_list.selection()[0]
            task_values = self.task_list.item(selected_item, "values")
            self.task_list.item(selected_item, values=(task_values[0], task_values[1], "Concluída"))
        except IndexError:
            messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para concluir.")


    def remove_task(self):
        """Remove a tarefa selecionada da lista."""
        try:
            selected_item = self.task_list.selection()[0]
            self.task_list.delete(selected_item)
        except IndexError:
            messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para remover.")


if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()
