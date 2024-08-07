import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class ToDoList:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("To-Do List")
        self.root.geometry("400x550")
        self.root.configure(bg="#191919")  # Dark background color
        self.tasks = []
        self.create_widgets()
        self.root.mainloop()
    
    def create_widgets(self):
        # Title
        self.title_label = tk.Label(self.root, text="To Do List", font=("Consolas", 24, "bold"), bg="#191919", fg="white")
        self.title_label.pack(pady=(20,0))

        self.task_entry = tk.Entry(self.root, width=50, bg="#0C0C0C", fg="white", insertbackground="white")
        self.task_entry.pack(pady=20)
        
        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task, bg="#3498db", fg="white")
        self.add_task_button.pack(pady=10)
        
        self.task_listbox = tk.Listbox(self.root, width=50, bg="#0C0C0C", fg="white", selectbackground="#3498db")
        self.task_listbox.pack(pady=20)
        
        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task, bg="#e74c3c", fg="white")
        self.delete_task_button.pack(pady=10)
        
        self.update_task_button = tk.Button(self.root, text="Update Task", command=self.update_task, bg="#2ecc71", fg="black")
        self.update_task_button.pack(pady=10)
        
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, bg="#95a5a6", fg="black")
        self.exit_button.pack(pady=10)
    
    def add_task(self):
        task = self.task_entry.get()
        if task == "":
            messagebox.showerror("Error", "Task cannot be empty")
            return
        self.tasks.append(task)
        self.task_listbox.insert(tk.END, task)
        self.task_entry.delete(0, tk.END)
    
    def delete_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(task_index)
            del self.tasks[task_index]
        except:
            messagebox.showerror("Error", "Please select a task to delete")
    
    def update_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            new_task = simpledialog.askstring("Update Task", "Enter new task")
            if new_task == "":
                messagebox.showerror("Error", "Task cannot be empty")
                return
            self.tasks[task_index] = new_task
            self.task_listbox.delete(task_index)
            self.task_listbox.insert(task_index, new_task)
        except:
            messagebox.showerror("Error", "Please select a task to update")

if __name__ == "__main__":
    ToDoList()