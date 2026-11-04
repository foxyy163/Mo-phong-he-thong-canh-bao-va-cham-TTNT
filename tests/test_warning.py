import unittest

from src.warning_engine import assess_risk


class WarningEngineTests(unittest.TestCase):
    def test_close_distance_at_high_speed_is_dangerous(self):
        self.assertEqual(assess_risk(90, 8)["level"], "Nguy hiểm")

    def test_negative_input_is_rejected(self):
        with self.assertRaises(ValueError):
            assess_risk(-1, 10)


if __name__ == "__main__":
    unittest.main()
