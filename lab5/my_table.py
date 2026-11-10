import tkinter as tk
from tkinter import ttk

class MyTable:
    def __init__(self, parent, on_select=None, on_delete=None):
        self.parent = parent
        self.on_select = on_select
        self.on_delete = on_delete
        
        self.window = tk.Toplevel(parent)
        self.window.title("Таблиця графічних об'єктів")
        self.window.geometry("420x340")
        self.window.protocol("WM_DELETE_WINDOW", self.hide)
        self.window.withdraw()
        
        columns = ("name", "x1", "y1", "x2", "y2")
        self.tree = ttk.Treeview(self.window, columns=columns, show="headings")
        self.tree.heading("name", text="Назва")
        self.tree.heading("x1", text="x1")
        self.tree.heading("y1", text="y1")
        self.tree.heading("x2", text="x2")
        self.tree.heading("y2", text="y2")
        
        self.tree.column("name", width=140)
        self.tree.column("x1", width=50)
        self.tree.column("y1", width=50)
        self.tree.column("x2", width=50)
        self.tree.column("y2", width=50)
        
        self.tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        bottom_frame = tk.Frame(self.window)
        bottom_frame.pack(fill=tk.X, pady=5)
        
        del_btn = tk.Button(bottom_frame, text="Видалити", command=self._on_delete_btn)
        del_btn.pack(pady=5)
        
        self.tree.bind("<<TreeviewSelect>>", self._on_select)
        
    def show(self):
        self.window.deiconify()
        
    def hide(self):
        self.window.withdraw()
        
    def toggle(self):
        if self.window.state() == "normal":
            self.hide()
        else:
            self.show()
            
    def update_data(self, data):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for idx, row in enumerate(data):
            self.tree.insert("", tk.END, iid=str(idx), values=row)
            
    def _on_select(self, event):
        if self.on_select:
            selected = self.tree.selection()
            if selected:
                self.on_select(int(selected[0]))
                
    def _on_delete_btn(self):
        if self.on_delete:
            selected = self.tree.selection()
            if selected:
                self.on_delete(int(selected[0]))