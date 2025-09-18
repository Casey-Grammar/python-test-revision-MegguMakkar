import unittest
from unittest.mock import patch
import io
import sys
import task8

class TestTask8(unittest.TestCase):
    
    @patch('builtins.input', return_value='David Jones')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_david_jones(self, mock_stdout, mock_input):
        """Test with first name 'David' and last name 'Jones'"""
        task8.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Your call sign is: Daones")
    
    @patch('builtins.input', return_value='John Smith')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_john_smith(self, mock_stdout, mock_input):
        """Test with first name 'John' and last name 'Smith'"""
        task8.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Your call sign is: Jomith")
    
    @patch('builtins.input', return_value='Mary Johnson')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mary_johnson(self, mock_stdout, mock_input):
        """Test with first name 'Mary' and last name 'Johnson'"""
        task8.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Your call sign is: Manson")
    
    @patch('builtins.input', return_value='Li Wang')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_short_names(self, mock_stdout, mock_input):
        """Test with short first name 'Li' and short last name 'Wang'"""
        task8.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Your call sign is: LiWang")
    
    @patch('builtins.input', return_value='Alexander Williamson')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_long_names(self, mock_stdout, mock_input):
        """Test with long names"""
        task8.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Your call sign is: Almson")
    
    @patch('builtins.input', return_value='Jean-Pierre Montoya')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_hyphenated_first_name(self, mock_stdout, mock_input):
        """Test with hyphenated first name"""
        task8.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Your call sign is: Jetoya")
    
    @patch('builtins.input', return_value='AB CDEF')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_minimum_length_names(self, mock_stdout, mock_input):
        """Test with minimum length names: 2-letter first name, 4-letter last name"""
        task8.main()
        self.assertEqual(mock_stdout.getvalue().strip(), "Your call sign is: ABCDEF")
    
    @patch('builtins.input', side_effect=['SingleName', 'John Smith'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_single_name_input_error(self, mock_stdout, mock_input):
        """Test handling of single name input (should raise IndexError)"""
        with self.assertRaises(IndexError):
            task8.main()

if __name__ == '__main__':
    unittest.main()