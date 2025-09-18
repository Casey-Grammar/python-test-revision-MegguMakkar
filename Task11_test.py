import unittest
from unittest.mock import patch
import io
import sys
import task11

class TestTask11(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['COFFEE', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_uppercase_order(self, mock_stdout, mock_input):
        """Test with uppercase drink order"""
        task11.main()
        expected_output = "2 COFFEES COMING RIGHT UP!\nThe barrister needs 8 scoops of coffee in the coffee making machine"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
    
    @patch('builtins.input', side_effect=['coffee', 'COFFEE', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_lowercase_order_then_uppercase(self, mock_stdout, mock_input):
        """Test with lowercase order first, then uppercase after prompt"""
        task11.main()
        expected_output = "I DIDN'T HEAR YOUR ORDER!\n1 COFFEES COMING RIGHT UP!\nThe barrister needs 4 scoops of coffee in the coffee making machine"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
    
    @patch('builtins.input', side_effect=['TEA', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_tea_order(self, mock_stdout, mock_input):
        """Test with uppercase TEA order"""
        task11.main()
        expected_output = "3 TEAS COMING RIGHT UP!\nThe barrister needs 12 scoops of coffee in the coffee making machine"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
    
    @patch('builtins.input', side_effect=['ESPRESSO', '5'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_espresso_order(self, mock_stdout, mock_input):
        """Test with uppercase ESPRESSO order"""
        task11.main()
        expected_output = "5 ESPRESSOS COMING RIGHT UP!\nThe barrister needs 20 scoops of coffee in the coffee making machine"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
    
    @patch('builtins.input', side_effect=['Coffee', 'COFFEE', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mixed_case_order(self, mock_stdout, mock_input):
        """Test with mixed case order, should prompt for reorder"""
        task11.main()
        expected_output = "I DIDN'T HEAR YOUR ORDER!\n2 COFFEES COMING RIGHT UP!\nThe barrister needs 8 scoops of coffee in the coffee making machine"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
        
    @patch('builtins.input', side_effect=['LATTE', '0'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_zero_quantity(self, mock_stdout, mock_input):
        """Test with zero quantity"""
        task11.main()
        expected_output = "0 LATTES COMING RIGHT UP!\nThe barrister needs 0 scoops of coffee in the coffee making machine"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()