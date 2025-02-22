import unittest
from  import item

class TestItem(unittest.TestCase):
"""Test Suite"""

    def setUp(self):
        self.calc = Calculator()
    
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2,2))

if __name__=='__main__':
    unittest.main()