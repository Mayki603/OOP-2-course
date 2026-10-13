import tkinter as tk
from shapes import PointShape, LineShape, RectShape, EllipseShape

class EditorApp:
    def __init__(self, root):
        self.root = root
        self.current_tool = "Прямокутник"
        self.update_title()
        
        self.shapes = []
        self.max_shapes = 107
        
        self.start_x = None
        self.start_y = None
        self.rubber_id = None
        
        self.setup_menu()
        
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def update_title(self):
        self.root.title(f"Лабораторна робота №2 - {self.current_tool}")

    def set_tool(self, tool_name):
        self.current_tool = tool_name
        self.update_title()

    def setup_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Файл", menu=file_menu)
        
        obj_menu = tk.Menu(menubar, tearoff=0)
        obj_menu.add_command(label="Крапка", command=lambda: self.set_tool("Крапка"))
        obj_menu.add_command(label="Лінія", command=lambda: self.set_tool("Лінія"))
        obj_menu.add_command(label="Прямокутник", command=lambda: self.set_tool("Прямокутник"))
        obj_menu.add_command(label="Еліпс", command=lambda: self.set_tool("Еліпс"))
        menubar.add_cascade(label="Об'єкти", menu=obj_menu)
        
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Довідка", menu=help_menu)

    def on_press(self, event):
        if len(self.shapes) >= self.max_shapes:
            return
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        if self.start_x is None: 
            return
            
        if self.rubber_id:
            self.canvas.delete(self.rubber_id)
            
        if self.current_tool == "Крапка":
            pass 
        elif self.current_tool == "Лінія":
            self.rubber_id = self.canvas.create_line(
                self.start_x, self.start_y, event.x, event.y, dash=(4, 4), fill="black")
        elif self.current_tool == "Прямокутник":
            dx = abs(event.x - self.start_x)
            dy = abs(event.y - self.start_y)
            self.rubber_id = self.canvas.create_rectangle(
                self.start_x - dx, self.start_y - dy, self.start_x + dx, self.start_y + dy, 
                dash=(4, 4), outline="black")
        elif self.current_tool == "Еліпс":
            self.rubber_id = self.canvas.create_oval(
                self.start_x, self.start_y, event.x, event.y, 
                dash=(4, 4), outline="black")

    def on_release(self, event):
        if self.start_x is None: 
            return
            
        if self.rubber_id:
            self.canvas.delete(self.rubber_id)
            self.rubber_id = None

        shape = None
        if self.current_tool == "Крапка":
            shape = PointShape(event.x, event.y, event.x, event.y)
        elif self.current_tool == "Лінія":
            shape = LineShape(self.start_x, self.start_y, event.x, event.y)
        elif self.current_tool == "Прямокутник":
            shape = RectShape(self.start_x, self.start_y, event.x, event.y)
        elif self.current_tool == "Еліпс":
            shape = EllipseShape(self.start_x, self.start_y, event.x, event.y)

        if shape:
            self.shapes.append(shape)
            shape.draw(self.canvas)

        self.start_x = None
        self.start_y = None

if __name__ == "__main__":
    main_window = tk.Tk()
    main_window.geometry("800x600")
    app = EditorApp(main_window)
    main_window.mainloop()