import unittest
import FizzBuzz

class   TestFizzBuzz(unittest.TestCase):

    # Test for Fizz -> Multiple of Three
    def test_Fizz(self):
        self.assertEqual(FizzBuzz.check_Fizz(1), 1)
        self.assertEqual(FizzBuzz.check_Fizz(3), 'Fizz')
        self.assertEqual(FizzBuzz.check_Fizz(5), 5)
        self.assertEqual(FizzBuzz.check_Fizz(7), 7)
        self.assertEqual(FizzBuzz.check_Fizz(9), 'Fizz')

if __name__ == '__main__':
    unittest.main()