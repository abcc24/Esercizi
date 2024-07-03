import unittest
from calc import Calculations

class TestCalc(unittest.TestCase):
    def test_sum(self):
        calc_1 = Calculations (a=2, b=3)
        result = calc_1.get_sum()
        self.assertEqual(result, 5, msg = f"Error Test Failed {result}")


if __name__ == "__main__":
    unittest.main()

    ###