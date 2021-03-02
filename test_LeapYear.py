import unittest
import LeapYear

class TestLeapYear(unittest.TestCase):

    # Test to detect years divisible by 4
    def test_DivFour(self):
        self.assertEqual(LeapYear.DivFour(2001), False)
        self.assertEqual(LeapYear.DivFour(2020), True)
        self.assertEqual(LeapYear.DivFour(1996), True)
        self.assertEqual(LeapYear.DivFour(1999), False)

if __name__ == '__main__':
    unittest.main()