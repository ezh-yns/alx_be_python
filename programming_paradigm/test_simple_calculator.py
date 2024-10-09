import unittest
from simple_calculator import SimpleCalculator

class TestAddFunction(unittest.TestCase):
    
    def test_add_integers(self):
        result = SimpleCalculator.add(1, 2)
        self.assertEqual(result, 3)  

    def test_add_floats(self):
        result = SimpleCalculator.add(1.5, 2.5)
        self.assertEqual(result, 4.0)  

    def test_add_strings(self):
        result = SimpleCalculator.add("Hello", " World")
        self.assertEqual(result, "Hello World")  

    def test_add_lists(self):
        result = SimpleCalculator.add([1, 2], [3, 4])
        self.assertEqual(result, [1, 2, 3, 4]) 

class TestSubtractFunction(unittest.TestCase):
    
    def test_add_integers(self):
        result = SimpleCalculator.subtract(5, 2)
        self.assertEqual(result, 3)  

    def test_add_floats(self):
        result = SimpleCalculator.subtract(6.5, 2.5)
        self.assertEqual(result, 4.0) 

class TestMultiplyFunction(unittest.TestCase):
    
    def test_add_integers(self):
        result = SimpleCalculator.multiply(5, 2)
        self.assertEqual(result, 10)  

    def test_add_floats(self):
        result = SimpleCalculator.multiply(2.5, 2.5)
        self.assertEqual(result, 6.25) 

class TestDivideFunction(unittest.TestCase):
    
    def test_add_integers(self):
        result = SimpleCalculator.divide(10, 2)
        self.assertEqual(result, 5)  

    def test_add_floats(self):
        result = SimpleCalculator.divide(10.5, 2.5)
        self.assertEqual(result, 4.2) 

    # def test_add_raises_type_error(self):
    #     with self.assertRaises(ZeroDivisionError):
    #         SimpleCalculator.divide(5, 0) 


if __name__ == '__main__':
    unittest.main()