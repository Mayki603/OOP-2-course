classDiagram
    class Shape {
        +int x1
        +int y1
        +int x2
        +int y2
        +draw(canvas)
    }
    class PointShape {
        +draw(canvas)
    }
    class LineShape {
        +draw(canvas)
    }
    class RectShape {
        +draw(canvas)
    }
    class EllipseShape {
        +draw(canvas)
    }
    
    Shape <|-- PointShape
    Shape <|-- LineShape
    Shape <|-- RectShape
    Shape <|-- EllipseShape