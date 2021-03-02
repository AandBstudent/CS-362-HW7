import unittest
import LeapYear

class TestLeapYear(unittest.TestCase):

    # Test to detect years divisible by 4
    def test_DivFour(self):
        self.assertEqual(LeapYear.LeapYear(2001), 'is not a leap year')
        self.assertEqual(LeapYear.LeapYear(2020), 'is a leap year')
        self.assertEqual(LeapYear.LeapYear(1996), 'is a leap year')
        self.assertEqual(LeapYear.LeapYear(1999), 'is not a leap year')
        
if __name__ == '__main__':
    unittest.main()