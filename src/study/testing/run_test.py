import unittest
import calculate

class TestCalculateModule(unittest.TestCase):
    def test_normal(self):
        test_param = 10
        expect_output = 15
        result = calculate.sum(test_param)
        self.assertEqual(result, expect_output)

    def test_value_error(self):
        test_param = "hhhhhh"
        result = calculate.sum(test_param)
        self.assertIsInstance(result, ValueError)
    
    def test_type_error(self):
        test_param = None
        result = calculate.sum(test_param)
        self.assertIsInstance(result, TypeError)

if __name__ == '__main__':
    unittest.main()