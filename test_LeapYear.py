import unittest
import LeapYear

class TestLeapYear(unittest.TestCase):

    # Test to detect years divisible by 4
    def test_DivFour(self):
        self.assertEqual(LeapYear.DivFour(2001), False)
        self.assertEqual(LeapYear.DivFour(2020), True)
        self.assertEqual(LeapYear.DivFour(1996), True)
        self.assertEqual(LeapYear.DivFour(1999), False)

    def test_DivHundred(self):
        self.assertEqual(LeapYear.DivHundred(2002), False)
        self.assertEqual(LeapYear.DivHundred(1900), True)
        self.assertEqual(LeapYear.DivHundred(2000), True)
        self.assertEqual(LeapYear.DivHundred(2019), False)

    def test_DivHundredFour(self):
        self.assertEqual(LeapYear.DivHundredFour(2200), False)
        self.assertEqual(LeapYear.DivHundredFour(4000), True)
        self.assertEqual(LeapYear.DivHundredFour(2000), True)
        self.assertEqual(LeapYear.DivHundredFour(2100), False)

if __name__ == '__main__':
    unittest.main()