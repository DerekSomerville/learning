import unittest
from FizzBuzz import fizzBuzz

class test_FizzBuss(unittest.TestCase):

    def test_Fizz(self):
        self.assertEqual(fizzBuzz(3),"Fizz")

    def main():
        unittest.main()

if __name__ == "__main__":
    unittest.main()
