import unittest

import pandas as pd

from Building import Building
from Utilities import normalize_speed
import Ex1


class MyTestCase(unittest.TestCase):
    def test_normalize_speed(self):
        building_path = "Ex1_input/Ex1_Buildings/B2.json"
        b = Building(building_path)
        elevators = b.get_elevators()  # 2 Elevators: speeds: 1.0, 2.0
        normalize_speed(elevators)
        self.assertAlmostEqual(elevators[0].get_norm_speed(), 0.33333, places=4)
        self.assertAlmostEqual(elevators[1].get_norm_speed(), 0.66666, places=4)

        building_path = "Ex1_input/Ex1_Buildings/B3.json"
        b = Building(building_path)
        elevators = b.get_elevators()  # 2 Elevators: speeds: 3.0, 7.0
        normalize_speed(elevators)
        self.assertAlmostEqual(elevators[0].get_norm_speed(), 0.3, places=4)
        self.assertAlmostEqual(elevators[1].get_norm_speed(), 0.7, places=4)

        building_path = "Ex1_input/Ex1_Buildings/B4.json"
        b = Building(building_path)
        elevators = b.get_elevators()  # 5 Elevators: speeds: 1.0, 2.0, 8.0, 6.0, 2.0
        normalize_speed(elevators)
        self.assertAlmostEqual(elevators[0].get_norm_speed(), 0.05263, places=4)
        self.assertAlmostEqual(elevators[1].get_norm_speed(), 0.10526, places=4)
        self.assertAlmostEqual(elevators[2].get_norm_speed(), 0.42105, places=4)
        self.assertAlmostEqual(elevators[3].get_norm_speed(), 0.31578, places=4)
        self.assertAlmostEqual(elevators[4].get_norm_speed(), 0.10526, places=4)

    def test_main(self):
        building_path = "Ex1_input/Ex1_Buildings/B3.json"
        input_path = "Ex1_input/Ex1_Calls/Calls_b.csv"
        output_path = "Ex1_input/output.csv"
        Ex1.main(building_path, input_path, output_path)
        df = pd.read_csv(output_path, index_col=False, header=None)
        self.assertTrue(df[[5]].value_counts()[0] > 250)
        self.assertTrue(df[[5]].value_counts()[1] > 650)


if __name__ == '__main__':
    unittest.main()
