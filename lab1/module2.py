import tkinter as tk

def open_dialog(parent, result_label):
    dialog = tk.Toplevel(parent)
    dialog.title("Робота 2 (Варіант 0)")
    dialog.geometry("300x150")
    
    entry = tk.Entry(dialog, font=("Arial", 12), width=25)
    entry.pack(pady=25)
    
    def on_yes():
        result_label.config(text=entry.get())
        dialog.destroy()
        
    def on_cancel():
        dialog.destroy()
        
    btn_frame = tk.Frame(dialog)
    btn_frame.pack(pady=10)
    
    tk.Button(btn_frame, text="Так", command=on_yes, width=10).pack(side=tk.LEFT, padx=10)
    tk.Button(btn_frame, text="Відміна", command=on_cancel, width=10).pack(side=tk.LEFT, padx=10)
    
    return dialog