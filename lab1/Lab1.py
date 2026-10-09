import tkinter as tk
import module1
import module2

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Лабораторна робота №1")
        self.root.geometry("400x300")
        self.current_dialog = None
        
        self.result_label = tk.Label(root, text="Очікування вводу...", font=("Arial", 14))
        self.result_label.pack(expand=True)
        
        menubar = tk.Menu(root)
        self.root.config(menu=menubar)
        
        menubar.add_command(label="Робота1", command=self.run_work1)
        menubar.add_command(label="Робота2", command=self.run_work2)

    def close_current_dialog(self):
        if self.current_dialog and self.current_dialog.winfo_exists():
            self.current_dialog.destroy()

    def run_work1(self):
        self.close_current_dialog()
        self.current_dialog = module1.open_dialog(self.root, self.result_label)

    def run_work2(self):
        self.close_current_dialog()
        self.current_dialog = module2.open_dialog(self.root, self.result_label)

if __name__ == "__main__":
    main_window = tk.Tk()
    app = App(main_window)
    main_window.mainloop()