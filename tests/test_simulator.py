import unittest

from src.simulator import SCENARIOS


class SimulatorTests(unittest.TestCase):
    def test_three_sample_scenarios_are_available(self):
        self.assertEqual(len(SCENARIOS), 3)


if __name__ == "__main__":
    unittest.main()
