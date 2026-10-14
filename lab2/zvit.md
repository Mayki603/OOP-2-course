```mermaid
classDiagram
    class EditorApp {
        +current_tool
        +shapes
        +max_shapes
        +update_title()
        +set_tool()
        +setup_menu()
        +redraw_all()
        +on_press()
        +on_drag()
        +on_release()
    }
    
    class Shape {
        <<abstract>>
        +x1, y1, x2, y2
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
    EditorApp o-- Shape : містить масив
    ```