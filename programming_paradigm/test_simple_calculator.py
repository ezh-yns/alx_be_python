import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(1.5, 1.5), 3.0)
        self.assertEqual(self.calc.add("Hello", "world"), "Hello World")
        self.assertEqual(self.calc.add([1, 2], [3, 4]), [1, 2, 3, 4])
        # Add more assertions to thoroughly test the add method.
   

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 2), 3)  
        self.assertEqual(self.calc.subtract(-5, -2), -7)  
        self.assertEqual(self.calc.subtract(6.5, 2.5), 4.0)  

    
    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(5, 2), 10)  
        self.assertEqual(self.calc.multiply(-5, 2), -10)  
        self.assertEqual(self.calc.multiply(2.5, 2.5), 6.25)  


    def test_divide(self):
        """Test the devide method."""
        self.assertEqual(self.calc.divide(10, 2), 5)  
        self.assertEqual(self.calc.divide(10.5, 2.5), 4.2)  
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(1, 0)


if __name__ == '__main__':
    unittest.main()
