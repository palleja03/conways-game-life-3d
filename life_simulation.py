import os
import time

class Life_Simulation:
    def __init__(self, size = 0, torus= False):
        self._cells = set([])
        self._generation = 0
        self._initial_cells = set([])

    def add_cell(self, i,j):
        self._cells.add((i,j))
        if self._generation == 0:
            self._initial_cells.add((i,j))

    def kill_cell(self, i,j):
        if (i,j) in self._cells:
            self._cells.remove((i,j))
        if self._generation == 0 and (i,j) in self._initial_cells:
            self._initial_cells.remove((i,j))
    

    def get_next_generation(self):
        next_gen = set([])
        adjacent_dead_cells = set([])

        for cell in self._cells:
            i,j = cell[0], cell[1]
            num_neighbors = self.get_num_neighbors(i,j)
            adjacent_cells = [(i + k%3-1,j + k//3 -1) for k in range(9) if k!=4]
            if num_neighbors in (2,3):
                next_gen.add(cell)
            for ad_cell in adjacent_cells:
                if ad_cell not in self._cells:
                    adjacent_dead_cells.add(ad_cell)
            
        for ad_cell in adjacent_dead_cells:
            num_neighbors = self.get_num_neighbors(ad_cell[0], ad_cell[1])
            if num_neighbors == 3:
                next_gen.add(ad_cell)
        
        return next_gen
    
    def advance_generation(self):
        self._cells = self.get_next_generation()
        self._generation += 1

    def get_num_neighbors(self, i,j):
        result = 0
        for x in range(3):
            for y in range(3):
                if (x-1 == 0 and y-1 == 0):
                    continue
                elif (i + (x-1), j + (y-1)) in self._cells:
                    result += 1
        return result


    def print_grid(self, grid_size=10, live_cell='o'):
        dead_cell = ' '
        rows = []

        for j in range(grid_size):
            row = ""
            for i in range(grid_size):
                if (i, j) in self._cells:
                    row += live_cell
                else:
                    row += dead_cell
            rows.append(row)

        for row in rows[::-1]:
            print(row)
        print("________________________________________________________")

        spacing_format = " "*(15 -len(str(len(self._cells))))
        print(f"Population: {len(self._cells)}{spacing_format} Generation: {self._generation}")
        time.sleep(0.5)

    def run_simulation(self, generations=10, grid_size=10, live_cell='o'):
        for generation in range(generations):
            print_clear()
            self.print_grid(grid_size, live_cell)
            self.advance_generation()


if __name__ == "__main__":
    def print_clear():
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')

    def penta_decathlon_sim():
        # Example usage
        sim = Life_Simulation()
        # Add Penta-decathlon
        sim.add_cell(5,5)
        sim.add_cell(5,6)
        sim.add_cell(4,7)
        sim.add_cell(6,7)
        sim.add_cell(5,8)
        sim.add_cell(5,9)
        sim.add_cell(5,10)
        sim.add_cell(5,11)
        sim.add_cell(4,12)
        sim.add_cell(6,12)
        sim.add_cell(5,13)
        sim.add_cell(5,14)


        # Run the simulation
        sim.run_simulation(generations=100, grid_size=20, live_cell='o')

    penta_decathlon_sim()