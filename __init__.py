import unittest
import math
import circle
import rectangle
import square
import triangle

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)
        
    def test_square_mul(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_float_area(self):
        res = rectangle.area(3.5, 2.5)
        self.assertEqual(res, 8.75)

    def test_area_string_input(self):
        with self.assertRaises(TypeError):
            rectangle.area("10", 5)
            
    def test_area_negative_width(self):
        with self.assertRaises(ValueError):
            rectangle.area(-5, 10)
            
    def test_area_negative_height(self):
        with self.assertRaises(ValueError):
            rectangle.area(5, -10)
            
    def test_area_both_negative(self):
        with self.assertRaises(ValueError):
            rectangle.area(-5, -10)

    def test_perimeter_normal(self):
        res = rectangle.perimeter(5, 10)
        self.assertEqual(res, 30)
        
    def test_perimeter_zero(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)
        
    def test_perimeter_float(self):
        res = rectangle.perimeter(3.5, 2.5)
        self.assertEqual(res, 12.0)
    
    def test_perimeter_string_input(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("10", 5)
            
    def test_perimeter_negative_width(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-5, 10)
            
    def test_perimeter_negative_height(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(5, -10)
            
    def test_perimeter_both_negative(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-5, -10)
            
    def test_perimeter_none_input(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(None, 5)

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)
       
    def test_positive_area(self):
        res = circle.area(9)
        self.assertEqual(res, math.pi * 81)
        
    def test_negative_area(self):
        with self.assertRaises(ValueError):
            circle.area(-1)
            
    def test_float_area(self):
        res = circle.area(2.5)
        self.assertAlmostEqual(res, math.pi * 6.25, places=5)

    def test_zero_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)
       
    def test_positive_perimeter(self):
        res = circle.perimeter(5)
        self.assertEqual(res, 2 * math.pi * 5)
        
    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-1)
            
    def test_float_perimeter(self):
        res = circle.perimeter(3.5)
        self.assertAlmostEqual(res, 2 * math.pi * 3.5, places=5)

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)
       
    def test_positive_area(self):
        res = square.area(5)
        self.assertEqual(res, 25)
        
    def test_negative_area(self):
        with self.assertRaises(ValueError):
            square.area(-1)
            
    def test_float_area(self):
        res = square.area(2.5)
        self.assertEqual(res, 6.25)

    def test_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)
       
    def test_positive_perimeter(self):
        res = square.perimeter(5)
        self.assertEqual(res, 20)
        
    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            square.perimeter(-1)
            
    def test_float_perimeter(self):
        res = square.perimeter(3.5)
        self.assertEqual(res, 14)

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = triangle.area(0, 5)
        self.assertEqual(res, 0)
       
    def test_positive_area(self):
        res = triangle.area(6, 4)
        self.assertEqual(res, 12)
        
    def test_negative_area(self):
        with self.assertRaises(ValueError):
            triangle.area(-1, 5)
            
    def test_float_area(self):
        res = triangle.area(3.5, 2.5)
        self.assertEqual(res, 4.375)

    def test_zero_perimeter(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)
       
    def test_positive_perimeter(self):
        res = triangle.perimeter(4, 4, 5)
        self.assertEqual(res, 13)
        
    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-1, 2, 3)
            
    def test_float_perimeter(self):
        res = triangle.perimeter(2.5, 3.5, 4.5)
        self.assertEqual(res, 10.5)

if __name__ == "__main__":
    unittest.main()

