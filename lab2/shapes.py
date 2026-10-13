class Shape:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, canvas):
        pass

class PointShape(Shape):
    def draw(self, canvas):
        r = 4
        canvas.create_oval(
            self.x2 - r, self.y2 - r, 
            self.x2 + r, self.y2 + r, 
            fill="black", outline="black"
        )

class LineShape(Shape):
    def draw(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="black")

class RectShape(Shape):
    def draw(self, canvas):
        dx = abs(self.x2 - self.x1)
        dy = abs(self.y2 - self.y1)
        canvas.create_rectangle(
            self.x1 - dx, self.y1 - dy, 
            self.x1 + dx, self.y1 + dy, 
            outline="black", fill="lightgreen"
        )

class EllipseShape(Shape):
    def draw(self, canvas):
        canvas.create_oval(
            self.x1, self.y1, self.x2, self.y2, 
            outline="black", fill=""
        )