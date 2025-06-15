import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test cases for SimpleCalculator class"""
    
    def setUp(self):
        """Set up test fixture before each test method"""
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        """Test addition operation with various inputs"""
        self.assertEqual(self.calc.add(2, 3), 5)                # Positive numbers
        self.assertEqual(self.calc.add(-1, -1), -2)             # Negative numbers
        self.assertEqual(self.calc.add(0, 5), 5)                # Zero as first operand
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)          # Floating point numbers
        self.assertEqual(self.calc.add(-1, 1), 0)               # Negative and positive
    
    def test_subtraction(self):
        """Test subtraction operation with various inputs"""
        self.assertEqual(self.calc.subtract(5, 3), 2)           # Positive result
        self.assertEqual(self.calc.subtract(3, 5), -2)          # Negative result
        self.assertEqual(self.calc.subtract(0, 5), -5)          # Zero as first operand
        self.assertEqual(self.calc.subtract(2.5, 1.5), 1.0)     # Floating point numbers
        self.assertEqual(self.calc.subtract(-1, -1), 0)         # Negative numbers
    
    def test_multiplication(self):
        """Test multiplication operation with various inputs"""
        self.assertEqual(self.calc.multiply(2, 3), 6)           # Positive numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)         # Negative and positive
        self.assertEqual(self.calc.multiply(0, 5), 0)           # Zero multiplication
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)      # Floating point numbers
        self.assertEqual(self.calc.multiply(-2, -2), 4)         # Negative numbers
    
    def test_division(self):
        """Test division operation with various inputs"""
        self.assertEqual(self.calc.divide(6, 3), 2)             # Exact division
        self.assertEqual(self.calc.divide(5, 2), 2.5)           # Floating point result
        self.assertEqual(self.calc.divide(-6, 3), -2)           # Negative numerator
        self.assertEqual(self.calc.divide(6, -3), -2)           # Negative denominator
        self.assertEqual(self.calc.divide(0, 5), 0)             # Zero numerator
        self.assertIsNone(self.calc.divide(5, 0))               # Division by zero
        self.assertIsNone(self.calc.divide(0, 0))               # Zero division by zero

if __name__ == '__main__':
    unittest.main()
