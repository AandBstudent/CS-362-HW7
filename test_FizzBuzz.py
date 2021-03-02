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

    # Test for Buzz -> Multiple of Five
    def test_Buzz(self):
        self.assertEqual(FizzBuzz.check_Buzz(5), 'Buzz')
        self.assertEqual(FizzBuzz.check_Buzz(6), 6)
        self.assertEqual(FizzBuzz.check_Buzz(20), 'Buzz')
        self.assertEqual(FizzBuzz.check_Buzz(24), 24)
        self.assertEqual(FizzBuzz.check_Buzz(35), 'Buzz')

    def test_FizzBuzz(self):
        self.assertEqual(FizzBuzz.check_FizzBuzz(5), 5)
        self.assertEqual(FizzBuzz.check_FizzBuzz(15), 'FizzBuzz')
        self.assertEqual(FizzBuzz.check_FizzBuzz(20), 20)
        self.assertEqual(FizzBuzz.check_FizzBuzz(30), 'FizzBuzz')

if __name__ == '__main__':
    unittest.main()