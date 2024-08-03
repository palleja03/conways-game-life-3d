from graphics import Window
from life_simulation import Life_Simulation
from grid import Grid


def main():
    screen_x = 1200
    screen_y = 900
    win = Window(screen_x, screen_y)
    sim = Life_Simulation()
    grid = Grid(win, sim)
    grid.draw()
    win.wait_for_close()


main()