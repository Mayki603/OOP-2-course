import tkinter as tk
from shapes import PointShape, LineShape, RectShape, EllipseShape

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip_window = None
        self.widget.bind("<Enter>", self.show_tip)
        self.widget.bind("<Leave>", self.hide_tip)

    def show_tip(self, event=None):
        if self.tip_window or not self.text:
            return
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + 25
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(
            tw, text=self.text, background="#ffffe0", 
            relief=tk.SOLID, borderwidth=1, font=("Tahoma", "8", "normal")
        )
        label.pack(ipadx=2, ipady=1)

    def hide_tip(self, event=None):
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()

class EditorApp:
    def __init__(self, root):
        self.root = root
        self.current_tool = "Прямокутник"
        
        self.shapes = []
        self.max_shapes = 108
        
        self.start_x = None
        self.start_y = None
        self.rubber_id = None
        self.tool_buttons = {}
        
        self.setup_menu()
        self.setup_toolbar()
        
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        
        self.update_menu_and_title()

    def set_tool(self, tool_name):
        self.current_tool = tool_name
        self.update_menu_and_title()

    def update_menu_and_title(self):
        self.root.title("Лабораторна робота №3")
        
        tools = ["Крапка", "Лінія", "Прямокутник", "Еліпс"]
        for idx, tool in enumerate(tools):
            prefix = "✓ " if tool == self.current_tool else "   "
            self.obj_menu.entryconfig(idx, label=f"{prefix}{tool}")
            
        for name, btn in self.tool_buttons.items():
            if name == self.current_tool:
                btn.config(relief=tk.SUNKEN, bg="#d0d0d0")
            else:
                btn.config(relief=tk.RAISED, bg="#f0f0f0")

    def setup_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Файл", menu=file_menu)
        
        self.obj_menu = tk.Menu(menubar, tearoff=0)
        tools = ["Крапка", "Лінія", "Прямокутник", "Еліпс"]
        for tool in tools:
            self.obj_menu.add_command(
                label=tool, 
                command=lambda t=tool: self.set_tool(t)
            )
        menubar.add_cascade(label="Об'єкти", menu=self.obj_menu)
        
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Довідка", menu=help_menu)

    def setup_toolbar(self):
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED, bg="#f0f0f0")
        
        tools = [
            ("Крапка", "Малювання крапки"),
            ("Лінія", "Малювання лінії"),
            ("Прямокутник", "Малювання прямокутника"),
            ("Еліпс", "Малювання еліпса")
        ]
        
        for name, hint in tools:
            btn = tk.Button(
                toolbar, text=name, command=lambda n=name: self.set_tool(n), 
                width=12, relief=tk.RAISED
            )
            btn.pack(side=tk.LEFT, padx=2, pady=2)
            ToolTip(btn, hint)
            self.tool_buttons[name] = btn
            
        toolbar.pack(side=tk.TOP, fill=tk.X)

    def redraw_all(self):
        self.canvas.delete("all")
        for shape in self.shapes:
            shape.draw(self.canvas)

    def add_shape(self, shape):
        if len(self.shapes) >= self.max_shapes:
            self.shapes.pop(0)
        self.shapes.append(shape)
        self.redraw_all()

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

        if self.current_tool == "Крапка":
            self.add_shape(PointShape(event.x, event.y, event.x, event.y))

    def on_drag(self, event):
        if self.current_tool == "Крапка":
            self.add_shape(PointShape(event.x, event.y, event.x, event.y))
            return

        if self.start_x is None: 
            return

        self.redraw_all()
            
        if self.current_tool == "Лінія":
            self.rubber_id = self.canvas.create_line(
                self.start_x, self.start_y, event.x, event.y, fill="black")
        elif self.current_tool == "Прямокутник":
            self.rubber_id = self.canvas.create_rectangle(
                self.start_x, self.start_y, event.x, event.y, outline="black")
        elif self.current_tool == "Еліпс":
            dx = abs(event.x - self.start_x)
            dy = abs(event.y - self.start_y)
            self.rubber_id = self.canvas.create_oval(
                self.start_x - dx, self.start_y - dy, 
                self.start_x + dx, self.start_y + dy, 
                outline="black")

    def on_release(self, event):
        if self.current_tool == "Крапка":
            self.start_x = None
            self.start_y = None
            return

        if self.start_x is None: 
            return

        shape = None
        if self.current_tool == "Лінія":
            shape = LineShape(self.start_x, self.start_y, event.x, event.y)
        elif self.current_tool == "Прямокутник":
            shape = RectShape(self.start_x, self.start_y, event.x, event.y)
        elif self.current_tool == "Еліпс":
            shape = EllipseShape(self.start_x, self.start_y, event.x, event.y)

        if shape:
            self.add_shape(shape)

        self.start_x = None
        self.start_y = None

if __name__ == "__main__":
    main_window = tk.Tk()
    main_window.geometry("800x600")
    app = EditorApp(main_window)
    main_window.mainloop()