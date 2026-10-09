import tkinter as tk

def open_dialog(parent, result_label):
    dialog = tk.Toplevel(parent)
    dialog.title("Робота 1 (Варіант 3)")
    dialog.geometry("300x250")
    
    listbox = tk.Listbox(dialog, font=("Arial", 11))
    groups = ["ІМ-55", "ІМ-51", "ІМ-53", "ІМ-54", "ІМ-52", "ІМ-051"]
    for g in groups:
        listbox.insert(tk.END, g)
    listbox.pack(pady=15, fill=tk.BOTH, expand=True, padx=20)
    
    def on_yes():
        selection = listbox.curselection()
        if selection:
            result_label.config(text=listbox.get(selection[0]))
        dialog.destroy()
        
    def on_cancel():
        dialog.destroy()
        
    btn_frame = tk.Frame(dialog)
    btn_frame.pack(pady=10)
    
    tk.Button(btn_frame, text="Так", command=on_yes, width=10).pack(side=tk.LEFT, padx=10)
    tk.Button(btn_frame, text="Відміна", command=on_cancel, width=10).pack(side=tk.LEFT, padx=10)
    
    return dialog