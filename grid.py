from graphics import Line, Point
import time

class Grid:
    def __init__(self, win, sim = None):
        self.grid_size = 50
        self._sim = sim
        self._win = win
        self.offset_x = 0
        self.offset_y = 0
        self._simmulating = False
        self._win._canvas.bind("<Button-1>", self.start_pan)
        self._win._canvas.bind("<B1-Motion>", self.pan)
        self._win._canvas.bind("<Double-Button-1>", self.start_simulation)
        self._win._canvas.bind("<Button-3>", self.toggle_cell)
        self._win._canvas.bind("<Control Button-1>", self.restart)
        self._win._canvas.bind("<Shift Button-1>", self.pause)
        # self._win._canvas.bind("<MouseWheel>", self.on_mouse_wheel)
        self._win._canvas.bind("<Button-4>", self.on_mouse_wheel_up)
        self._win._canvas.bind("<Button-5>", self.on_mouse_wheel_down)


    def draw(self):
        screen_x = self._win._width
        screen_y = self._win._height
        extra = (screen_x//self.grid_size) // 2
        self._win._canvas.create_rectangle(0, 0, screen_x, screen_y, fill='#282728')

        if self._sim is not None:
            self._win.set_generation(self._sim._generation)
            self._win.set_population(len(self._sim._cells))
            i_range = ((-self.offset_x ) // self.grid_size, (screen_x -self.offset_x ) // self.grid_size)
            j_range = ((self.offset_y ) // self.grid_size, (screen_y + self.offset_y ) // self.grid_size)
            
            for i in range(i_range[0] - extra, i_range[1] + extra):
                for j in range(j_range[0] - extra, j_range[1] + extra):
                    if (i,j) in self._sim._cells:
                        self.draw_cell(i,j, True)

        
        for i in range(screen_x//self.grid_size):
            top_point = Point((self.offset_x + i*self.grid_size) % screen_x, 0)
            bottom_point = Point((self.offset_x + i*self.grid_size) % screen_x, screen_y)
            vertical = Line(top_point, bottom_point)
            self._win.draw_line(vertical)

        for i in range(screen_y//self.grid_size):
            left_point = Point(0, (self.offset_y + i*self.grid_size) % screen_y)
            right_point = Point(screen_x, (self.offset_y + i*self.grid_size) % screen_y)
            horizontal = Line(left_point, right_point)
            self._win.draw_line(horizontal)

    def draw_cell(self, i,j, alive):
        screen_x = self._win._width
        screen_y = self._win._height
        top_left_x = (self.offset_x + i*self.grid_size) 
        top_left_y = (screen_y - (- self.offset_y + (j)*self.grid_size)) 
        fill_color = "#282728"
        if alive:
            fill_color = "#FFFFBF"
        self._win._canvas.create_rectangle(top_left_x, top_left_y, top_left_x + self.grid_size, top_left_y - self.grid_size, fill=fill_color)

    def get_grid_coordinates(self, x,y):
        i = (x - self.offset_x ) // self.grid_size
        j = (self._win._height - (y - self.offset_y )) // self.grid_size
        return i,j

    def toggle_cell(self, event):
        i,j = self.get_grid_coordinates(event.x, event.y)
        if self._sim is None:
            return
        alive = (i,j) in self._sim._cells
        if alive:
            self._sim.kill_cell(i,j)
            self._win.set_population(len(self._sim._cells))
            self.draw_cell(i,j, False)
        else:
            self._sim.add_cell(i,j)
            self._win.set_population(len(self._sim._cells))
            self.draw_cell(i,j, True)

    def start_pan(self, event):
        self.last_x = event.x
        self.last_y = event.y

    def pan(self, event):
        self.offset_x += event.x - self.last_x
        self.offset_y += event.y - self.last_y
        self.last_x = event.x
        self.last_y = event.y
        self.draw()

    def on_mouse_wheel(self, event):
        print(event)
        if event.delta > 0:
            # Scroll up
            self.grid_size += 10
        elif event.delta < 0:
            # Scroll down
            if self.grid_size <25:
                return
            self.grid_size -= 10
        self.draw()

    def on_mouse_wheel_up(self, event):
        self.grid_size += 10
        self.draw()

    def on_mouse_wheel_down(self, event):
        if self.grid_size < 25:
            return
        self.grid_size -= 10
        self.draw()

    def start_simulation(self, _=None):
        if self._sim is None:
            return
        self._simmulating = True
        print("running simmulation...")
        while self._simmulating:
            self._sim.advance_generation()
            self.draw()
            self._animate(0.1)
            

    def restart(self, _):
        print("simmulation restarted...")
        self._simmulating = False
        self._sim._cells = self._sim._initial_cells
        self._sim._generation = 0
        self.draw()

    def pause(self, _):
        if self._simmulating:
            print("simmulation paused...")
            self._simmulating = False
            return
        self.start_simulation()
            

    def _animate(self, animation_speed):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(animation_speed)
