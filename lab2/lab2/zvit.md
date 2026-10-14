```mermaid
classDiagram
    class Shape {
        <<abstract>>
        +int x1
        +int y1
        +int x2
        +int y2
        +__init__(x1, y1, x2, y2)
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

    class EditorApp {
        +Tk root
        +str current_tool
        +list shapes
        +int max_shapes
        +__init__(root)
        +update_title()
        +set_tool(tool_name)
        +setup_menu()
        +redraw_all()
        +on_press(event)
        +on_drag(event)
        +on_release(event)
    }

    Shape <|-- PointShape : успадковує
    Shape <|-- LineShape : успадковує
    Shape <|-- RectShape : успадковує
    Shape <|-- EllipseShape : успадковує
    EditorApp o-- Shape : містить масив об'єктів