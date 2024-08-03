from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self._height = height
        self._width = width
        self._root = Tk()
        self._root.title("Game of Life")
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._canvas = Canvas(self._root, bg="#282728", height=height, width=width)
        self._canvas.pack(fill=BOTH, expand=1)
        self._running = False
        
    def get_canvas(self):
        return self._canvas
    
    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color = "gray"):
        line.draw(self._canvas, fill_color)

    def close(self):
        self._running = False

class Point:
    def __init__(self, x,y,z=0):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __repr__(self) -> str:
        return f"Point({self.x},{self.y},{self.z})"

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color = "gray"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )