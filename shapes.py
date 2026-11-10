class Shape:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, canvas):
        pass

    def draw_rubber(self, canvas):
        pass


class PointShape(Shape):
    def draw(self, canvas):
        r = 4
        canvas.create_oval(
            self.x2 - r, self.y2 - r, 
            self.x2 + r, self.y2 + r, 
            fill="black", outline="black"
        )

    def draw_rubber(self, canvas):
        self.draw(canvas)


class LineShape(Shape):
    def draw(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="black")

    def draw_rubber(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, dash=(4, 4), fill="black")


class RectShape(Shape):
    def draw(self, canvas):
        canvas.create_rectangle(
            self.x1, self.y1, self.x2, self.y2, 
            outline="black", fill=""
        )

    def draw_rubber(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, dash=(4, 4), outline="black")


class EllipseShape(Shape):
    def draw(self, canvas):
        dx = abs(self.x2 - self.x1)
        dy = abs(self.y2 - self.y1)
        canvas.create_oval(
            self.x1 - dx, self.y1 - dy, 
            self.x1 + dx, self.y1 + dy, 
            outline="black", fill="lightgreen"
        )

    def draw_rubber(self, canvas):
        dx = abs(self.x2 - self.x1)
        dy = abs(self.y2 - self.y1)
        canvas.create_oval(self.x1 - dx, self.y1 - dy, self.x1 + dx, self.y1 + dy, dash=(4, 4), outline="black")


class LineOOShape(LineShape, EllipseShape):
    def draw(self, canvas):
        orig_x1, orig_y1, orig_x2, orig_y2 = self.x1, self.y1, self.x2, self.y2
        
        LineShape.draw(self, canvas)
        
        R = 3
        self.x1, self.y1 = orig_x1, orig_y1
        self.x2, self.y2 = orig_x1 + R, orig_y1 + R
        EllipseShape.draw(self, canvas)
        
        self.x1, self.y1 = orig_x2, orig_y2
        self.x2, self.y2 = orig_x2 + R, orig_y2 + R
        EllipseShape.draw(self, canvas)
        
        self.x1, self.y1, self.x2, self.y2 = orig_x1, orig_y1, orig_x2, orig_y2

    def draw_rubber(self, canvas):
        orig_x1, orig_y1, orig_x2, orig_y2 = self.x1, self.y1, self.x2, self.y2
        
        LineShape.draw_rubber(self, canvas)
        
        R = 3
        self.x1, self.y1 = orig_x1, orig_y1
        self.x2, self.y2 = orig_x1 + R, orig_y1 + R
        EllipseShape.draw_rubber(self, canvas)
        
        self.x1, self.y1 = orig_x2, orig_y2
        self.x2, self.y2 = orig_x2 + R, orig_y2 + R
        EllipseShape.draw_rubber(self, canvas)
        
        self.x1, self.y1, self.x2, self.y2 = orig_x1, orig_y1, orig_x2, orig_y2


class CubeShape(RectShape, LineShape):
    def draw(self, canvas):
        orig_x1, orig_y1, orig_x2, orig_y2 = self.x1, self.y1, self.x2, self.y2
        
        shift_x = int((orig_x2 - orig_x1) * 0.3)
        shift_y = int((orig_y2 - orig_y1) * 0.3)
        
        self.x1, self.y1 = orig_x1 + shift_x, orig_y1 - shift_y
        self.x2, self.y2 = orig_x2 + shift_x, orig_y2 - shift_y
        RectShape.draw(self, canvas)
        
        self.x1, self.y1 = orig_x1, orig_y1
        self.x2, self.y2 = orig_x2, orig_y2
        RectShape.draw(self, canvas)
        
        self.x1, self.y1 = orig_x1, orig_y1
        self.x2, self.y2 = orig_x1 + shift_x, orig_y1 - shift_y
        LineShape.draw(self, canvas)
        
        self.x1, self.y1 = orig_x2, orig_y2
        self.x2, self.y2 = orig_x2 + shift_x, orig_y2 - shift_y
        LineShape.draw(self, canvas)
        
        self.x1, self.y1 = orig_x2, orig_y1
        self.x2, self.y2 = orig_x2 + shift_x, orig_y1 - shift_y
        LineShape.draw(self, canvas)
        
        self.x1, self.y1 = orig_x1, orig_y2
        self.x2, self.y2 = orig_x1 + shift_x, orig_y2 - shift_y
        LineShape.draw(self, canvas)
        
        self.x1, self.y1, self.x2, self.y2 = orig_x1, orig_y1, orig_x2, orig_y2

    def draw_rubber(self, canvas):
        orig_x1, orig_y1, orig_x2, orig_y2 = self.x1, self.y1, self.x2, self.y2
        
        shift_x = int((orig_x2 - orig_x1) * 0.3)
        shift_y = int((orig_y2 - orig_y1) * 0.3)
        
        self.x1, self.y1 = orig_x1 + shift_x, orig_y1 - shift_y
        self.x2, self.y2 = orig_x2 + shift_x, orig_y2 - shift_y
        RectShape.draw_rubber(self, canvas)
        
        self.x1, self.y1 = orig_x1, orig_y1
        self.x2, self.y2 = orig_x2, orig_y2
        RectShape.draw_rubber(self, canvas)
        
        self.x1, self.y1 = orig_x1, orig_y1
        self.x2, self.y2 = orig_x1 + shift_x, orig_y1 - shift_y
        LineShape.draw_rubber(self, canvas)
        
        self.x1, self.y1 = orig_x2, orig_y2
        self.x2, self.y2 = orig_x2 + shift_x, orig_y2 - shift_y
        LineShape.draw_rubber(self, canvas)
        
        self.x1, self.y1 = orig_x2, orig_y1
        self.x2, self.y2 = orig_x2 + shift_x, orig_y1 - shift_y
        LineShape.draw_rubber(self, canvas)
        
        self.x1, self.y1 = orig_x1, orig_y2
        self.x2, self.y2 = orig_x1 + shift_x, orig_y2 - shift_y
        LineShape.draw_rubber(self, canvas)
        
        self.x1, self.y1, self.x2, self.y2 = orig_x1, orig_y1, orig_x2, orig_y2