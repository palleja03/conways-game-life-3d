import unittest
from life_simulation import Life_Simulation

class Tests(unittest.TestCase):

    def test_life_simulation_add(self):
        ls = Life_Simulation()
        ls.add_cell(1,2)
        coordinates = (1,2)
        self.assertEqual(
            ls._cells,
            set([coordinates]),
        )


    def test_life_simulation_del(self):
        ls = Life_Simulation()
        ls.add_cell(1,2)
        ls.add_cell(0,0)
        ls.kill_cell(0,0)
        coordinates = (1,2)
        self.assertEqual(
            ls._cells,
            set([coordinates]),
        )

    def test_life_simulation_get_num_neighbors(self):
        ls = Life_Simulation()
        ls.add_cell(1,1)
        ls.add_cell(1,2)
        ls.add_cell(2,2)
        ls.add_cell(3,2)
        ls.add_cell(3,3)
        ls.add_cell(0,0)
        ls.add_cell(1,0)
        ls.add_cell(4,0)

        self.assertEqual(
            ls.get_num_neighbors(0,0),
            2
        )
        self.assertEqual(
            ls.get_num_neighbors(4,0),
            0
        )
        self.assertEqual(
            ls.get_num_neighbors(3,2),
            2
        )

    def test_life_simulation_get_next_gen(self):

        # block
        ls_b = Life_Simulation()
        ls_b.add_cell(1,1)
        ls_b.add_cell(1,2)
        ls_b.add_cell(2,1)
        ls_b.add_cell(2,2)

        # beehive
        ls_bee = Life_Simulation()
        ls_bee.add_cell(1,2)
        ls_bee.add_cell(1,3)
        ls_bee.add_cell(2,1)
        ls_bee.add_cell(2,4)
        ls_bee.add_cell(3,2)
        ls_bee.add_cell(3,3)

        # toad
        ls_t0 = Life_Simulation()
        ls_t0.add_cell(2,2)
        ls_t0.add_cell(2,3)
        ls_t0.add_cell(2,4)
        ls_t0.add_cell(3,1)
        ls_t0.add_cell(3,2)
        ls_t0.add_cell(3,3)

        ls_t1 = Life_Simulation()
        ls_t1.add_cell(2,1)
        ls_t1.add_cell(3,1)
        ls_t1.add_cell(4,2)
        ls_t1.add_cell(1,3)
        ls_t1.add_cell(2,4)
        ls_t1.add_cell(3,4)


        

        # self.assertEqual(
        #     ls_b.get_next_generation(),
        #     ls_b._cells
        # )

        # self.assertEqual(
        #     ls_bee.get_next_generation(),
        #     ls_bee._cells
        # )

        self.assertEqual(
            ls_t0.get_next_generation(),
            ls_t1._cells
        )
        

if __name__ == "__main__":
    unittest.main()